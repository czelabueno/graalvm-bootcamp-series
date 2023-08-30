import sys
import time
import psutil
import re

import numpy as np
import subprocess
import matplotlib.pyplot as plt
import concurrent.futures

def get_process_info(pid):
    process = psutil.Process(pid)
    cpu_percent = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    memory_usage = memory_info.rss / (1024 ** 2)  # Convert bytes to megabytes

    return cpu_percent, memory_usage


def parse_hey_output(output):
    lines = output.decode('utf-8').splitlines()
    rps = None
    for line in lines:
        if 'Requests/sec' in line:
            rps = float(line.split(':')[1].strip())
            break
    
    return rps

def extract_response_histogram(output):
    output_str = output.decode('utf-8')  # Convert bytes to string
    response_histogram = re.search(r'Response time histogram:(.*?)Latency distribution:', output_str, re.DOTALL)
    if response_histogram:
        histogram_data = response_histogram.group(1).strip()
        return histogram_data
    return ''

def process_load_test(pid):
    try:    
        hey_output = subprocess.check_output(['hey', '-z', '15s', '-c', '4', 'http://localhost:8080/community'])
        return hey_output
    except psutil.NoSuchProcess:
        return None
    except ValueError:
        return None


# Get the process ID from command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script_name.py <pid>")
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <pid>")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_load_test = executor.submit(process_load_test, pid)
            future_process_info = executor.submit(get_process_info, pid)

        hey_output = future_load_test.result()
        cpu_percent, memory_usage = future_process_info.result()

        print(hey_output.decode('utf-8'))

        # Parse `hey` output to extract RPS data
        rps = parse_hey_output(hey_output)

        # Data for the response time distribution subplot
        response_histogram_data = extract_response_histogram(hey_output)
        lines = response_histogram_data.split('\n')

        response_time_values = []
        frequency_values = []

        for line in lines:
            if '[' in line and ']' in line:
                parts = line.split('[')
                time = float(parts[0].strip())
                frequency = int(parts[1].split(']')[0])
                response_time_values.append(time)
                frequency_values.append(frequency)
        

        # Data for the bar graph
        labels = ['CPU', 'Memory']
        values = [cpu_percent, memory_usage]

        # Create subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        # Plot resource consumption data
        ax1.bar(labels, values, color=['blue', 'green'])
        ax1.set_xlabel('Resource')
        ax1.set_ylabel('Usage')
        ax1.set_title(f'Resource Consumption for PID {pid}')
        ax1.set_ylim(0, max(values) + 10)

        # Plot response time distribution data
        ax2.plot(response_time_values, frequency_values, marker='o')
        ax2.set_xlabel('Response Time')
        ax2.set_ylabel('Frequency')
        ax2.set_title(f'Response Time Distribution - RPS: {rps}')

        plt.tight_layout()
        plt.savefig('realtime_graph.png')

    except ValueError:
        print("Invalid PID provided.")


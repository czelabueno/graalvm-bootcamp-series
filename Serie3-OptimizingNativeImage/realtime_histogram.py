import sys
import os
import time
import psutil
import re
import statistics

import numpy as np
import subprocess
import matplotlib.pyplot as plt
import concurrent.futures

def get_process_info(pid, duration):
    memory_mb = []
    cpu_percent = []
    time_counter = []

    start_time = time.time()  # Record the start time
    while time.time() - start_time < duration:
        try:
            process = psutil.Process(pid)
            memory_mb.append(process.memory_info().rss / (1024 * 1024))  # Convert bytes to MB
            cpu_percent.append(process.cpu_percent(interval=0.010))
            time_counter = time.time() - start_time  # Calculate time elapsed
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            break

    return time_counter, memory_mb, cpu_percent

def plot_latency_distribution(response_time_values, frequency_values, rps, prefix):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot response time distribution data
    ax1.plot(response_time_values, frequency_values, marker='o')
    ax1.set_xlabel('Response Time')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'Response Time Distribution - RPS: {rps}')
    ax1.grid(True)

    plt.tight_layout()

    # Ensure the directory for saving exists
    save_path = f'bench-histograms/{prefix}'
    os.makedirs(save_path, exist_ok=True)

    # Save the figure in the specified path
    plt.savefig(f'{save_path}/{prefix}_latency_graph.png')
    


def plot_resource_consumption(time_counter, memory_mb, cpu_percent, prefix, pid):

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('Memory MB', color=color)
    ax1.plot(range(1, len(memory_mb) + 1), memory_mb, label='Memory MB', color=color, linestyle='-')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 170)
    ax1.set_title(f'Resource Consumption for PID {pid}')

    ax1.grid(True)

    ax2 = ax1.twinx()  # Create a secondary y-axis sharing the same x-axis

    color = 'tab:red'
    ax2.set_ylabel('CPU %', color=color)
    ax2.plot(range(1, len(cpu_percent) + 1), cpu_percent, label='CPU %', color=color, linestyle='-')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 800)  # CPU percentage is between 0 and 100
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/100:.2f}s'))  # Convert to seconds

    # Adjust this value to control the space between the plot and the summary table
    table_bbox = [0.25, -0.25, 0.5, 0.12]  # [left, bottom, width, height]

    # Summary table
    summary_data = [
        ['Metric', 'Max', 'Min', 'Average', 'Latest'],
        ['Memory MB', f'{max(memory_mb):.2f}', f'{min(memory_mb):.2f}', f'{statistics.mean(memory_mb):.2f}', f'{memory_mb[-1]:.2f}'],
        ['CPU Percent', f'{max(cpu_percent):.2f}', f'{min(cpu_percent):.2f}', f'{statistics.mean(cpu_percent):.2f}', f'{cpu_percent[-1]:.2f}']
    ]

    table = plt.table(cellText=summary_data,
                      colLabels=None,
                      cellLoc='center',
                      bbox=table_bbox,
                      colWidths=[0.15, 0.1, 0.1, 0.1, 0.1]
                      )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.tight_layout()

    # Ensure the directory for saving exists
    save_path = f'bench-histograms/{prefix}'
    os.makedirs(save_path, exist_ok=True)

    # Save the figure in the specified path
    plt.savefig(f'{save_path}/{prefix}_consumption_graph.png')

    
def parse_hey_output(output):
    lines = output.decode('utf-8').splitlines()
    rps = None
    for line in lines:
        if 'Requests/sec' in line:
            rps = float(line.split(':')[1].strip())
            break
    
    return rps

def process_load_test(pid, prefix):
    try:    
        hey_output = subprocess.check_output(['hey', '-z', '15s', '-c', '4', 'http://localhost:8080/community'])
        save_path = f'bench-histograms/{prefix}'
        os.makedirs(save_path, exist_ok=True)
        output_file = f'{save_path}/hey_load_test_output.md'
        # Save the output to the specified file
        with open(output_file, "w") as file:
            file.write(hey_output.decode('utf-8'))
        print(f"Process output saved to {output_file}")
        return hey_output
    except psutil.NoSuchProcess:
        return None
    except ValueError:
        return None

def extract_latency_histogram(output):
    output_str = output.decode('utf-8')  # Convert bytes to string
    response_histogram = re.search(r'Response time histogram:(.*?)Latency distribution:', output_str, re.DOTALL)
    response_time_values = []
    frequency_values = []

    if response_histogram:
        lines = response_histogram.group(1).strip().split('\n')
        for line in lines:
            if '[' in line and ']' in line:
                parts = line.split('[')
                time = float(parts[0].strip())
                frequency = int(parts[1].split(']')[0])
                response_time_values.append(time)
                frequency_values.append(frequency)

    return response_time_values, frequency_values


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python realtime_histogram.py <pid> <image_type>")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
        prefix = str(sys.argv[2])

        duration = 15  # Monitoring duration in seconds

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_load_test = executor.submit(process_load_test, pid, prefix)
            future_process_info = executor.submit(get_process_info, pid, duration)

        hey_output = future_load_test.result()
        # Parse `hey` output to extract RPS data
        rps = parse_hey_output(hey_output)
        # Parse `hey` output to extract response_time and frequency data
        response_time_values, frequency_values = extract_latency_histogram(hey_output)

        time_counter, memory_mb, cpu_percent = future_process_info.result()

        plot_resource_consumption(time_counter, memory_mb, cpu_percent, prefix, pid)
        plot_latency_distribution(response_time_values, frequency_values, rps, prefix)

        print(hey_output.decode('utf-8'))

    except ValueError:
        print("Invalid PID provided.")


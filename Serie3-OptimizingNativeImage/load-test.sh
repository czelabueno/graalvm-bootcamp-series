#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <profile>"
    exit 1
fi

# Access the first argument provided
profile="$1"

NI_EXECUTABLE_PATH="quarkus-aot-sample/target/quarkus-aot-sample-${profile}-runner"

# Step 0: Check if the executable is already running and kill its process
if ps aux | grep -q "[${NI_EXECUTABLE_PATH:0:1}]${NI_EXECUTABLE_PATH:1}"; then
    pids=$(ps aux | grep "[${NI_EXECUTABLE_PATH:0:1}]${NI_EXECUTABLE_PATH:1}" | awk '{print $2}')
    for pid in $pids; do
        echo 'Killing PID: '$pid
        kill $pid
    done
fi

# Step 1: Run the Native executable
$NI_EXECUTABLE_PATH &

sleep 3

# Step 2: Get the PID of the running executable
pid_ni=$(ps aux | grep "[${NI_EXECUTABLE_PATH:0:1}]${NI_EXECUTABLE_PATH:1}" | awk '{print $2; exit}')

# Step 3: Pass the PID to a second command line (replace "your_command" with the actual command you want to run)
python realtime_histogram.py $pid_ni $profile &

echo -ne "Load Testing...PID "$pid_ni" "

# Progress bar
for i in `seq 16`;
    do echo -ne "#";
    sleep 1s;
done
echo -ne " DONE"

# Step4: Clean and kill natice executable process
# Step 0: Check if the executable is already running and kill its process
if ps aux | grep -q "[${NI_EXECUTABLE_PATH:0:1}]${NI_EXECUTABLE_PATH:1}"; then
    pids=$(ps aux | grep "[${NI_EXECUTABLE_PATH:0:1}]${NI_EXECUTABLE_PATH:1}" | awk '{print $2}')
    for pid in $pids; do
        echo 'Killing PID: '$pid
        kill $pid
    done
fi
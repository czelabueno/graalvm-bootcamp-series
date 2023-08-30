#!/bin/bash

# Step 1: Run the Native executable
./target/native-executable &

# Step 2: Get the PID of the running executable
pid=$(pgrep target/native-executable)

# Step 3: Pass the PID to a second command line (replace "your_command" with the actual command you want to run)
python realtime_histogram.py $pid


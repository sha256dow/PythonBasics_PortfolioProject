# Creating a program that constantly runs (looping), verifying currently running process and return their NAME | PID | RAM usage :

import psutil
import time

def listing_process():
 
    processes = psutil.process_iter()
    
    # Header:
    print("{:<10} {:<10} {:<10}".format("NAME", "PID", "RAM Usage"))
    
    # Iterating:
    for process in processes:
        try:
            # Get Process Name:
            name = process.name()
            name = name.upper()
            
            # Get Process PID:
            pid = process.pid
            
            # Get RAM Usage:
            memory = process.memory_info().rss / (1024 * 1024)  # Bytes -> MegaBytes
            
            print("{:<40} {:<10} {:<10.2f} MB".format(name, pid, memory))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Main Loop:
while True:
    listing_process()
    time.sleep(60) # Change time.sleep value due your needs


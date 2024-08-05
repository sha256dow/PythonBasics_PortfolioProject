# Creating a program to find process memory address:

import psutil

def listing_programs():
    print("Currently executing:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Nome: {process.info['name']}")

def get_memory_usage(process_name):
    for process in psutil.process_iter(['pid', 'name', 'memory_info', 'cmdline']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            name = process.info['name']
            memory = process.info['memory_info'].rss
            address = process.info['cmdline']
            return pid, name, memory, address

def main():
    listing_programs()
    program_name = input("\nProgram to monitoring: ")
    pid, name, memory, address = get_memory_usage(program_name)
    print(f"PID '{name}': {pid}")
    print(f"RAM Usage: {memory} bytes")
    print(f"Memory Address: {address}")

if __name__ == "__main__":
    main()


# Creating a Python program to list all ESTABLISHED connections and identify its server based on processes.

import psutil

def list_established_connections():
    established_connections = []
    for connection in psutil.net_connections(kind='inet'):
        if connection.status == psutil.CONN_ESTABLISHED:
            established_connections.append(connection)
    return established_connections

def identify_servers_and_processes(connections):
    processes_servers = {}
    for connection in connections:
        remote_address = connection.raddr
        pid = connection.pid
        if remote_address and pid:
            process = psutil.Process(pid)
            process_name = process.name()
            ipAddress = remote_address.ip
            port = remote_address.port
            if ipAddress not in processes_servers:
                processes_servers[ipAddress] = [(port, process_name)]
            else:
                processes_servers[ipAddress].append((port, process_name))
    return processes_servers

def main():
    established_connections = list_established_connections()
    processes_servers = identify_servers_and_processes(established_connections)
    
    print("ESTABLISHED Connections: ")
    print("----------------------------------------------")
    for ipAddress, processes_ports in processes_servers.items():
        print(f"Sever IP Address: {ipAddress}")
        for port, process_name in processes_ports:
            print(f"   Porta: {port:<7} Process: {process_name}")
        print()

if __name__ == "__main__":
    main()

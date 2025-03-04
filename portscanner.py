from queue import Queue
import socket
import threading

target = '127.0.0.1'
port_queue = Queue()  # Create an instance of Queue
open_ports = []       # Define the list to store open ports

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.close()  # Always close the socket after use
        return True
    except socket.error:  # Catch specific socket exceptions
        return False

def fill_queue(ports):
    for port in ports:
        port_queue.put(port)

def worker():
    while not port_queue.empty():
        port = port_queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))

# Create a range of ports to scan
ports = range(1, 1024)
fill_queue(ports)

thread_list = []
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are:", open_ports)

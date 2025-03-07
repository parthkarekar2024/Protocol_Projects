import socket

def udp_server():
    host = "127.0.0.1"  # Localhost
    port = 54321        # Port number for the server

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
        # Wait to receive data from a client (up to 1024 bytes)
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received message from {client_address}: {data.decode()}")

        # Send a response back to the client
        response = "Message received"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_server()

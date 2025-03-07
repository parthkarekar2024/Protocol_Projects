import socket


def tcp_server():
    host = '127.0.0.1'  # Localhost
    port = 12345  # Port to listen on

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for incoming connections
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a new connection
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received:", data.decode())

        # Send a response back to the client
        response = "Message received"
        client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()


if __name__ == "__main__":
    tcp_server()

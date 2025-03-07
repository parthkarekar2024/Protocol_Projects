import socket


def tcp_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 12345  # The same port as used by the server

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Send a message to the server
    message = "Hello, server!"
    client_socket.send(message.encode())

    # Receive the server's response (up to 1024 bytes)
    response = client_socket.recv(1024)
    print("Server response:", response.decode())

    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    tcp_client()

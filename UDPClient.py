import socket

def udp_client():
    host = "127.0.0.1"  # Server address (localhost)
    port = 54321        # The same port as used by the server

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Message to send
    message = "TCP is better!"
    client_socket.sendto(message.encode(), (host, port))
    print(f"Sent message to server: {message}")

    # Wait for the server's response
    response, server_address = client_socket.recvfrom(1024)
    print(f"Received response from server: {response.decode()}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    udp_client()

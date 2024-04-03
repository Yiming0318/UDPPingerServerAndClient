"""
This is the UDP Pinger Server, this module is to generate randomized lost packets
"""
# Yiming Ge
import random
from socket import AF_INET, SOCK_DGRAM, socket

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
# The empty string '' serves as a wildcard, 
# meaning the server is bound to all available interfaces on the host machine
serverSocket.bind(('', 12000))

while True:
    # Generate a random number for simulating packet loss
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    message = message.decode().upper()

    #  print the response message from server
    print(f"Message received from {address}: {message}")   

    # If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    message = message.encode()
    serverSocket.sendto(message, address)

"""
This is the UDP Client, this module is to
(1) send the ping message using UDP (Note: Unlike TCP, you do not need to establish
 a connection first, since UDP is a connectionless protocol.)
(2) print the response message from server, if any 
(Ping message format: Ping sequence_number time
where sequence_number starts at 1 and progresses to 10 for each successive ping message
sent by the client, and time is the time when the client sends the message.)
(3) calculate and print the round trip time (RTT), in seconds, of each packet,
 if server responses (report the minimum, maximum, and average RTTs at the end of all pings from the client. 
 In addition, calculate the packet loss rate)
(4) otherwise, print “Request timed out”
"""
# Yiming Ge
import time
from socket import AF_INET, SOCK_DGRAM, socket, timeout

####Setup Client Basic Part#######
# Create a UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# Get the client wait up to one second for a reply
timeout_seconds = 1.0
client_socket.settimeout(timeout_seconds)

# Server address and port we will use
server_address = ('localhost', 12000)  # localhost test
# server_address = ('10.0.0.40', 12000) # network ip test
# number of pings we will do in this client
number_of_pings = 10

#####Calculation Part#######
# Initialization
rtt_map = {} # hashmap to store the rtt for each avaliable packet
lost_packets = 0 # track the number of lost_packets

for sequence_number in range(1, number_of_pings + 1):
    send_time = time.time() # get the start sending time
    # Create the ping message
    message = f'Ping {sequence_number} {send_time}'.encode()
    try:
        # Send the message to the UDPPingerServer
        client_socket.sendto(message, server_address)
        # Calculate the round-trip time after receiving the server response sucessfully
        response, server_address = client_socket.recvfrom(1024)
        receive_time = time.time()
        rtt = receive_time - send_time
        # put them into the rtt hashmap for futher calculation
        rtt_map[sequence_number] = rtt
        # Print the server's response message and its RTT
        print(f'Response message from {server_address}: {response.decode()} and its RTT: {rtt} seconds')

    except timeout:
        # Handle the timeout case 
        # if no reply is received within time out seconds,
        # client program should assume that the packet was lost during transmission across the network
        lost_packets += 1
        print(f'Request timed out for sequence number {sequence_number}')

# Summary for this calculation
min_rtt = min(rtt_map.values())
max_rtt = max(rtt_map.values())
sum_rtt = sum(rtt_map.values())
avaliable_rtt_number = len(rtt_map)
print(f'###############Summary Stats##################')
print(f'Minimum RTT: {min_rtt} seconds')
print(f'Maximum RTT: {max_rtt} seconds')
print(f'Average RTT: {sum_rtt / avaliable_rtt_number} seconds')
print(f'Packet loss rate: {lost_packets / number_of_pings * 100}%')

# Close the socket
client_socket.close()

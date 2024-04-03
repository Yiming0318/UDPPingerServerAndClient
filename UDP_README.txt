Overview of the program: 
The UDP Client program is designed to test the network connection to a server by sending a series of 10 ping messages using the UDP protocol. It calculates and displays the round trip time (RTT) for each response received from the server and provides summary statistics at the end, including the minimum, maximum, and average RTT, as well as the packet loss rate.

Instructions:
Ensure Python is installed on your system.
Download the UDPClient.py and UDPPingerServer.py files to your local machine.
Run the server program in one terminal window: python UDPPingerServer.py.
Run the client program in another terminal window: python UDPClient.py. (*change the server address in UDPClient if you want to test your network instead of the localhost)
Observe the output in both terminal windows.

Dependencies: No external libraries are required beyond Python's standard library.

Troubleshooting:
If you encounter a "Connection timeout" error, ensure the server is running and accessible from the client's network.
For any address-related errors, verify the server's IP address and port number specified in the client's script.
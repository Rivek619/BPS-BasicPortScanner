#!/bin/python3 

import sys
import socket
from datetime import datetime

# Defining the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 bps.py <ip>")

# Banner
print("=" * 50)
print("BBBBB   PPPP    SSS                         ")
print("B   BB  P   PP  S                           ")
print("BBBBB   PPPP     SSS                        ")
print("B    B  P         S      -Rivek.exe         ")
print("BBBBB   P      SSSS                         ")
print("=" * 50)
print("Scanning target: " + target)  # Added space after "target"
print("Time started: " + str(datetime.now()))
print("=" * 50)

# Port Scanning
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Returns an error indicator; 0 for open, 1 for closed
        if result == 0:
            print(f"Port {port} is open")
        s.close()

# Exception handling
except KeyboardInterrupt:
    print("\nExiting program")  # Corrected spelling of "Exiting"
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect")
    sys.exit()


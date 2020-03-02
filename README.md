# SYN-Flood-attack-simulator
A Python script that simulates SYN-Flood attack using SCAPY module.
This script generates IPv4 Packets with its SYN flag set in TCP layer. This script will generate and flood multiple SYN packets with random source ports to avoid detection of TCP packet retransmits by IDS/IPS, if any.


# Requirement
1. Python 3.0 +
2. Linux
3. Scapy module

# Note
Attacking script creates SYN packets at Application level. So attacker machine’s Kernel stack layer will send RST for each initiated TCP-handshake request.

# Solution
RST Packets should be blocked at Firewall level or iptables in case of Linux.




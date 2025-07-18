#!/usr/bin/env python3
from scapy.all import *
from datetime import datetime
import time

LOG_FILE = "web_visits.log"
PACKET_LIMIT = 25  
DELAY_SECONDS = 2    # Time between outputs

def log_visit(packet):
    if not packet.haslayer(TCP) or not packet.haslayer(IP):
        return
    
    src = f"{packet[IP].src}:{packet[TCP].sport}"
    dst = f"{packet[IP].dst}:{packet[TCP].dport}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if packet[TCP].dport == 80 and packet.haslayer(Raw): # HTTP (Port 80)
        try:
            host = next(line.split("Host: ")[1] for line in str(packet[Raw].load).split('\\r\\n') if "Host: " in line)
            log = f"[{timestamp}] HTTP: {src} -> {host} (Port 80)"
            print(log)
            return log + "\n"
        except:
            pass
    
    
    elif packet[TCP].dport == 443: # HTTPS (Port 443)
        log = f"[{timestamp}] HTTPS: {src} -> {packet[IP].dst} (Port 443)"
        print(log)
        return log + "\n"
    
    return None

def main():
    print(f"\n...Monitoring web traffic (HTTP/HTTPS)...\n")
    print("Press Ctrl+C to stop\n")
    
    packet_count = 0
    with open(LOG_FILE, "a") as log_file:
        def callback(packet):
            nonlocal packet_count
            if packet_count >= PACKET_LIMIT:
                return
            
            log_entry = log_visit(packet)
            if log_entry:
                log_file.write(log_entry)
                packet_count += 1
                time.sleep(DELAY_SECONDS)  
        
        sniff(prn=callback, store=False, filter="tcp port 80 or tcp port 443")

    print(f"\n...Captured {packet_count} packets. Log saved to '{LOG_FILE}'...")

if __name__ == "__main__":
    main()
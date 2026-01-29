import socket

# BioCyberWall - General Cybersecurity Project
# Purpose: Basic Network Port Scanner for security assessment

def scan_ports(target_ip):
    print(f"Starting security scan on: {target_ip}")
    # Common ports to check
    ports = [21, 22, 80, 443, 8080]
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[!] Port {port} is OPEN - Potential Risk")
        else:
            print(f"[-] Port {port} is closed")
        s.close()

if __name__ == "__main__":
    # You can change this to your local network IP for testing
    target = "127.0.0.1" 
    scan_ports(target)

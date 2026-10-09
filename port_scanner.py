"""
Simple TCP Port Scanner (beginner friendly)

Only scan computers and networks you own or have explicit permission to test.
Scanning systems without permission may be illegal.

Usage examples:
    python port_scanner.py 127.0.0.1
    python port_scanner.py 192.168.1.1 --start 1 --end 1024
    python port_scanner.py scanme.nmap.org --start 20 --end 100
"""

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

# A few well-known ports and what they are usually used for
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP (alt)",
}


def scan_port(host, port, timeout=1.0):
    """Try to connect to one port. Returns the port number if it's open, else None."""
    # AF_INET = IPv4, SOCK_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)  # don't wait forever on closed/filtered ports
        # connect_ex returns 0 if the connection succeeded (port is open)
        result = sock.connect_ex((host, port))
        if result == 0:
            return port
    return None


def main():
    # Read options from the command line
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="IP address or hostname to scan")
    parser.add_argument("--start", type=int, default=1, help="first port (default 1)")
    parser.add_argument("--end", type=int, default=1024, help="last port (default 1024)")
    parser.add_argument("--timeout", type=float, default=1.0, help="seconds to wait per port")
    parser.add_argument("--threads", type=int, default=100, help="how many ports to check at once")
    args = parser.parse_args()

    # Basic input checks
    if not (1 <= args.start <= args.end <= 65535):
        print("Ports must be between 1 and 65535, and start must be <= end.")
        return

    # Turn a hostname like "example.com" into an IP address
    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"Could not resolve host: {args.host}")
        return

    print(f"Scanning {args.host} ({ip}) ports {args.start}-{args.end}...")

    ports = range(args.start, args.end + 1)
    open_ports = []

    # Threads let us check many ports at the same time, which is much faster
    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        results = pool.map(lambda p: scan_port(ip, p, args.timeout), ports)
        for port in results:
            if port is not None:
                open_ports.append(port)
                service = COMMON_SERVICES.get(port, "unknown")
                print(f"  Port {port} is OPEN ({service})")

    print(f"\nDone. Found {len(open_ports)} open port(s).")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan cancelled.")

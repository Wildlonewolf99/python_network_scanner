import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

print("Thank you for using IP_Scanner by Wildlonewolf")
print("Buy me a coffee: https://paypal.me/PraveenThamotharan?country.x=MY&locale.x=en_US")

KNOWN_PORTS = [80, 443, 8006, 8080]  # Add more ports as needed

def scan_ip(ip):
    open_ports = []
    for port in KNOWN_PORTS:
        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, port))
            open_ports.append(port)
        except socket.error:
            pass
    return ip, open_ports

def scan_network(output_file=None):
    used_ips = []
    free_ips = []

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network_prefix = '.'.join(local_ip.split('.')[:-1]) + '.'

    ips_to_scan = [network_prefix + str(i) for i in range(1, 255)]

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(scan_ip, ip): ip for ip in ips_to_scan}

        with tqdm(total=len(ips_to_scan), desc="Scanning IP addresses") as pbar:
            for future in as_completed(futures):
                ip, open_ports = future.result()
                if open_ports:
                    used_ips.append((ip, open_ports))
                else:
                    free_ips.append(ip)
                pbar.update(1)

    output = ""

    output += "Used IP Addresses:\n"
    for ip, open_ports in used_ips:
        output += f"IP Address: {ip}, Open Ports: {', '.join(map(str, open_ports))}\n"

    output += "\nFree IP Addresses:\n"
    for ip in free_ips:
        output += f"{ip}\n"

    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
    else:
        print(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan local network for used and free IP addresses.")
    parser.add_argument("-o", "--output", help="Specify the output file location", default=None)
    args = parser.parse_args()

    scan_network(output_file=args.output)

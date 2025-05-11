import socket
import threading

# Function to scan a single port
def scan_port(target, port, timeout=0.5):
    """Scan a single port on the target."""
    try:
        # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for faster scanning
        sock.settimeout(timeout)
        
        # Try to connect to the target IP and port
        result = sock.connect_ex((target, port))  # connect_ex returns 0 if successful
        
        # If the result is 0, the port is open
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            with open("scan_results.txt", "a") as log_file:
                log_file.write(f"Port {port} is OPEN\n")
        else:
            print(f"❌ Port {port} is CLOSED")
            with open("scan_results.txt", "a") as log_file:
                log_file.write(f"Port {port} is CLOSED\n")
        sock.close()  # Close the socket after checking the port
    
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

# Function to scan a range of ports using threading
def scan_ports(target, start_port, end_port, timeout):
    """Scan a range of ports using threads to speed up the process."""
    print(f"\nScanning target: {target} from port {start_port} to {end_port}")
    
    # List to keep track of threads
    threads = []
    
    # Iterate over the range of ports from start_port to end_port
    for port in range(start_port, end_port + 1):  # +1 to include the end_port
        # Create a new thread to scan each port
        thread = threading.Thread(target=scan_port, args=(target, port, timeout))
        
        # Add the thread to the list of threads
        threads.append(thread)
        
        # Start the thread (this means it will begin scanning the current port)
        thread.start()

    # Wait for all threads to finish before the program ends
    for thread in threads:
        thread.join()

# Main program to execute the scanner
if __name__ == "__main__":
    try:
        # Get user input for the target (IP or domain) and port range
        target = input("Enter target IP or domain: ")
        
        # Validate the target IP or domain
        socket.gethostbyname(target)  # This will raise an error if the target is invalid

        # Get start and end ports, ensure they're valid
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range. Ensure the start port < end port and they are between 1 and 65535.")

        # Get the timeout from the user
        timeout = float(input("Enter timeout in seconds (e.g., 0.5): "))

        # Call the function to scan the specified range of ports
        scan_ports(target, start_port, end_port, timeout)
        print("\nScan complete. Results saved in 'scan_results.txt'.")
        
    except ValueError as e:
        print(f"Error: {e}")
    except socket.gaierror:
        print("Error: Invalid target IP or domain. Please try again.")

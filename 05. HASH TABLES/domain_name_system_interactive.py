import socket

def resolve_dns(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        print(f"Error resolving DNS for {domain_name}: {e}")
        return None

def main():
    while True:
        domain_name = input("Enter the domain name to resolve (or 'quit' to exit): ")
        if domain_name.lower() == 'quit':
            print("Exiting...")
            break
        
        ip_address = resolve_dns(domain_name)
        if ip_address:
            print(f"The IP address of {domain_name} is: {ip_address}")
        else:
            print(f"Failed to resolve DNS for {domain_name}")

if __name__ == "__main__":
    main()

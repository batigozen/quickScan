import socket
from colorama import Fore, Style, init

init()

def portScan(target):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{Fore.RED}Couldn't find the host {target}{Style.RESET_ALL}")
        quitApp()

    print(f"{Fore.YELLOW}Scanning target: {ip}\n--------{Style.RESET_ALL}")

    openPortCount = 0
    timeout = 0.05

    try:
        for port in range(1,1000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{Fore.GREEN}Port {port} is open{Style.RESET_ALL}")
                openPortCount += 1
            sock.close()

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Scan interrupted by user. Exiting...{Style.RESET_ALL}")
        quit()

    print(f"{Fore.YELLOW}--------{Style.RESET_ALL}\n{Fore.CYAN}Open port count: {openPortCount}{Style.RESET_ALL}")


def quitApp():
    print(f"{Fore.RED}Quitting...{Style.RESET_ALL}")
    quit()


if __name__ == "__main__":
    target = input(f"{Fore.CYAN}Enter the IP Address/Host Name: {Style.RESET_ALL}")
    timeout = 0.125

    if target == "":
        print(f"\n{Fore.RED}Please Enter a non-empty IP/Host{Style.RESET_ALL}")
        quitApp()


    portScan(target) 

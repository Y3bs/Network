import socket as s
import binascii

def get_local_machine_info():
    host_name = s.gethostname()
    ip = s.gethostbyname(host_name)
    fqdn = s.getfqdn()
    print(f"Hostname: {host_name}")
    print(f"IP: {ip}")
    print(f"FQDN: {fqdn}")

def convert_ipv4():
    for i in ['127.0.0.1','192.168.0.1','192.168.1.5']:
        packed = s.inet_aton(i)
        unpacked = s.inet_ntoa(packed)
        print(f"IP: {i} => Packed: {binascii.hexlify(packed)} => Unpacked: {unpacked}")
        print(f"IP: {i} => Packed: {packed} => Unpacked: {unpacked}")

def check_port():
    for port in [25,80]:
        for proto in ['tcp','udp']:
            try:
                print(f"Port {port}/{proto} = > {s.getservbyport(port , proto)}")
            except OSError as e:
                print(f"Port {port} offline\nError: {e}")
def convert_integer_data_to_network():
    data = 1234
    print(f"Original : {data}")
    print(f"Network byte order : {s.htonl(data)}")
    print(f"Host byte order: {s.ntohl(s.htonl(data))}")

def socket_timout():
    sk = s.socket(s.AF_INET,s.SOCK_STREAM)
    print(f"Default timeout:{sk.gettimeout()}")
    sk.settimeout(5)
    print(f"Updated timeout:{sk.gettimeout()} Seconds")

# assignment => client and server chat 



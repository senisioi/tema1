import socket
import traceback

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)

def get_location_info(ip):
    '''Folositi un API public, cum ar fi cel de la ip2loc pentru
    a afisa locatia despre IP: https://ip2loc.com/documentation'''
    oras = ''
    regiune = ''
    tara = ''
    return oras, regiune, tara

def traceroute(ip, port):
    '''Functie care are ca scop afisarea locatiilor geografice 
    de pe rutele pachetelor.
    '''
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 64
    udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)

    # trimite un mesaj UDP catre un tuplu (IP, port)
    udp_send_sock.sendto(b'ador', (ip, port))

    # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
    # aici nu verificăm daca tipul de mesaj este ICMP
    # dar ati putea verifica daca primul byte are valoarea Type == 11
    # https://tools.ietf.org/html/rfc792#page-5
    # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header
    addr = 'done!'
    try:
        data, addr = icmp_recv_socket.recvfrom(63535)
    except Exception as e:
        print("Socket timeout ", str(e))
        print(traceback.format_exc())
    print (addr)
    adresa_ip = '???'
    #oras, regiune, tara = get_location_info(adresa_ip)
    #continuati aici



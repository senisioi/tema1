# emitator Reliable UDP
from helper import *
from argparse import ArgumentParser
import socket
import logging
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)


def connect(sock, adresa_receptor, fisier):
    try:
        # TODO: trebuie sa alegeti un fisier de cel putin 100 KB pentru a fi trimis
        fisier = ''
        file_descriptor = open(fisier, 'rb')
        segment = citeste_segment(file_descriptor)
        
        seq_nr = .. # TODO: setati initial sequence number
        flags = 'S'
        checksum = 0
        octeti_header_fara_checksum = create_header_emitator(seq_nr, flags, checksum)
        
        mesaj = octeti_header_fara_checksum + segment
        checksum = calculeaza_checksum(mesaj)
        octeti_header_cu_checksum = create_header_emitator(seq_nr, flags, checksum)

        mesaj = octeti_header_cu_checksum + segment

        sock.sendto(mesaj, adresa_receptor)

        data, server = sock.recvfrom(MAX_SEGMENT)

        if verifica_checksum(data) is False:
            # TODO: daca checksum nu e ok, mesajul de la receptor trebuie ignorat
            return
        
        ack_nr, checksum, window = parse_header_receptor(data)

        logging.info('Ack Nr: "%d"', ack_nr)
        logging.info('Checksum: "%d"', checksum)
        logging.info('Window: "%d"', window)

    finally:
        sock.close()
        file_descriptor.close()

def main():
    parser = ArgumentParser(usage=__file__ + ' '
                                             '-a/--adresa IP '
                                             '-p/--port PORT'
                                             '-f/--fisier FILE_PATH',
                            description='Reliable UDP Emitter')

    parser.add_argument('-a', '--adresa',
                        dest='adresa',
                        default='receptor',
                        help='Adresa IP a receptorului (IP-ul containerului, localhost sau altceva)')

    parser.add_argument('-p', '--port',
                        dest='port',
                        default='10000',
                        help='Portul pe care asculta receptorul pentru mesaje')

    parser.add_argument('-f', '--fisier',
                        dest='fisier',
                        help='Calea catre fisierul care urmeaza a fi trimis')

    # Parse arguments
    args = vars(parser.parse_args())

    ip_receptor = args['adresa']
    port_receptor = args['port']
    fisier = args['fisier']

    adresa_receptor = (ip_receptor, port_receptor)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)


if __name__ == '__main__':
    main()
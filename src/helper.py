import struct
import socket
import logging

MAX_UINT32 = 0xFFFFFFFF
MAX_BITI_CHECKSUM = 16
MAX_SEGMENT = 1400

def compara_endianness(numar):
    '''
    https://en.m.wikipedia.org/wiki/Endianness#Etymology
        numarul 16 se scrie in binar 10000 (2^4)
        pe 8 biti, adaugam 0 pe pozitiile mai mari: 00010000
        pe 16 biti, mai adauga un octet de 0 pe pozitiile mai mari: 00000000 00010000
        daca numaratoarea incepe de la dreapta la stanga:
            reprezentarea Big Endian (Network Order) este: 00000000 00010000
                - cel mai semnificativ bit are adresa cea mai mica
            reprezentarea Little Endian este: 00010000 00000000
                - cel mai semnificativ bit are adresa cea mai mare 
    '''
    print ("Numarul: ", numar)
    print ("Network Order (Big Endian): ", [bin(byte) for byte in struct.pack('!H', numar)])
    print ("Little Endian: ", [bin(byte) for byte in struct.pack('<H', numar)])


def create_header_emitator(seq_nr, checksum, flags='S'):
    '''
    TODO: folosind struct.pack impachetati numerele in octeti si returnati valorile
    flags pot fi 'S', 'P', sau 'F'
    '''
    octeti = struct.pack(..)
    return octeti


def parse_header_emitator(octeti):
    '''
    TODO: folosind struct.unpack despachetati numerele 
    din headerul de la emitator in valori si returnati valorile
    '''
    seq_nr, checksum, spf = struct.unpack(..)
    flags = ''
    if spf & 0b100:
        # inseamna ca am primit S
        flags = 'S'
    elif spf & 0b001:
        # inseamna ca am primit F
        flags = 'F'
    elif spf & 0b010:
        # inseamna ca am primit P
        flags = 'P'
    return (seq_nr, checksum, flags)


def create_header_receptor(ack_nr, checksum, window):
    '''
    TODO: folosind struct.pack impachetati numerele in octeti si returnati valorile
    flags pot fi 'S', 'P', sau 'F'
    '''
    octeti = struct.pack(..)
    return octeti


def parse_header_receptor(octeti):
    '''
    TODO: folosind struct.unpack despachetati octetii in valori si returnati valorile
    '''
    ack_nr, checksum, window = struct.unpack(..)
    return (ack_nr, checksum, window)


def citeste_segment(file_descriptor):
    '''
        generator, returneaza cate un segment de 1400 de octeti dintr-un fisier
    '''
    yield file_descriptor.read(MAX_SEGMENT)


def exemplu_citire(cale_catre_fisier):
    with open(cale_catre_fisier, 'rb') as file_in:
        for segment in citeste_segment(file_in):
            print(segment)


def calculeaza_checksum(octeti):
    checksum = 0

    # 1. convertim sirul octeti in numere pe 16 biti
    # 2. adunam numerele in complementul lui 1, ce depaseste 16 biti se aduna la coada
    # 3. cheksum = complementarea bitilor sumei
    return checksum


def verifica_checksum(octeti):
    if calculeaza_checksum(octeti):
        return True
    return False



if __name__ == '__main__':
    compara_endianness(16)
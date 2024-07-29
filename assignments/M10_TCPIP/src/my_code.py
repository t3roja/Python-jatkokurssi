import socket

def fetch_number(IP, p):

    UPDSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    msg = "Anna luku!"
    UPDSocket.sendto(msg.encode(), (IP, p))
    
    data = UPDSocket.recvfrom(1024)

    num = data[0]

    num = int(num.decode())

    return num


if __name__=='__main__':
    pass
    #Write test code here

"""
Kirjoita funktio fetch number(IP, p), joka l¨ahett¨a¨a
parametrina saamaansa IP-osoitteeseen, porttiin p, viestin "Anna
luku!"1 UDP-protokollaa k¨aytt¨aen. Funktio palauttaa
palvelimelta paluuviestiss¨a saadun merkkijonon muutettuna
kokonaisluvuksi
"""
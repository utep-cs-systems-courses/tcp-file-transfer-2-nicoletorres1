import socket
import os
import sys


def main():
    os.fork()
    s = socket.socket()
    host = socket.gethostname()
    port = 50001

    s.bind((host, port))
    print("Server should have binded")
    fileName = open('TestRec.txt', 'wb')
    s.listen(5)

    while True:
        client, addr = s.accept()
        print("Connection from: " + str(addr))
        print("Receiving...")
        data = client.recv(1024)

        while True:
            if not data:
                break
            fileName.write(data)
            data = client.recv(1024)
        fileName.close()
        print("Done")
        client.shutdown(socket.SHUT_RD)
        client.close()
        os.wait()


if __name__ == '__main__':
    main()



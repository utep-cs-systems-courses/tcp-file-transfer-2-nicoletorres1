
'''
1. work with and without the proxy
2. support multiple clients simultaneously using fork()
3. gracefully deal with scenarios such as:
4. zero length files
5. user attempts to transmit a file which does not exist
6. file already exists on the server
7. the client or server unexpectedly disconnect

//copy from framed echo FileClient, framed socket, Fileserver

'''

import socket


def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 50001

    s.connect((host, port))

    # this is the file transfer
    file = open('TestSend.txt', 'rb')
    print("Sending file...")

    sending = file.read(1024)
    while (sending):
        print("Sending file...")
        s.send(sending)
        sending = file.read(1024)
    file.close()
    print("Done sending")
    s.shutdown(socket.SHUT_WR)
    print(s.recv(1024))

    s.close()


if __name__ == '__main__':
    main()


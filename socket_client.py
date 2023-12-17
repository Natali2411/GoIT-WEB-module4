import socket
from threading import Thread


def socket_client(ip: str, port: int, body: str) -> None:
    """
    Method creates the socket connection from socket client to server.
    :param ip: local host.
    :param port: local port.
    :param body: message for HTTP POST request.
    :return: None.
    """
    def handle(sock):
        data = body.encode()
        sock.sendto(data, server)
        print(f'Send data from client: {data.decode()} to server: {server}')
        try:
            response, address = sock.recvfrom(1024)
            print(f'Response data received on client side: {response.decode()} from address:'
                  f' {address}')
        except Exception as err:
            print(f'Response error received on client side {err}')
            return err

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port

    thread = Thread(target=handle, args=(sock, ))
    thread.start()
    thread.join()

    sock.close()

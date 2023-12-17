import json
import socket
from concurrent import futures as cf


def read_data():
    with open("storage/data.json", "r") as fh:
        try:
            file_data = json.load(fh)
        except ValueError:
            return {"users_msgs": []}
        return file_data


def write_data(data: dict):
    with open("storage/data.json", "w") as fh:
        json.dump(data, fh)


def run_server(ip: str, port: int):
    """
    Method creates connection for socket server.
    :param ip: local host.
    :param port: local port.
    :return: None.
    """
    print("Server socket")

    def handle():
        data, address = sock.recvfrom(1024)
        print(f'Received data on server: {data.decode()} from client: {address}')
        file_data = read_data()
        print(file_data)
        file_data.get("users_msgs").append(json.loads(data.decode()))
        write_data(data=file_data)
        sock.sendto(f'Send data: {data.decode()} to client: {address}'.encode(), address)
        # print(f'Send data: {data.decode()} to client: {address}')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    with cf.ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                client_pool.submit(handle)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            sock.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 5000)

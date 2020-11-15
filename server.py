import socket
import threading
from _thread import start_new_thread


def responder(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError:
            data = None

        if not data:
            print(addr[0] + " closed")
            responder_lock.release()
            break

        data = data.decode()
        response = process_response(data)

        print("Q: " + data)

        conn.send(response)


def process_response(data):
    return str(len(data)).encode()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('127.0.0.1', 666))
        sock.listen()

        while True:
            conn, addr = sock.accept()
            responder_lock.acquire()

            print(addr[0] + " connected")

            start_new_thread(responder, (conn, addr))


responder_lock = threading.Lock()
if __name__ == '__main__':
    main()

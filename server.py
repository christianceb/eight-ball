import socket
import threading
from _thread import start_new_thread
from classes.EightBall import EightBall


def responder(conn, addr):
    """
    Logic for responding to received messages
    :param conn:
    :param addr:
    :return:
    """
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError:
            # Gracefully exit when client does
            data = None

        # Release thread opened if we get something that closely resembles an exit
        if not data:
            print(addr[0] + " closed")
            responder_lock.release()
            break

        data = data.decode()
        response = process_response(data)

        # Log data received
        print("Q: " + data)

        # Send a response
        conn.send(response)


def process_response(data):
    """
    Logic for processing response goes here
    :param data: A string, mostly
    :return: A string, mostly
    """
    return eight_ball.get_response(data).encode()


def main():
    """
    Instantiate our socket and handle connections

    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('127.0.0.1', 666))
        sock.listen()

        while True:
            conn, addr = sock.accept()
            responder_lock.acquire()

            print(addr[0] + " connected")

            start_new_thread(responder, (conn, addr))


responder_lock = threading.Lock()
eight_ball = EightBall()
if __name__ == '__main__':
    main()

import socket


def run_eight_ball(sock: socket):
    while True:
        question = input("I am a sexy Magic 8-Ball: ask me almost anything or nothing to exit\nQ: ")

        if question == "":
            sock.close()
            break

        sock.send(question.encode())
        response = sock.recv(1024)
        print("A: " + str(response.decode()) + "\n")


def main():
    """
    Open a socket and connect to our server
    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect(('127.0.0.1', 666))
            run_eight_ball(sock)

        except ConnectionRefusedError:
            print("Server might be down. Exiting")


if __name__ == '__main__':
    main()

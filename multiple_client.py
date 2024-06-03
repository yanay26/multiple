import socket

def main():
    HOST = '127.0.0.1'  # Локальный адрес сервера
    PORT = 12345  # Тот же порт, который использует сервер

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Клиент подключен к серверу.")

        while True:
            message = input("Введите сообщение для отправки на сервер: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print("Ответ от сервера:", data.decode())

if __name__ == "__main__":
    main()

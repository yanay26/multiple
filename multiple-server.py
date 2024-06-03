import socket
import threading

def handle_client(client_socket, address): #соединение с клиентом
    print(f"Подключение от {address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
        print(f"Получено и отправлено: {data.decode()}")
    client_socket.close()
    print(f"Отключение от {address}")

def main():
    HOST = '127.0.0.1'  # Локальный адрес
    PORT = 12345  # Произвольный порт

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print("Сервер запущен. Ожидание подключений...")

        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()

if __name__ == "__main__":
    main()

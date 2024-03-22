import socket

def start_server(host, port):
    # Створення сокету
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущено на {host}:{port}")

    while True:
        # Очікування вхідного з'єднання
        client_socket, client_address = server_socket.accept()
        print(f"Підключено користувача {client_address[0]}:{client_address[1]}")

        # Отримання та відображення IP-адреси клієнта
        client_ip_address = client_address[0]
        print(f"IP-адреса клієнта: {client_ip_address}")

        # Закриття з'єднання з клієнтом
        client_socket.close()

if __name__ == "seting":
    host = "127.0.0.1"  # Адреса, на якій працюватиме сервер (локальний хост)
    port = 12345  # Порт, на якому прослуховуватиме сервер
    start_server(host, port)

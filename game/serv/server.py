import socket, threading

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', port))
    server.listen()
    print(f"Serveur en écoute sur le port {port}...")
    prompt_cmd = threading.Thread(target=game)
    prompt_cmd.start()
    id=0
    while True:
        client_socket, addr = server.accept()
        print(f"Connexion de {addr}...")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,id))
        client_handler.start()
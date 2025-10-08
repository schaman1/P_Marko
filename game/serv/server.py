import socket, threading
from config import ip as server_ip

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen()
    print(f"Serveur en écoute sur le port {port}...")
    #prompt_cmd = threading.Thread(target=game)
    #prompt_cmd.start()
    id = 0
    while True:
        client_socket, addr = server.accept()
        print(f"Connexion de {addr}...")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,id))
        client_handler.start()

# server.py
import socket, threading

port = 5000
lClient = []

def handle_client(client_socket, id):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Reçu : {data}")

        # Envoyer le message à tous les clients encore connectés
        for client in lClient:
            try:
                client.send(f"{data}".encode())
            except OSError:
                    # Si le socket n'est plus valide, on l'enlève de la liste
                lClient.remove(client)

    client_socket.close()

def start_server(port):
 
    host = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port)) #Lance le serveur
    server.listen()
    print(f"Serveur en écoute sur le port {port}...")

    while True:

        client_socket, addr = server.accept()
        lClient.append(client_socket)

        print(f"Connexion de {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,id))
        client_handler.start()

    server.close()

start_server(port)
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

def start_server(host,port):
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
print("Quel mode de serveur voulez vous lancer ?\n1. Serveur Local\n2. Serveur sur le réseau local\n3. Serveur sur internet (ngrok)")
rep=input("-> ")
if rep=="3":
    port=5000
    ip="localhost"
    os.system("start ngrok tcp 5000")
elif rep=="2":
    ip="0.0.0.0"
    port=int(input("Quel port : "))
else:
    ip="localhost"
    port=int(input("Quel port : "))
clear()
start_server(ip,port)
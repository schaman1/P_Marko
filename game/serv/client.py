import socket, json, threading
from config import ip as server_ip

port = 5000

dic = {}

def reception_server():
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        # Réception de la réponse
        data = json.loads(client.recv(1024).decode())  #reception des datas

        print(f"Réponse du serveur : {data["pseudo"]} ta force : {data["force"]}")


# Création de la socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
#ip = input(f"IP")
port = int(input(f"Port"))
client.connect((server_ip, port))
print("Connecté au serveur")

# Démarrer un thread pour recevoir les messages du serveur
threading.Thread(target=reception_server, daemon=True).start()

# Envoi d'un message
dic["pseudo"] = input("Ton pseudo: ")
dic["force"] = int(input("ta force"))

client.send(json.dumps(dic).encode())
print("Message envoyé")



# Fermer la connexion
client.close()
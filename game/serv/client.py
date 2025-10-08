import socket, json, threading

port = 5000

dic = {}

def reception_server():
    while True:

        data = json.loads(client.recv(1024).decode())  #reception des datas
        
        if not data:
            break
        # Réception de la réponse


        print(f"Réponse du serveur : {data["pseudo"]} ta force : {data["force"]}")


# Création de la socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
ip = input("ip : ")
if ip=="":
    ip="localhost"

port = int(input("Port"))
client.connect((ip, port))
print("Connecté au serveur")

# Démarrer un thread pour recevoir les messages du serveur
threading.Thread(target=reception_server).start()

# Envoi d'un message
while True:
    dic["pseudo"] = input("Ton pseudo: ")
    dic["force"] = int(input("ta force"))

    client.send(json.dumps(dic).encode())
    print("Message envoyé")

# Fermer la connexion
client.close()
import requests
import random
import time
import uuid

# Obtenir l'adresse IP
url = "https://httpbin.org/ip"
try:
    r1 = requests.get(url)
    print("Adresse IP :", r1.json()["origin"])
except Exception as e:
    print(f"Impossible de récupérer l'adresse IP : {e}")
    exit()

# Demander le mode d'envoi
mode = input("Choisissez le mode d'envoi (normal/slow) : ").strip().lower()
if mode not in ["normal", "slow"]:
    print("Mode invalide. Veuillez choisir 'normal' ou 'slow'.")
    exit()

# Définir le délai en fonction du mode
if mode == "normal":
    delay_min, delay_max = 0.2, 1.2
else:
    delay_min, delay_max = 4.0, 5.0

# Demander le nom d'utilisateur
username = input("Entrez le nom d'utilisateur NGL : ")

# Demander le nombre de messages à envoyer
try:
    nombre_de_repetitions = int(input("Combien de messages souhaitez-vous envoyer ? "))
except ValueError:
    print("Veuillez entrer un nombre valide.")
    exit()

# URL de l'API NGL
ngl_url = "https://ngl.link/api/submit"

# Liste des messages possibles
messages = [
    "La cour était presque vide après la pause.",
    "Les fenêtres de la salle de maths sont restées ouvertes.",
    "Les cahiers de français étaient empilés sur le bureau.",
    "Le portail principal a fermé en avance.",
    "Les poubelles étaient pleines après la récré.",
    "La salle des profs était fermée ce matin.",
    "Les lumières du couloir sont restées allumées toute la journée.",
    "Les casiers du premier étage étaient tous fermés.",
    "Les tables du foyer étaient encore sales.",
    "Le tableau du hall avait de nouvelles affiches.",
    "Les ballons de sport étaient encore dehors.",
    "Les portes de l’amphithéâtre étaient ouvertes.",
    "Le CDI n'a pas ouvert cet après-midi.",
    "Les escaliers étaient vides à la fin des cours.",
    "Les bancs sous le préau étaient mouillés.",
    "Les carnets de liaison ont été vérifiés en classe.",
    "Le baby-foot au foyer n’a toujours pas été réparé.",
    "Les couloirs étaient calmes ce matin.",
    "Les ordinateurs de la salle info étaient éteints.",
    "Le club de dessin n’a pas eu lieu aujourd’hui."
]

# Générer le premier device ID
device_id = str(uuid.uuid4())
print("Device ID initial :", device_id)

def envoyer_message(compteur):
    global device_id

    # Changer l'UUID toutes les 5 itérations
    if compteur % 5 == 0:
        device_id = str(uuid.uuid4())
        print(f"NEW Device ID : {device_id}")

    message = random.choice(messages)

    payload = {
        "username": username,
        "question": message,
        "deviceId": device_id,
        "gameSlug": "",
        "referrer": ""
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.post(ngl_url, data=payload, headers=headers)
        if response.status_code == 200:
            print(f"MSG {compteur} Send : {message}")
        elif response.status_code == 429:
            print("Echec de l'envoi : 429 - Trop de requêtes. Pause de 60 secondes.")
            time.sleep(60)
        else:
            print(f"Echec de l'envoi : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur : {e}")

# Envoyer les messages
for i in range(1, nombre_de_repetitions + 1):
    envoyer_message(i)
    time.sleep(random.uniform(delay_min, delay_max))  # Délai ajusté selon le mode choisi

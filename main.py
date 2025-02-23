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
mode = input("Choisissez le mode d'envoi (normal/slow/extra_slow) : ").strip().lower()
if mode not in ["normal", "slow", "extra_slow"]:
    print("Mode invalide. Veuillez choisir 'normal', 'slow' ou 'extra_slow'.")
    exit()

# Définir le délai en fonction du mode
if mode == "normal":
    delay_min, delay_max = 0.2, 1.2
elif mode == "slow":
    delay_min, delay_max = 4.0, 5.0
else:
    delay_min, delay_max = 15.0, 25.0  # Mode extra slow

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
    "La cour était presque vide après la pause… tout le monde a séché ou quoi ? 😂",
    "Les fenêtres de la salle de maths sont restées ouvertes mdrr, qui chauffe la salle pour les pigeons ?",
    "Les cahiers de français étaient empilés sur le bureau… la prof a rage quit ? 🤔",
    "Le portail principal a fermé en avance ptdr, ils voulaient vraiment qu'on reste coincés ?",
    "Les poubelles étaient pleines après la récré… c’est si dur de viser ou quoi ? 💀",
    "La salle des profs était fermée ce matin mdrr. Réunion de crise ou sieste collective ?",
    "Les lumières du couloir sont restées allumées toute la journée… EDF vous remercie 💸.",
    "Les casiers du premier étage étaient tous fermés 😭. Quelqu’un a crié 'contrôle surprise' ou quoi ?",
    "Les tables du foyer étaient encore sales, comme si un goûter apocalypse avait eu lieu 😂.",
    "Le tableau du hall avait de nouvelles affiches… encore un club chelou qui se lance ?"
]

# Générer le premier device ID
device_id = str(uuid.uuid4())
print("Device ID initial :", device_id)

def envoyer_message(compteur):
    global device_id

    # Changer l'UUID à chaque message si mode extra slow
    if mode == "extra_slow":
        device_id = str(uuid.uuid4())
        print(f"NEW Device ID (extra slow) : {device_id}")
    elif compteur % 5 == 0:
        device_id = str(uuid.uuid4())
        print(f"NEW Device ID (normal/slow) : {device_id}")

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

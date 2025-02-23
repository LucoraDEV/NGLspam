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
    "La cour était presque vide après la pause… tout le monde a séché ou quoi ? 😂",
    "Les fenêtres de la salle de maths sont restées ouvertes mdrr, qui chauffe la salle pour les pigeons ?",
    "Les cahiers de français étaient empilés sur le bureau… la prof a rage quit ? 🤔",
    "Le portail principal a fermé en avance ptdr, ils voulaient vraiment qu'on reste coincés ?",
    "Les poubelles étaient pleines après la récré… c’est si dur de viser ou quoi ? 💀",
    "La salle des profs était fermée ce matin mdrr. Réunion de crise ou sieste collective ?",
    "Les lumières du couloir sont restées allumées toute la journée… EDF vous remercie 💸.",
    "Les casiers du premier étage étaient tous fermés 😭. Quelqu’un a crié 'contrôle surprise' ou quoi ?",
    "Les tables du foyer étaient encore sales, comme si un goûter apocalypse avait eu lieu 😂.",
    "Le tableau du hall avait de nouvelles affiches… encore un club chelou qui se lance ?",
    "Les ballons de sport étaient encore dehors mdrr, ils partent faire leur vie sans nous ?",
    "Les portes de l’amphithéâtre étaient ouvertes… répétition secrète ou oubli ? 🤨",
    "Le CDI n'a pas ouvert cet après-midi… la doc a ghosté l'école ? 😂",
    "Les escaliers étaient vides à la fin des cours… tout le monde a sprint pour le bus ? 💀",
    "Les bancs sous le préau étaient mouillés… quelqu'un a pleuré sa vie ou quoi ? 😂",
    "Les carnets de liaison ont été vérifiés en classe… qui a encore pris une heure de colle ? 🤷‍♀️",
    "Le baby-foot au foyer n’a toujours pas été réparé mdrr, c’est un projet sur 10 ans ou quoi ?",
    "Les couloirs étaient calmes ce matin… soit c’est la paix, soit un truc se prépare 😶.",
    "Les ordinateurs de la salle info étaient éteints… hacké par un sixième ou juste la flemme ? 😂",
    "Le club de dessin n’a pas eu lieu aujourd’hui… les artistes sont en grève ? 🎨",
    "Apparemment y’a eu embrouille devant le foyer… quelqu’un a les détails ? 👀",
    "Untel et unetelle se sont encore disputés ptdr, c’est la série Netflix en direct.",
    "Quelqu’un a vu qui est arrivé en retard ce matin ? C’était le défilé mdrr.",
    "La prof de maths a rendu les contrôles… et ça pique fort 💀.",
    "Il paraît que quelqu’un a changé la musique sur l’enceinte du foyer en plein milieu… respect 😂.",
    "Le surveillant a confisqué un téléphone… encore un qui pensait être discret 💀.",
    "Les stores de la salle 204 sont encore bloqués… ça fait ambiance grotte mdrr.",
    "Y’a eu un cri chelou dans le couloir pendant les cours… c’était un prank ou quoi ? 😭",
    "Qui a encore oublié son sac devant le portail ? Il est là depuis ce matin ptdr.",
    "Y’a un prof qui s’est embrouillé avec un élève en plein cours… malaise général 💀.",
    "Quelqu’un a mis un post-it 'en panne' sur la fontaine à eau… c’est du troll pur 😂.",
    "Y’a un pull qui traîne sur un banc depuis hier… c’est à qui, sérieusement ?",
    "Le micro du gymnase grésille encore mdrr, on dirait un vieux talkie-walkie.",
    "La machine à café des profs est encore cassée… ils vont être en PLS aujourd’hui 😂.",
    "Il paraît que le foyer va fermer plus tôt cette semaine… qui a encore abusé ? 💀",
    "Quelqu’un a mis des faux insectes dans la salle de SVT… la prof a hurlé mdrr.",
    "Les trottinettes sont encore alignées comme des dominos devant le portail 😂.",
    "Le self était en rupture de dessert à 12h10… la guerre des premiers servis continue 💪.",
    "Y’a un sixième qui a essayé de rentrer en cours de troisième comme si de rien n’était mdrr.",
    "La prof principale a fait un speech de 10 min… pour dire qu’il fallait ranger son casier 💀."
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

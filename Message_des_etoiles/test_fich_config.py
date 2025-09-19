import configparser
import os

print("------ Test config ------")

config=configparser.ConfigParser()
print(config.sections())

chemin_courant=os.getcwd()
print(f"chemin courant = {chemin_courant}")
chemin_fichier=chemin_courant+'\\fich_config.ini'
print(f"chemin+fichier : {chemin_fichier}")
config.read(chemin_fichier)
print(config.sections())

print(type(config))
for key in config:
    print(key)

print(config['chemin_acces']['chem_mess_etoiles'])

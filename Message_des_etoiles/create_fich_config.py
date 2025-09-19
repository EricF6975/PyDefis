#----- Creation fichier de config ----
import configparser

print(" ---------  Creation de fichier de config ------------")
config=configparser.ConfigParser()
config['DEFAULT']={'Test':'yes'}
config['chemin_acces']={'chem_mess_etoiles':'C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_des_etoiles\\'}

with open('C:\\Users\\EFEUERSTEIN\Documents\\Formations\\Python\\pyDefi\\Message_des_étoiles\\fich_config.ini','w') as configfile:
    config.write(configfile)
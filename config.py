import pickle
from time import sleep
import hashlib

#Diccionari model d'usuari
user = {
    "username": "",
    "passwd": "",
    "move_folders": []
    
}

#Diccionaris para el organitzador d'archius
move_folders_origin = {

        "origin_folder": ""
}

move_folders_destination = {

        "destination_folder": ""
}

#Funcio per a crear usuaris 
def create_user():
    
    #Es copia el diccionari model per a poder tenir mes de un usuari
    new_user = user.copy()
    
    print("----- CONFIGURACIO DE USUARI -----")

    print("Usuari: {}".format(new_user["username"]))

    

    sleep(2)
    new_user["username"] = input("Nom de l'usuari: ")

    sleep(2)
    new_user["passwd"] = encryption_hash()

    

def encryption_hash():

    #es pregunta la contrasenya 
    passwd = input("Contrasenya: ")
    
    #variable amb el tipus de hash
    hash_code = hashlib.sha256()
    
    #confirmem que la contrasenya s'ha escrit de forma correcta
    passwd = str(passwd).encode("utf-8")
    
    #creem el hash de la contrasenya
    hash_code.update(passwd)
    
    #posem el hash com a hexadecimal i el retornem
    result = hash_code.hexdigest()
    return result





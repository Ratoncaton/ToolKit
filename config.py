import pickle
from time import sleep
import hashlib
import os
from pathlib import Path
from tkinter import filedialog

#DICCIONARIS DE CONFIGURACIO DE USUARIS

#Diccionari model d'usuari
user = {
    "username": "",
    "passwd": "",
    "orign_move_folders": [],
    "destination_move_folders": []
    
}

#Diccionaris para el organitzador d'archius
move_folders_origin = {

        "origin_folder": ""
}

move_folders_destination = {

        "destination_folder": ""
}

######################################################################

#INTERFICIE EN TERMINAL | VISTA DE L'USUARI

#funcio per netejar la terminal independentment del SO
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#funcio per al titol
def creation_title(new_user):
    print("----- CONFIGURACIO DE USUARI -----")

    print("Usuari: {}".format(new_user["username"]))

    print("----------------------------------")
    print()

#Funcio per a crear usuaris 
def create_user():
    
    #Es copia el diccionari model per a poder tenir mes de un usuari
    new_user = user.copy()

    creation_title(new_user)

    sleep(2)
    new_user["username"] = input("Nom de l'usuari: ")
    clear()

    creation_title(new_user)

    sleep(2)
    new_user["passwd"] = encryption_hash()
    clear()

    create_origin_folder(new_user) if input("Vols crear ara una carpeta d'origen? (S/N) ").lower() == "s" else print()
    create_destination_folder(new_user) if input("Vols crear ara una carpeta de destinació? (S/N) ").lower() == "s"  else print()

####################################################################

#LOGICA DE CONFIGURACIO

#Funcio de encriptacio hash per a guardar i verificar les contrasenyes de forma segura
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

def create_origin_folder(new_user):
    
    #Crea una copia del diccionari model per a les carpetes d'origen
    new_origin_folder = move_folders_origin.copy()
    
    #Agafa la ruta absoluta de forma grafica 
    directory_path = filedialog.askdirectory()

    new_origin_folder["origin_folder"] = directory_path

    #Afegim a la llista 
    new_user["orign_move_folders"].append(new_origin_folder)


def create_destination_folder(new_user):
    new_destination_folder = move_folders_destination.copy()

    directory_path = filedialog.askdirectory()

    new_destination_folder["destination_folder"] = directory_path

    new_user["destination_move_folders"].append(new_destination_folder)


if __name__ == "__main__":
    create_user()
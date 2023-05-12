import pickle
from time import sleep
import hashlib
import os
from pathlib import Path
from tkinter import filedialog
import readchar

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

    "name_folder": "",
    "origin_folder": ""
}

move_folders_destination = {

    "name_folder": "",
    "destination_folder": "",
    "type_of_file": []
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

    print(new_user)

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

    #Preguntem el nom per a poder tindre un identificador
    new_origin_folder["name_folder"] = input("Introdueix el nom de la carpeta: ")
    
    #Afegim a la llista 
    new_user["orign_move_folders"].append(new_origin_folder)


def append_files_destination_folder(file_list, new_destination_folder):
    for file in file_list:
        new_destination_folder["type_of_file"].append(file)


def type_of_file(new_destination_folder):
    print(""""Tria un tipus de fitxer o crea un nou
    1. PDF
    2. Imatges (JPG,JPEG, PNG)
    3. Archius comprimits (RAR, ZIP, 7Z, TAR.GZ)
    4. Executables (EXE)
    5. Personalitzat""")

    option_choosed = readchar.readchar().decode()

    if option_choosed == "1":
        new_destination_folder["type_of_file"].append(".pdf") 
    
    elif option_choosed == "2":
        file_list = [".jpg", ".jpeg", ".png"]
        append_files_destination_folder(file_list, new_destination_folder)

    elif option_choosed == "3":
        file_list = [".rar", ".zip", ".7z", ".tar.gz"]
        append_files_destination_folder(file_list, new_destination_folder)

    elif option_choosed == "4":
        new_destination_folder["type_of_file"].append(".exe")
    
    elif option_choosed == "5":
        
        file_list = []
        user_input = input("Introdueix la extensio: ")
        file_list.append(".{}".format(user_input))
        
        while user_input != "q":

            user_input = input("Introdueix la extensio (q per sortir) : ")
            file_list.append(".{}".format(user_input))

        




def create_destination_folder(new_user):
    new_destination_folder = move_folders_destination.copy()

    #new_destination_folder["type_of_file"].append(type_of_file(new_destination_folder))

    directory_path = filedialog.askdirectory()

    new_destination_folder["destination_folder"] = directory_path

    new_user["destination_move_folders"].append(new_destination_folder)


if __name__ == "__main__":
    create_user()
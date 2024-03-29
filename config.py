#Made By Walid El Ourfi El Orfi | 25/05/2023 | 1 SMX MP14 Python

import pickle
from time import sleep
import hashlib
import os
from pathlib import Path
from tkinter import filedialog
import readchar

#DICCIONARIS DE CONFIGURACIO DE USUARIS

users = []

#Diccionari model d'usuari
user_structure = {
    "username": "",
    "passwd": "",
    "auto_login": False,
    "origin_move_folders": [],
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
    
    clear()
    
    print("----- CONFIGURACIO DE USUARI -----")

    print("Usuari: {}".format(new_user["username"]))

    print("----------------------------------")
    print()

#Funcio per a crear usuaris 
def create_user():
    
    finnish = False
    while not finnish:
    #Es copia el diccionari model per a poder tenir mes de un usuari
        new_user = user_structure.copy()

        #variable per a mes endavant
        username_confirmation = False

        while not username_confirmation:
            clear()
            creation_title(new_user)

            sleep(1)
            new_user["username"] = input("Nom de l'usuari: ")

            #Si es el primer usuari no es necessari confirmar res
            if len(users) == 0:
                username_confirmation = True

            else:
                for user in users:
                    #Si el username del usuari es igual que el de un altre, pot causar confusions, per tants surt un error
                    if user["username"] == new_user["username"]:

                        new_user["username"] = ""

                        print("       ¡ ERROR !")
                        print("Aquest usuari ja existeix")
                        sleep(2)
                    
                    else:
                        username_confirmation = True
                
        clear()

        creation_title(new_user)

        sleep(1)
        new_user["passwd"] = encryption_hash()
        
        clear()
        print("---- CONFIGURACIO DIRECTORIS ----")
        print()
        if input("Vols crear ara una carpeta d'origen? (S/N) ").lower() == "s":
            
            creation_origin_folder_finnish = False

            while not creation_origin_folder_finnish:
                create_origin_folder(new_user)
                creation_origin_folder_finnish = True if input("Introduir una altra carpeta d'origen? (S/N) ").lower() == "n" else print(end="")

        if input("Vols crear ara una carpeta de destinacio? (S/N) ").lower() == "s":
            
            creation_destination_folder_finnish = False
            
            while not creation_destination_folder_finnish:
                create_destination_folder(new_user)
                creation_destination_folder_finnish = True if input("Introduir una altra carpeta de destinacio? (S/N) ").lower() == "n" else print(end="")
        
        clear()
        new_user["auto_login"] = True if input("Inicia sessio sense posar la contrasenya? (S/N) ").lower() == "s" else print(end="")

        users.append(new_user)

        finnish = True if input("Vols introduir un altre usuari? (S/N)  ").lower() == "n" else print(end="")
    
    #Es crea el fitxers amb els usuaris en format binari, a part es retorna la llista d'usuaris per a poder iniciar sessió directament
    with open ("config.txt", "wb") as config:
        pickle.dump(users , config)
        return users

    

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

#Funcio per extraure usuaris de l'arxiu JSON
def extract_users():
    try:
        
        with open("config.txt", "rb") as config:
            return pickle.load(config)
    
    except FileNotFoundError:
        
        print("No existeixen usuaris...")
        sleep(1)
        print("Dirigint-te a la configuracio de usuaris")
        sleep(1)
        return create_user()

#Crea una carpeta d'origen, des d'aquesta carpeta shutil revisara i moura carpetes
def create_origin_folder(new_user):
    clear()
    print(""" 
-- CONFIGURACIO CARPETA DE ORIGEN --
    """)

    #Crea una copia del diccionari model per a les carpetes d'origen
    new_origin_folder = move_folders_origin.copy()
    
    #Agafa la ruta absoluta de forma grafica 
    directory_path = filedialog.askdirectory()

    new_origin_folder["origin_folder"] = directory_path

    #Preguntem el nom per a poder tindre un identificador
    new_origin_folder["name_folder"] = input("Introdueix el nom de la carpeta: ")
    
    #Afegim a la llista 
    new_user["origin_move_folders"].append(new_origin_folder)


#Facilita escritura per afegir tipus d'arxius
def append_files_destination_folder(file_list, new_destination_folder):
    for file in file_list:
        new_destination_folder["type_of_file"].append(file)

#Tipus d'arxius que s'agafaran 
def type_of_file(new_destination_folder):
    
    #titol

    clear()
    print("""
--- CONFIGURACIO TIPUS DE FITXER ---
    
Tria un tipus de fitxer o crea un nou
1. PDF
2. Imatges (JPG,JPEG, PNG)
3. Archius comprimits (RAR, ZIP, 7Z, TAR.GZ)
4. Executables (EXE)
5. Personalitzat
6. Sortir

---------------------------------------""")

    #escollir opcio de manera automatica (com el choice de batch)
    option_choosed = readchar.readchar()

    if option_choosed == "1":
        new_destination_folder["type_of_file"].append(".pdf")
        
        print("S'ha introduit la carpeta de destinacio per a PDF correctament")
        input("Prem enter per a continuar: ")
        sleep(1)
    
    elif option_choosed == "2":
        file_list = [".jpg", ".jpeg", ".png"]
        #funcio per afegir a l'apartat type of file
        append_files_destination_folder(file_list, new_destination_folder)
        
        print("S'ha introduit la carpeta de destinacio per a imatges correctament")
        input("Prem enter per a continuar: ")
        sleep(1)

    elif option_choosed == "3":
        file_list = [".rar", ".zip", ".7z", ".tar.gz"]
        append_files_destination_folder(file_list, new_destination_folder)
        
        print("S'ha introduit la carpeta de destinacio per a archius comprimits correctament")
        input("Prem enter per a continuar: ")
        sleep(1)

    elif option_choosed == "4":
        new_destination_folder["type_of_file"].append(".exe")
        
        print("S'ha introduit la carpeta de destinacio per a executables correctament")
        input("Prem enter per a continuar: ")
        sleep(1)
    
    elif option_choosed == "5":
        
        file_list = []
        user_input = input("Introdueix la extensio: ")
        file_list.append(".{}".format(user_input))
        
        print("S'ha introduit la carpeta de destinacio correctament")
        input("Prem enter per a continuar: ")
        sleep(1)
        
        while user_input != "q":

            user_input = input("Introdueix la extensio (q per sortir) : ")
            file_list.append(".{}".format(user_input))
    
    elif option_choosed == "6":
        #al retornar true, el bucle s'acaba
        return True

    else:
        clear()
        #Missatge de error
        print("""
                ¡ERROR!
Has introduit un parametre incorrectament""")
              
        sleep(2)

#Crea la carpeta de desti
def create_destination_folder(new_user):

    clear()
    print(""" 
-- CONFIGURACIO CARPETA DE ORIGEN --
    """)

    new_destination_folder = move_folders_destination.copy()

    #new_destination_folder["type_of_file"].append(type_of_file(new_destination_folder))

    directory_path = filedialog.askdirectory()

    new_destination_folder["destination_folder"] = directory_path

    new_destination_folder["name_folder"] = input("Introdueix el nom de la carpeta: ")

    new_user["destination_move_folders"].append(new_destination_folder)

    finnish = False
    while not finnish:
        finnish = type_of_file(new_destination_folder)


if __name__ == "__main__":
    create_user()


import shutil
import readchar
import config
from time import sleep
import os
import pyshorteners
import subprocess
import secrets
import string
import boveda

def choose_actual_user(users):
    
    finnish = False
    while not finnish:
        #Titol
        config.clear()

        print(""" 
---------- Inici Sessio ----------
------------ usuaris -------------
        """)

        #D'aquesta forma es mostren els noms dels usuaris registrats
        for user in range(len(users)):
            print("{}.{} |".format(user, users[user]["username"]), end=" ")
            
        print("\n")
        print("----------------------------------")

        user_choosen = readchar.readchar().lower()    
        
        #Si ha escrit una tecla incorrecta surtirà un missatge d'error
        try:
            actual_user  = users[int(user_choosen)]
            finnish = True
            
        except:
            print("""
            ¡ ERROR !
Has introduit un usuari inexistent""")
            sleep(2)

    config.clear()

    #Titol amb el nom d'usuari
    print(""" 
---------- Inici Sessio ----------
------------ {} -------------
    """.format(actual_user["username"]))
        
    #Es crea la variable de contrasenya per a no donar errors mes endavant amb l'inici automatic
    password_actual_user = ""
        
    #Si te l'inici automatic es passa directament al menu
    if actual_user["auto_login"] == True:
        pass
        
    else:
        
        #S'encripta la contrasenya per a poder comparar
        password_actual_user = config.encryption_hash()

    #Es compara la contrasenya, tambe si l'usuari a posat que s'inicii sessió automaticament s'entra directe
    if password_actual_user == actual_user["passwd"] or actual_user["auto_login"] == True:
        config.clear()
        return actual_user
    
    else:
        
        config.clear()
        print("Contrasenya incorrecta")
        sleep(1)


#Moure fitxers
def move_files(actual_user):
    
    #S'agafa un directori de la llista de directoris d'origen
    for origin_folder in actual_user["origin_move_folders"]:

        #Es llista el directori per saber els fitxers existents
        for file in os.listdir(origin_folder["origin_folder"]):
            
            #S'escolleix un directori desti de la llista
            for destination_folder in actual_user["destination_move_folders"]:
                
                #S'escolleix un tipus d'arxiu
                for file_end in destination_folder["type_of_file"]:
                    
                    #Si l'arxiu escollit del directori origen es del mateix tipus que el de desti, es moura l'arxiu
                    if file.endswith(file_end):
                        
                        #Es crea la variable per amb tota la direcció de l'arxiu
                        path_file = os.path.join(origin_folder["origin_folder"], file)

                        #Es mou l'arxiu
                        shutil.move(path_file, destination_folder["destination_folder"])


def link_shorter():
    
    config.clear()
    #S'introdueix el link 
    link = input("Introdueix el link: ")
    
    #Comanda acortada per facilitar lectura
    shortener = pyshorteners.Shortener()

    #Acortador del link
    #Si s'intenta ficar un link ja acortat salta l'error pertinent
    try:
        link_shorted = shortener.tinyurl.short(link)
    

        user_choice = input("Vols mostrar el link en pantalla (1) o guardar-lo en un archiu .txt (2)? \n")
            
        finnish = False
        while not finnish:
            if user_choice == "1":
                    
                config.clear()
                    
                    #Es mostra el link per pantalla
                print(link_shorted)
                print()

                input("Prem ENTER per a continuar... ")
                finnish = True
                
            elif user_choice == "2":

                    #Es guarda el link en un archiu .txt en la carpeta
                with open ("links_shorted.txt", "a") as file:
                    file.write("\n{} = {}".format(link, link_shorted))
                    
                finnish = True
                
            else:
                    #Missatge d'error
                print("            ¡ ERROR ! ")
                print("Has escollit un parametre inexistent")

    except pyshorteners.exceptions.ShorteningErrorException:
        print("                  ¡ ERROR !")
        print("Es veu que has intentant acortar un link ja acortat...")
        sleep(2)

def cache_cleaner():
    
    #Si el SO es Windows
    if os.name == 'nt':
        try:
            #Comanda per rentar la cache
            subprocess.run("cleanmgr /sagerun:1", shell=True)

            print("Cache netejada correctament")
            print()
            input("Prem ENTER per continuar... ")

        except Exception as error:
            #Missatge d'error amb l'error corresponent
            print("Error: {error}")
            sleep(3)
    
    #Si no es Windows, es Linux. Mac no existeix
    else:
        try:

            #Comanda per rentar la cache
            subprocess.run("sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches", shell=True)
            
            print("Cache netejada correctament")
            print()
            input("Prem ENTER per continuar... ")
        
        except Exception as error:
            print("Error: {error}")
    


def passwd_gen():
    
    #Variable per saber quin tipus de contrasenyes ficar
    alphabet = ""

    finnish = False
    while not finnish:
        
        config.clear()

        print("------ GENERADOR DE CONTRASENYES ------")
        
        try:
            passwd_length = int(input("\nLongitud de la contrasenya: "))
            finnish = True
        
        #Per si l'usuari introdueix algo que no es un numero
        except ValueError:
            print()
            print("          ¡ ERROR !")
            print("No has introduit un nombre valid")
            sleep(2)

    if input("Majuscules (S/N): ").lower() == "s":
        alphabet += string.ascii_uppercase
    
    if input("Minuscules (S/N): ").lower() == "s":
        alphabet += string.ascii_lowercase

    if input("Digits (S/N): ").lower() == "s":
        alphabet += string.digits

    if input("Caracters especials (S/N): ").lower() == "s":
        alphabet += string.punctuation

    #Si hi ha algun tipus de caracter es pot crear la contrasenya
    if alphabet != "":

        password = ""
        
        for character in range(passwd_length):
            password += "".join(secrets.choice(alphabet))
        
        config.clear()

        print("------ GENERADOR DE CONTRASENYES ------")

        print("\nContrasenya: {}".format(password))

        if input("Vols guardar la contrasenyar? (S/N): ").lower() == "s":
            boveda.password_generated_data(password)
    
    #Si no ha ficat ningun tipus de caracter, no es pot crear la contrasenya
    else:
        print()
        print("                         ¡ ERROR !")
        print("No es pot crear ninguna contrasenya cap tipus de caracters")
        sleep(2)


def password_trunk(actual_user):
    finnish = False
    
    while not finnish:
        config.clear()

        print("""
------ LA BOVEDA ------ 
1. Afegir contrasenyes
2. Consultar contrasenyes
3. Sortir al menu principal""")

        user_choice = readchar.readchar()

        if user_choice == "1":
            
            password_actual_user = config.encryption_hash()
            
            if password_actual_user ==  actual_user["passwd"]:
                boveda.generate_data()     

            else:
                print("Contrasenya incorrecta")
                sleep(2)
        
        elif user_choice == "2":
            password_actual_user = config.encryption_hash()
            
            if password_actual_user ==  actual_user["passwd"]:
                boveda.boveda_main(True)     

            else:
                print("Contrasenya incorrecta")
                sleep(2)
        
        elif user_choice == "3":
            finnish = True
        
        else:
            print("            ¡ ERROR !")
            print("Has introduit un parametre inexistent")


def menu(actual_user):
    
    finnish = False
    while not finnish:
        config.clear()

        print(""" 
      $$$$$$$$\                  $$\ $$\   $$\ $$\   $$\     
      \__$$  __|                 $$ |$$ | $$  |\__|  $$ |    
         $$ | $$$$$$\   $$$$$$\  $$ |$$ |$$  / $$\ $$$$$$\   
         $$ |$$  __$$\ $$  __$$\ $$ |$$$$$  /  $$ |\_$$  _|  
         $$ |$$ /  $$ |$$ /  $$ |$$ |$$  $$<   $$ |  $$ |    
         $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |\$$\  $$ |  $$ |$$\ 
         $$ |\$$$$$$  |\$$$$$$  |$$ |$$ | \$$\ $$ |  \$$$$  |
         \__| \______/  \______/ \__|\__|  \__|\__|   \____/ 

------------------------------------------------------------------

Usuari: {} 

------------------------------------------------------------------

1. Ordenar Fitxers
2. Acortador de links
3. Netejar Cache
4. Generador de contrasenyes
5. La boveda
6. Canviar usuari
7. Tancar programa
    """.format(actual_user["username"]))

        user_choice = readchar.readchar()

        if user_choice == "1":
            
            move_files(actual_user)
        
        elif user_choice == "2":
        
            link_shorter()
        
        elif user_choice == "3":
            
            cache_cleaner()
    
        elif user_choice == "4":

            pass
            passwd_gen()
        
        elif user_choice == "5":
            
            password_trunk(actual_user)

        elif user_choice == "6":

            finnish = True

        elif user_choice == "7":
            finnish = True
            return True


def main():
    finnish = False
    print("Extraent usuaris...")
    sleep(2)
    #S'extrauen els usuaris del arxiu config.txt, si aquest no existeix, significa que no existeixen usuaris i es va directament a la creació d'aquests
    users = config.extract_users()
    
    while not finnish:
        #Seguidament s'inicia sessió amb l'usuari i contrasenya ja establegudes
        actual_user = choose_actual_user(users)
        
        #Finalment, s'envia al menu on podran triar les diferentes opcions
        finnish = menu(actual_user)

if __name__ == "__main__":
    main()
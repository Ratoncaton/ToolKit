import shutil
import readchar
import config
from time import sleep
import os


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



def menu(actual_user):
    finnish = False
    while not finnish:
        print("""" 
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
5. Guardar contrasenyes
6. Canviar usuari
7. Tancar programa
    """.format(actual_user["username"]))

        user_choice = readchar.readchar()

        if user_choice == "1":
            
            pass
            move_files(actual_user)
        
        elif user_choice == "2":
            
            pass
            #link_shorter()
        
        elif user_choice == "3":
            
            pass
            #cache_cleaner()
    
        elif user_choice == "4":

            pass
            #passwd_gen()
        
        elif user_choice == "5":

            pass
            #password_trunk()

        elif user_choice == "6":

            pass

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
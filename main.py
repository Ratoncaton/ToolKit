import shutil
import readchar
import config
from time import sleep


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
        print("[A] - Afegir usuaris")
        print("----------------------------------")
        print("\nQui ets? (Prem el numero d'usuari)\n")

        user_choosen = readchar.readchar().lower()    
        
        if user_choosen == "a":
            
            config.add_user()
            main()
            actual_user = users[-1]
            finnish = True
        
        else:
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


def organize_files():
    pass


def menu(actual_user):
    finnish = False
    while not finnish:
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
5. Guardar contrasenyes
6. Tancar sessio
7. Canviar sessio
8. Tancar programa
    """.format(actual_user["username"]))

        user_choosen = readchar.readchar()

        if user_choosen == "1":
            pass
            finnish = True
            #organize_files()
        
        elif user_choosen == "2":
            pass
            finnish = True
            #link_shorter()
        
        elif user_choosen == "3":
            pass
            finnish = True
            #cache_cleaner
        
        elif user_choosen == "4":
            pass
            finnish = True
            #password_gen()
        
        elif user_choosen == "5":
            pass
            finnish = True
            #password_trunk()
        
        elif user_choosen == "6":
            actual_user = choose_actual_user()
        
        elif user_choosen == "7":
            actual_user = choose_actual_user()
        
        elif user_choosen == "8":
            print("Fet per Walid El Ourfi | 1 SMX B | Projecte MP14 2023")
            finnish = True
        else:
            config.clear()
            print("""
            ¡ ERROR !
Has introduit una opcio inexistent""")
            sleep(2)


def main():
    
    print("Extraent els usuaris...")
    sleep(1)
    #S'extrau els usuaris, si es la primera vegada obrint el programa, s'anira directament al dialeg de configuracio
    users = config.extract_users()

    #Iniciar sessio dels usuaris
    actual_user = choose_actual_user(users)

    menu(actual_user)

if __name__ == "__main__":
    main()

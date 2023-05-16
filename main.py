import shutil
import readchar
import config
from time import sleep

actual_user = {}

users = config.extract_users()
#print(users)

def choose_actual_user():
    
    config.clear()

    print(""" 
---------- Inici Sessio ----------
------------ usuaris -------------
    """)


    for user in range(len(users)):
        print("{}.{} |".format(user, users[user]["username"]), end=" ")
    
    print("\n")
    print("----------------------------------")
    print("\nQui ets? (Prem el numero d'usuari)\n")
    
    user_choosen = readchar.readchar()

    actual_user  = users[int(user_choosen)]
    
    password_actual_user = config.encryption_hash()

    if password_actual_user == actual_user["passwd"]:
        config.clear()
        menu()
    else:
        config.clear()
        print("Contrasenya incorrecta")
        sleep(1)

        choose_actual_user()


choose_actual_user()

def menu():
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
    """.format(actual_user["username"]))



import json
import shutil
import readchar
import config

actual_user = {}

users = config.extract_users()
print(users)

def choose_actual_user():
    print("Quin usuari vols triar?")
    print("")

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



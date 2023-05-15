import json
import shutil
import readchar
import config


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

1. Ordenar Fitxers
2. Acortador de links
3. Netejar Cache
4. Generador de contrasenyes
5. Guardar contrasenyes
    """)

from cryptography.fernet import Fernet
import config
import json
import pickle
import os
from time import sleep


data = {
    "website":"",
    "username": "",
    "password": ""
}

boveda = []

#Clau de la encriptacio
def generate_key():

    #Si no existeix la clau, la crea i la guarda en un archiu en binari per a mes tard
    if not os.path.exists("key.txt"):

        key = Fernet.generate_key()

        with open("key.txt", "wb") as file:
            pickle.dump(key, file)
        
        return key
    
    #Sino simplement lagafa
    else:

        with open("key.txt", "rb") as file:
            
            return  pickle.load(file)

#Per a quan solament vol introduir contrasenyes a la boveda desde el menu principal
def generate_data():
    
    finnish = False

    while not finnish:
        
        config.clear()

        new_data = data.copy()
        
        print("------ LA BOVEDA ------ ")
        print()

        new_data["website"] = input("Plataforma: ")

        new_data["username"] = input("Nom d'usuari: ")

        new_data["password"] = input("Contrasenya: ")

        boveda.append(new_data)

        finnish = True if input("Introduir mes contrasenyes? (S/N): ").lower() == "n" else print(end="")
    
    boveda_main(False)

#Per a quan vol guardar la contrasenya desde el generador
def password_generated_data(password):

    new_data = data.copy()
    
    config.clear()

    print("------ LA BOVEDA ------")
    print()

    new_data["website"] = input("Plataforma: ")

    new_data["username"] = input("Nom d'usuari: ")

    new_data["password"] = password

    boveda.append(new_data)

    #Per si vol introduir mes contrasenyes
    if input("Introduir mes contrasenyes? (S/N): ").lower() == "s":   
        generate_data()

    else:
        boveda_main(False)


def encrypt(cipher_suite):
    
    #Com l'encriptador no deixa guardar llistes, el convertim en un json
    boveda_json = json.dumps(boveda)

    #Encriptem i codifiquem (per a que pugui encriptar sense errors) el json
    encrypted_data = cipher_suite.encrypt(boveda_json.encode("utf-8"))

    #Guardem les dades en un archiu binari, que apart esta encriptat
    with open("data.bin", "wb") as file:

        file.write(encrypted_data)

def desencrypt(cipher_suite):
    try:
        #Obre l'archiu encriptat
        with open("data.bin", "rb") as file:
                
            encrypted_data = file.read()

            #El desencripta amb la clau
            no_encrypted_data = cipher_suite.decrypt(encrypted_data)

            #el guarda en la variable data
            data = json.loads(no_encrypted_data.decode("utf-8"))

        return data
    
    #per si has intentat veure contrasenyes quan no tens l'archiu encriptat
    except FileNotFoundError:
        print("              ¡ ERROR !")
        print("No tens ninguna contrasenya guardada")
        sleep(2)
        

#Mostra les contrasenyes
def show_passwords(data):
    
    config.clear()

    print("------ LA BOVEDA ------")
    
    try:
        for a in data:
            
            print()
            print("Plataforma: {}".format(a["website"]))
            print("Usuari: {}".format(a["username"]))
            print("Contrasenya: {}".format(a["password"]))
            print("\n--------------------------------")
        
        input("Prem ENTER per continuar... ")
    
    except TypeError:
        pass


def boveda_main(show):

    #Es genera la clau si no existeix i es guarda, o l'agafa del arxiu i el guarda
    cipher_suite = Fernet(generate_key())
    
    #si no existeix l'arxiu data.bin, significa que s'ha de crear i que mai a guardat contrasenyes
    if not os.path.exists("data.bin"):

        #si la variable show no esta activada, significa que vol guardar contrasenyes
        if not show:
            encrypt(cipher_suite)
        
        #Sino es que els vol veure
        else:
            show_passwords(desencrypt(cipher_suite))
    
    #Si existeix
    else:
        if not show:
            #Primer es desencripta l'arxiu, es fica a la variable boveda i es torna a encriptar, d'esta forma no es perd la informacio anterior a la nova encriptacio
            boveda.append(desencrypt(cipher_suite))
            encrypt(cipher_suite)
        
        else:
            show_passwords(desencrypt(cipher_suite))
            input("Prem ENTER per continuar... ")

if __name__ == "__main__":


    boveda_main(True)



import hashlib

def encriptar_hash(variable):
    # Crea un objeto hash
    hash_object = hashlib.sha256()

    # Convierte la variable a una cadena antes de encriptar
    variable_str = str(variable).encode('utf-8')

    # Actualiza el objeto hash con la variable en forma de cadena
    hash_object.update(variable_str)

    # Obtiene el hash en formato hexadecimal
    hash_result = hash_object.hexdigest()

    # Devuelve el hash
    return hash_result

# Ejemplo de uso
variable = input("Introduce el ash: ")
hash_variable = encriptar_hash(variable)
print(hash_variable)
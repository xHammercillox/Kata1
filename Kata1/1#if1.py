"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y
minusculas.
"""

password = "contraseña"

password_del_usuario = input("Introduzca la contraseña: ")

password_del_usuario = password_del_usuario.lower() # Convierte la cadena en minuscula y la guarda

if password == password_del_usuario:
    print("La contraseña es correcta")
else:
    print("La contraseña no coincide")
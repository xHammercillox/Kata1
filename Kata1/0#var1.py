"""
Una panaderia vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%.

Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Desputés tu
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser
fresca y el coste total.
"""

precio = 3.49
descuento = 1 - 0.6
precio_con_descuento = precio * descuento

"Leemos el valor"
numero_de_barras = input("Introduce el numero de barras vendidas: ")
"Convertimos el valor introducido a int"
numero_de_barras = int(numero_de_barras)

print("Precio habitual: " +str(precio))
print("Descuento: " +str(precio_con_descuento))
print("Coste final: " +str(numero_de_barras * precio_con_descuento))
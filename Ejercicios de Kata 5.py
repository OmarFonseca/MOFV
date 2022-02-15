#Ejercicio 1

#Se definen variables
tierra = int('149597870')
jupiter = int('778547200')
millas = float('0.621')

distancia_km = (tierra - jupiter)
print('La distancia en kilometros entre la Tierra y Jupiter es de: ' , abs(distancia_km))

distancia_millas = distancia_km*millas

valorAbsoluto = abs(distancia_millas)

print(round(valorAbsoluto))

#############################################################################
print("--------------------------------------------------------------------")
#############################################################################

#Ejercicio 2

#Se piden datos por teclado al usuario y se guardan en una variable
print('Ingrese la distancia en kilometros del sol al primer planeta')
planeta1 = input()

print('Ingrese la distancia en kilometros del sol al primer planeta')
planeta2 = input()

#Se realiza la conversion de string a int
planeta1 = int(planeta1)
planeta2 = int(planeta2)

#Se realiza operación
distanciaKm = planeta2 - planeta1
print(distancia_km)

#Se convierten kilometros a millas
distanciaMillas = distanciaKm * millas
print(abs(distanciaMillas))

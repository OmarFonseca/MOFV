#Ejercicio 1

#Declaración de variables
new_planet = ''
planets = []

print('Ingrese el nombre de un planeta para comenzar la lista \nEscriba "done" si ya no desea escribir otro planeta')
#Se crea ciclo while el cual se seguira ejecutando mientras el usurio no escriba la palabra "done"
while new_planet.lower() != 'done':
    #Por medio de un if se comprueba si el usuario ingreso un planeta
    if new_planet:
        planets.append(new_planet)
        #Se imprime el planeta y se pide un nuevo valor
    new_planet = input('Planea: ')
print('Lista terminada\n')

#Ejercicio 2

#Se crea un cliclo for para imprimir los planetas ingresados en la lista anterior
for planet in planets:
    print('Los planetas ingresados son: ' + planet + "\U0001F600")
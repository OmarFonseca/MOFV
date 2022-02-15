#Ejercicio 1

#Se crea la lista
planets = ['MERCURIO', 'VENUS', 'TIERRA', 'MARTE', 'JUPITER', 'SATURNO', 'URANO']

#Se realiza un conteo en la lista
print('Número de planetas: ',len(planets))

#Se agrega pluton a la lista y se muestra
planets.append('PLUTON')
print(planets[-1], 'es el ultimo planeta')

#############################################################################
print("--------------------------------------------------------------------")
#############################################################################

#Ejercicio 2

#Se crea la lista
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Pluton']

#Se pide planeta por teclado
guardarPlaneta = input('Por favor, ingrese el nombre de un planeta (La primer letra del planeta debe ser MAYUSCULA y las demás minusculas): ')

#Se busca planeta
buscarPlaneta = planets.index(guardarPlaneta)

#Se muestran los dos planetas mas cercanos al sol, dependiendo del planeta ingresado
print('Planetas más cercanos al SOL: ' + guardarPlaneta)
print(planets[0:buscarPlaneta])

#Se muestran los dos planetas mas lejanos al sol, dependiendo del planeta ingresado
print('Planetas más lejanos al SOL: ' + guardarPlaneta)
print(planets[buscarPlaneta + 1:])

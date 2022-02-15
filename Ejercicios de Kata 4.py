print('Ejercicio 1 \n')

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Se separa el texto por oraciones
partes = text.split('. ')
partes

#Se definen palabras claves 
palabrasClave = ['average', 'temperature', 'distance']

#Se realiza ciclo for para recorrec la cadena
for cliclo in partes:
    for palabrasClave in palabrasClave:
        if palabrasClave in cliclo:
            print(cliclo)
            break   

#Se realiza ciclo para recorrer el texto y C por Celsius
for cliclo in partes:
    for palabrasClave in palabrasClave:
        if palabrasClave in cliclo:
            print(cliclo.replace('C', ('Celsius')))
            break 


print('-----------------------------------------------------------------')
print('*****************************************************************')
print('-----------------------------------------------------------------')

print('Ejercicio 2 \n')

#Se definen variables
nombre = "Luna"
gravity   = 0.00143
planet = "Tierra"

#Se crea titulo
titulo = f"La gravedad de {nombre}"

#Se crea plantilla
plantilla = f"""\n"{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {nombre}: {gravity * 1000} m/s2 
"""

#Se une titulo y plantilla
cadena = f"""{titulo.title()} 
{plantilla} 
""" 
print(titulo+plantilla)







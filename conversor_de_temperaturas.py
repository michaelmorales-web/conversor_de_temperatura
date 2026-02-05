#Programa para convertir los grados celcius en grados kelvin, fahrenheit

#input
C = input("digite los grados celcius: ")
C = int(C)

#procesing
F = 9/5*C + 32
K = C + 273.15

#output
print("------Resultado------")
print("Grados celcius: " + str(C))
print("Grados kelvin: " + str(K))
print("Grados fahrenheit: " + str(F))

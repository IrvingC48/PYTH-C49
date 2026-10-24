#Este algoritmo resuelvee.......

#Variable integer
# chocolate = 50

# #Variable float
# PI = 3.141592653589793

# #Variable boolean
# is_active = True

# #Variable string/char
# saludo = 'Hola, Mundo!'

# print(f'Variables simples: {chocolate}, {PI}, {is_active}, {saludo}')

# #----------------------------------------------------------------------------

# #Variable list
# #[index1, index2, index3, ...]
# fruits = ['apple', 50, 'cherry', [1,2,3], True]

# #Variable tuple
# #(value1, value2)
# coordinates = (10, 20.0)

# #Variable dictionary
# person = {
#     #key : value,
#     #key : value
#     'name' : 'Juan',
#     'age' : 30,
#     'city' : 'Madrid',
#     'hobbies' : ['football', 'read', 'trips']
# }

# # print(f'Variables complejas: {fruits}, {coordinates}, {person}')

# print(fruits[2])
# print(coordinates[1])
# print(person['hobbies'][1])


#----------------------------------

#Ejemplo de conversión de tipos
numero_str = "100"

#a + b // a,b deben ser del mismo tipo (decimal, enteros)
#No podemos sumar/concatenar un string con un entero directamente
print(f'{numero_str}50') #output 10050

numero_int = int(numero_str) + 50 #Conversion de string a entero y sumar 50
print(numero_int)

fruits_str = ["10", "20", "50"]
print(fruits_str) #Output ['10', '20', '50']
fruits_int = list(map(int,fruits_str))
# print(int(fruits_str))

flotante = 25.657
entero = int(flotante) #Conversión de float a entero
print(entero) #Output 25
print(round(flotante,0)) #Output 26

flotante_nuevo = float(numero_str) #Convertir de entero a float
print(flotante_nuevo) #Output 100.0
print(entero + flotante_nuevo) #Output 125.0

#Ejemplo de conversión a boleano
is_boolean = True
is_boolean_str = str(is_boolean) #Convertir boolean a str
print(is_boolean_str) #Output "True"
is_boolean_int = int(is_boolean) #Output 1
print(is_boolean_int)
is_boolean_float = float(is_boolean) #Output 1.0
print(is_boolean_float)
boolean_float = bool(is_boolean_float) #Output True
print(boolean_float)

fruta = 'platano'
fruta_int = int(fruta)  #ValueError: invalid literal for int() with base 10: 'platano'
print(fruits_int)
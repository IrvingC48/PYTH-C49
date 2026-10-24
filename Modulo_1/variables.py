#Este algoritmo resuelvee.......

#Variable integer
chocolate = 50

#Variable float
PI = 3.141592653589793

#Variable boolean
is_active = True

#Variable string/char
saludo = 'Hola, Mundo!'

print(f'Variables simples: {chocolate}, {PI}, {is_active}, {saludo}')

#----------------------------------------------------------------------------

#Variable list
#[index1, index2, index3, ...]
fruits = ['apple', 50, 'cherry', [1,2,3], True]

#Variable tuple
#(value1, value2)
coordinates = (10, 20.0)

#Variable dictionary
person = {
    #key : value,
    #key : value
    'name' : 'Juan',
    'age' : 30,
    'city' : 'Madrid',
    'hobbies' : ['football', 'read', 'trips']
}

# print(f'Variables complejas: {fruits}, {coordinates}, {person}')

print(fruits[2])
print(coordinates[1])
print(person['hobbies'][1])
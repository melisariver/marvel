#declaro una lista
#lista = ["cadena", 1, False, "nombre", 20, [1, 3, 2 , 4]]
#listaMultiple = ["cadena", ["cadena dentro", "de otra cadena"]]
#listaEnteros = [2, 3, 1]
​
#Insertar en listas
#lista.append(["agregado", "otro mas"])
#print (lista)
​
# #tuplas
#tupla = (1, "hola", True)
​
​
# #diccionarios
#dic = {
#		'Nombre': 'Paco',
#		'Apellido': 'Ocampo'
#		}
​
#Insertar en diccionario
#dic["nuevo"] = value
​

#mi lista
#lista = ["Nombre", 2, True, "melisa", 19, [0, 2, 4, 6]]
#listaMultiple = ["perros", ["miztin", "saya"]]
#listaEnteros = [1, 3]

#agregar a la lista

>>> miDiccionario = 
{
	"nombre" : {'primero' : 'sandra', 'segundo' : 'melisa'},   
	'apellidos' : {'paterno' : 'castillo', 'materno' : 'vargas'}, 
	'edad' : [19]
}
>>> print(miDiccionario
... )
{
	'apellidos': {'paterno': 'castillo', 'materno': 'vargas'}, 
	'nombre': {'segundo': 'melisa', 'primero': 'sandra'}, 
	'edad': [19]
}
>>> otroDiccionario = {'hobbies' : ['leer', 'musica', 'perros']}
>>> miDiccionario['hobbies'] = otroDiccionario
>>> print(miDiccionario)
{
	'apellidos': {'paterno': 'castillo', 'materno': 'vargas'}, 
	'nombre': {'segundo': 'melisa', 'primero': 'sandra'}, 
	'edad': [19], 
	'hobbies': {'hobbies': ['leer', 'musica', 'perros']}
}
>>> miDiccionario["direccion"] = {'calle' : 'pedregal', 'numero' : 66}
>>> print(miDiccionario)
{
	'apellidos': {'paterno': 'castillo', 'materno': 'vargas'}, 
	'nombre': {'segundo': 'melisa', 'primero': 'sandra'},
	'direccion': {'calle': 'pedregal', 'numero': 66}, 
	'edad': [19], 
	'hobbies': {'hobbies': ['leer', 'musica', 'perros']}
}
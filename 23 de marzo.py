#23 DE MARZO DEL 2024: FUNCION MAP()

# - map() function: evuelve un objeto de mapa (que es un iterador) de los resultados después de aplicar la función dada a cada elemento de un iterable determinado (lista, tupla, etc.)
# link: https://www.geeksforgeeks.org/python-map-function/

# - LAMBDA REEMPLAZA A FOR DE FORMA REDUCIDA, SE PASA A:
lista=[3,10,5,7,18,50]
resultado=list(filter(lambda x: x>10, lista))
print(resultado)

#Ejercicio con map x*x

def cuadrado(elemento=0):
    return elemento*elemento
lista=[7,49,343]
resultado1=list(map(cuadrado,lista))
print(resultado)

#con lambda

lista1=[1,2,3,4,5,6,7]
resultado2= list(map (lambda x: x*x, lista1))
print(resultado2)

#Ejercicio: cocatenar un prefijo a cada elemento de palabras

def comida(palabra):
    return prefijo+palabra
palabras=["manzana", "pera", "papaya","limon"]
prefijo="frutas _"

resultad03=list(map(comida,palabras))
print(resultad03)

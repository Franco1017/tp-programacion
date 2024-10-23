#Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
def maximo(a,b,c):
    lista=[a,b,c]
    maximo=max(lista)
    return maximo
def main():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    c=int(input("Ingrese el tercer número: "))
    numero_mayor=maximo(a,b,c)
    print(f"el numero mayor es {numero_mayor}")
    
if __name__ == "__main__":
    main()
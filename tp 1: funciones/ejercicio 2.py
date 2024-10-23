#Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.
def fecha_valida(a,b,c):
    if a < 0 or b < 0:
        return False
    elif b in [1,3,5,7,8,10,12] and a <= 31:
        return True
    elif b in [4,6,9,11] and a <= 30:
        return True
    elif b == 2 and a == 29 and (c%4 == 0 and c%100 !=0) or c%400 == 0:
        return True
    elif b == 2 and a <= 28:
        return True
    else:
        return False
    
def main():
    dia=int(input("Ingrese el día: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))
    if fecha_valida(dia,mes,año):
        print("La fecha es válida")
    else:
        print("La fecha no es válida")
        
if __name__ == "__main__":
    main()
def edad2070(edad,año):

    diferencia = 2070 - año
    return(diferencia+edad)

def main():

    Años = int(input("Introduzca su edad: "))
    AñoActual = int(input("Introduzca el año actual: "))
    print(edad2070(Años,AñoActual))

if __name__ == '__main__':
    main()
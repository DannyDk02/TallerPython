def main():
    numero = int(input("Ingrese un numero: "))
    cadena = ''+str(numero)
    for i in range(numero-1):
        cadena = cadena + str(numero)

    print(cadena)

if __name__ == '__main__':
    main()
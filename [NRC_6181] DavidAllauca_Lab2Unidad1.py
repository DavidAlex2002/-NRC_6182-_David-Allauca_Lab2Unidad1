#funcion calculo
def calculo(radio):
    pi = 3.1415926535
    area = pi*(radio*radio) #fórmula calculo del área del círculo
    print ("El área del círculo con radio ", radio, " es:", str(area)) 
    return area

#ingresar el valor del radio
radio = float(input("Ingrese el radio del círculo: "))
#llamado a la funcion calculo
resultado = calculo(radio)

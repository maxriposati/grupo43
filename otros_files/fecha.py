from datetime import datetime


now = datetime.today()
fecha = input("Dame una fecha:  ")
fecha_actual = datetime.strptime(fecha, "%d-%m-%Y")

if (fecha_actual < now):
    print("La fecha ingresada no puede ser anterior a la fecha actual\nIntente nuevamente")
else:
    print("La fecha ingresada es : " + str(fecha_actual))


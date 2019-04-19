"""
Solución del laboratorio
"""
from custom_functions.temperature_methods import promedio
from custom_functions.temperature_methods import meses
from custom_functions.temperature_methods import departamentomascaliente
from custom_functions.temperature_methods import mesmascalientedetodos
from custom_functions.temperature_methods import promediodelatemperatura

import statistics as np

print("clima")

print("santander")
mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
tems=[]
temg = []
temn = []

try:
    for i in range(0, 12):
        a = int(input("ingrese la temperatura {}:".format(mes[i])))
        tems.append(a)

    print(tems)

    promedio_santander = promedio(tems)

    print("guajira")
    for i in range(0, 12):
        b = (int(input("ingrese la temperatura {}:".format(mes[i]))))
        temg.append(b)

    promedio_guajira = promedio(temg)

    print("nariño")
    for i in range(0, 12):
        c = int(input("ingrese la temperatura {}:".format(mes[i])))
        temn.append(c)

    print(temn)
    promedio_nariño = promedio(temn)

    print("el promdeio del departamento de santander es :", promedio_santander)

    print("el promedio del departamento de aguajira es: ", promedio_guajira)

    print("el promedio del departtamento del nariño es:", promedio_nariño)

    promedion = [promedio_santander, promedio_nariño, promedio_guajira]

    promedionacional = promedio(promedion)

    print("el promedio nacional es:", promedionacional)

    tem1 = meses(tems)

    t2 = meses(temg)

    tem3 = meses(temn)

    print("en santander es:", tem1)
    print("en el agujira es:", t2)
    print("en nariño:", tem3)

    numero1 = max(tems)
    numero2 = max(temg)
    numero3 = max(temn)

    uwi = [numero1, numero2, numero3]
    promediomesc = promedio(uwi)
    print("el promedio de los meses mas calientes", promediomesc)

    uwu= [promedio_santander,promedio_guajira,promedio_nariño]
    uwux2=promediodelatemperatura(uwu)
    print(uwux2)


    lista23 = [numero1, numero2, numero3]
    porfin = mesmascalientedetodos(lista23)
    print("la temperatura mas caliente es", porfin)

    if porfin == numero1:
        print(tem1)
    if porfin == numero2:
        print(t2)
    if porfin == numero3:
        print(tem3)

    lista24 = [tems, temg,temn]
    creo = departamentomascaliente(lista24)
    print(creo)

    desviacionsantander = np.stdev(tems)
    print("la desviacion de santander : ", desviacionsantander)

    desviacionguajira = np.stdev(temg)
    print("la desviacion del aguajira es:", desviacionguajira)

    desviacionnariño = np.stdev(temn)
    print("desviacion del nariño", desviacionnariño)
except ValueError as no:
    print("solo se aceptan numeros")
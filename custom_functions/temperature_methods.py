def promedio(lista):
    suma=0
    for item in lista:
        suma=suma+item
        promedio=suma/len(lista)
    return promedio

def meses (lista):
    holaxd=lista[0]
    for i in range(0,len(lista)):
     if lista[i]>holaxd:
            holaxd=lista[i]
    posicion=lista.index(holaxd)
    if posicion==0:
     return "el mes mas caliente fue enero"
    if posicion==1:
     return "el mes mas caliente fue febrero"
    if posicion==2:
     return "el mes mas  caliente fue marzo "
    if posicion==3:
     return "el mes mas caliente fue abril"
    if posicion==4:
     return "el mes mas caliente fue mayo"
    if posicion==5:
     return "el mes mas calientes fue junio"
    if posicion==6:
     return "el mes mas caliente fue julio"
    if posicion==7:
     return "el mes mas caliente fue agosto"
    if posicion==8:
     return "el mes mas caliente fue septiembre"
    if posicion==9:
     return "el mes mas caliente fue octubre"
    if posicion==10:
     return "el mes mas caliente fue noviembre"
    if posicion==11:
     return "el mes mas caliente fue diciembre"


def promediodelatemperatura(lista):
    prosnñ=lista[0]
    for i in range(0,len(lista)):
        if lista [i]>prosnñ:
            prosnñ=lista[i]
        alfin=lista.index(prosnñ)
        if alfin==0:
            print("el departamento con mayor promedio es santander")
        if alfin==1:
            print("el departamento con mayor promedio es guajira")
        if alfin==2:
            print("el departamento con mayor promedio es nariño")
        return prosnñ

def mesmascalientedetodos(lista):
    gg=lista[0]
    for i in range(0,len(lista)):
        if lista[i]>gg:
            gg=lista[i]

        posicion=max(lista)

        return posicion



def departamentomascaliente(lista):
    tt=lista[0]
    for i in range(0,len(lista)):
        if lista[i]>tt:
            tt=lista[i]

        posicion=lista.index(tt)

    if posicion==0:
     return "el departamento con maxima temperatura es santander"
    if posicion==1:
     return "el departamento con maxima temperatura es guajira"
    if posicion==2:
     return "el departamento con maxima temperatura es nariño"





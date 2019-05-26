# Mi primera prueba en el mumdo real
"""
Se dispone a hacer un programa que optiene el factor de crecimiento de una empresa

1 - Se debe de llamar desde el  print(progreCrecimiento(a, b, c))
a = es el tamanho inicial de la empresa

b = es la estacion
    0 = Prima
    2 = Vera
    1 = Oto
    3 = Inv
    (Nota b<4)

c = son los periodos como tal la empresa va a crecer 

    4 = sigifica un a+0
    10 = mas de un a+o son 10 periodos

Nota importantisima = El periodo en que empieza b no es contado

        ejemplo :  si empiezas en otono el crecimieto de la empresara
                a contar desde invierno,  por ello si quiero empezar 
                a contar lo ganado en otonho tengo que empesar en verana.

    
"""


EstacionXCrecimiento = [("Primavera", 5), ("verano", 3), ("Otonho", 2), ("Invierno", 0)]
estacion_actual = 0
Tamano_empresa = 0


def progreCrecimiento(Tamano_empresa, estacion_actual, nro_estaciones):
    for i in range(0, nro_estaciones):
        Tamano_empresa = Tamano_empresa + EstacionXCrecimiento[sigEstacion(i+estacion_actual)][1]
        print('Estoy en: ', EstacionXCrecimiento[sigEstacion(i+estacion_actual)][0])
        print('La empresa va a crecer', EstacionXCrecimiento[sigEstacion(i+estacion_actual)][1])

    print('==================================================')
    cuuantos_AnosPasaron = nro_estaciones/4

    print('La empresa ha crecido', Tamano_empresa)
    print('En un total de', cuuantos_AnosPasaron)

def sigEstacion(actual):
    if actual >= len(EstacionXCrecimiento)-1:
        normalizacion = actual%(len(EstacionXCrecimiento) - 1)
        return normalizacion
    else:
        return actual + 1

print(progreCrecimiento(5, 0, 6))
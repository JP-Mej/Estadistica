import math

import pandas as pd

#Ingreso de datos

estudiantes ={
    'Ingreso total' : [30, 35, 20, 40, 30, 70, 30, 50, 20, 20, 37, 38, 30, 50, 50, 30, 30,
                       24, 20, 70, 40, 50, 50, 50, 30, 62, 27, 30, 50, 15, 14, 30, 30, 40,
                       30, 35, 20, 35, 30, 30, 30, 50, 50, 40, 60, 30, 70, 40, 35, 65],
    'Egreso total': [22, 25, 15, 25, 24, 14, 14, 15, 24, 17, 39, 32, 9, 20, 24, 22, 12,
                     34, 14, 22, 26, 35, 34, 23, 11, 11, 31, 20, 15, 20, 11, 12, 22, 40,
                     22, 20, 19, 31, 17, 30, 40, 35, 39, 27, 13, 13, 18, 39, 37, 27]
}
#Creacion de dataFrames

df_estudiantes = pd.DataFrame(estudiantes)
#Hallar el numero total de estudiantes

n = len(df_estudiantes['Ingreso total'])


def crear_intervalos_ingresos():

    #para ingresos:

    #Para hallar los intervalos
    rango = df_estudiantes['Ingreso total'].max() - df_estudiantes['Ingreso total'].min()
    m =  1 + (3.3*math.log(n,10))
    m = round(m)
    a = rango/m
    min = df_estudiantes['Ingreso total'].min()
    intervalos = [min]
    #crear los intervalos
    for i in range(1,m+1):
        intervalos.append(min+a*i)

    #Hallar la frecuencia
    frecuencia = pd.cut(df_estudiantes['Ingreso total'],bins=intervalos[0:m], right = False).value_counts(sort = False)

    #Ajuste:
    intervalos[m-1] = intervalos[m-1] - 0.0001
    ajuste = pd.cut(df_estudiantes['Ingreso total'],bins=intervalos[m-1:m+1], right = True ).value_counts(sort = False)


    #Creacion de dataframe:
    df_frecuencia = frecuencia.reset_index()
    df_frecuencia.columns = ['Ingresos','Estudiantes']

    df_ajuste = ajuste.reset_index()
    df_ajuste.columns = ['Ingresos', 'Estudiantes']


    #creacion de dataframe ingreso
    df_ingreso = pd.concat([df_frecuencia,df_ajuste],ignore_index=True)
    return df_ingreso

def crear_intervalos_egresos():
    #misma logica
    rango = df_estudiantes['Egreso total'].max() - df_estudiantes['Egreso total'].min()
    m =  1 + (3.3*math.log(n,10))
    m = round(m)
    a = rango/m
    min = df_estudiantes['Egreso total'].min()
    intervalos = [min]

    for i in range(1,m+1):
        intervalos.append(min+a*i)


    frecuencia = pd.cut(df_estudiantes['Egreso total'],bins=intervalos[0:m], right = False).value_counts(sort = False)


    intervalos[m-1] = intervalos[m-1] - 0.0001
    ajuste = pd.cut(df_estudiantes['Egreso total'],bins=intervalos[m-1:m+1], right = True ).value_counts(sort = False)



    df_frecuencia = frecuencia.reset_index()
    df_frecuencia.columns = ['Egresos','Estudiantes']

    df_ajuste = ajuste.reset_index()
    df_ajuste.columns = ['Egresos', 'Estudiantes']

    df_egreso = pd.concat([df_frecuencia,df_ajuste],ignore_index=True)
    return df_egreso






import matplotlib.pyplot as plt
from intervalos import *
import math

df_ingreso = crear_intervalos_ingresos()
df_egreso = crear_intervalos_egresos()


# Calculo de frecuencia acumulada
df_ingreso['Frecuencia acumulada'] = df_ingreso['Estudiantes'].cumsum()
df_egreso['Frecuencia acumulada'] = df_egreso['Estudiantes'].cumsum()

#amplitud:

m =  1 + (3.3*math.log(n,10))
m = round(m)

rango_ing = df_estudiantes['Ingreso total'].max() - df_estudiantes['Ingreso total'].min()
a_ing = rango_ing/m
inf_ingresos = df_ingreso.loc[0,'Ingresos'].left
sup_ingresos = df_ingreso.loc[m-1,'Ingresos'].right

# Calculo de la marca de clase y asignación correcta de columnas en df_marca_ingreso
df_marca_ingreso = pd.DataFrame({
    'Marca de clase': (df_ingreso['Ingresos'].apply(lambda x: x.left) + df_ingreso['Ingresos'].apply(lambda x: x.right)) / 2,
    'Frecuencia': df_ingreso['Estudiantes'],
    'Frecuencia acumulada': df_ingreso['Frecuencia acumulada']
})

# Agregar filas adicionales para ingresos


df_marca_ingreso = pd.concat(
    [pd.DataFrame({'Marca de clase': [inf_ingresos - a_ing], 'Frecuencia': [0], 'Frecuencia acumulada': [0]}), df_marca_ingreso, pd.DataFrame({'Marca de clase': [sup_ingresos+a_ing], 'Frecuencia': [0], 'Frecuencia acumulada' : [0]})],
    ignore_index=True)


rango_eg = df_estudiantes['Egreso total'].max() - df_estudiantes['Egreso total'].min()
a_eg = rango_eg/m

inf_egresos = df_egreso.loc[0,'Egresos'].left
sup_egresos = df_egreso.loc[m-1,'Egresos'].right



df_marca_egreso = pd.DataFrame({
    'Marca de clase': (df_egreso['Egresos'].apply(lambda x: x.left) + df_egreso['Egresos'].apply(lambda x: x.right)) / 2,
    'Frecuencia': df_egreso['Estudiantes'],
    'Frecuencia acumulada': df_egreso['Frecuencia acumulada']
})


df_marca_egreso = pd.concat(
[pd.DataFrame({'Marca de clase': [inf_egresos-a_eg], 'Frecuencia': [0], 'Frecuencia acumulada' : [0]}), df_marca_egreso, pd.DataFrame({'Marca de clase': [sup_egresos+a_eg], 'Frecuencia': [0], 'Frecuencia acumulada' : [0]})],ignore_index=True)



#Creacion de la ojiva de ingresos
def ojiva_ingreso():
    plt.figure(figsize=(10, 6))
    plt.plot(df_marca_ingreso['Marca de clase'].iloc[0:8], df_marca_ingreso['Frecuencia acumulada'].iloc[0:8], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.title('Ojiva de Ingreso Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()

def ojiva_egreso():    #Creacion de la ojiva de egresos
    plt.figure(figsize=(10, 6))
    plt.plot(df_marca_egreso['Marca de clase'].iloc[0:8], df_marca_egreso['Frecuencia acumulada'].iloc[0:8], marker='s', color='b', label="Egreso total semanal")
    plt.title('Ojiva de Egresos Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()



#Creacion de las 2 ojivas
def ojiva_dos():
    plt.figure(figsize=(10, 6))
    plt.plot(df_marca_ingreso['Marca de clase'].iloc[0:8], df_marca_ingreso['Frecuencia acumulada'].iloc[0:8], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.plot(df_marca_egreso['Marca de clase'].iloc[0:8], df_marca_egreso['Frecuencia acumulada'].iloc[0:8], marker='s', color='b', label="Egreso total semanal")
    plt.title('Ojiva de Ingreso y Egresos Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()


#Creacion del poligono de frecuencia
def pol():
    plt.figure(figsize=(10, 6))
    plt.plot(df_marca_ingreso['Marca de clase'], df_marca_ingreso['Frecuencia'], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.plot(df_marca_egreso['Marca de clase'], df_marca_egreso['Frecuencia'], marker='s', color='b', label="Egreso total semanal")
    #plt.axvline(x = 26, color='g') borrar el # para añadir la linea
    plt.title('Poligono de frecuencia de Ingreso y Egresos Totales Semanales')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()



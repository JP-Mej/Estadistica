import pandas as pd
import matplotlib.pyplot as plt


#Ingreso de datos
ingreso_data ={
    'Ingreso total' : [10,18,26,34,42,50, 58, 66, 74],
    'Estudiantes' : [0,7,17,6,5,9,2,4,0]
}
egreso_data = {
    'Egreso total' : [6.75,11.25,15.75,20.25,24.75,29.25,33.75,38.25,42.75],
    'Estudiantes' : [0,8,9,10,9,3,5,6,0]
}


#Creacion de dataFrames
df_ingreso = pd.DataFrame(ingreso_data)
df_egreso = pd.DataFrame(egreso_data)

#Calculo de frecuencia acumulada
df_ingreso['Frecuencia acumulada'] = df_ingreso['Estudiantes'].cumsum()
df_egreso['Frecuencia acumulada'] = df_egreso['Estudiantes'].cumsum()


#Creacion de dataFrames
df_ingreso = pd.DataFrame(ingreso_data)
df_egreso = pd.DataFrame(egreso_data)

#Calculo de frecuencia acumulada
df_ingreso['Frecuencia acumulada'] = df_ingreso['Estudiantes'].cumsum()
df_egreso['Frecuencia acumulada'] = df_egreso['Estudiantes'].cumsum()



#Creacion de la ojiva de ingresos
def ojiva_ingreso():
    plt.figure(figsize=(10, 6))
    plt.plot(df_ingreso['Ingreso total'], df_ingreso['Frecuencia acumulada'], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.title('Ojiva de Ingreso Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()

def ojiva_egreso():    #Creacion de la ojiva de egresos
    plt.figure(figsize=(10, 6))
    plt.plot(df_egreso['Egreso total'], df_egreso['Frecuencia acumulada'], marker='s', color='b', label="Egreso total semanal")
    plt.title('Ojiva de Egresos Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()



#Creacion de las 2 ojivas
def ojiva_dos():
    plt.figure(figsize=(10, 6))
    plt.plot(df_ingreso['Ingreso total'], df_ingreso['Frecuencia acumulada'], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.plot(df_egreso['Egreso total'], df_egreso['Frecuencia acumulada'], marker='s', color='b', label="Egreso total semanal")
    plt.title('Ojiva de Ingreso y Egresos Total Semanal de los estudiantes')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()


#Creacion del poligono de frecuencia
def pol():
    plt.figure(figsize=(10, 6))
    plt.plot(df_ingreso['Ingreso total'], df_ingreso['Estudiantes'], marker='o', color='r', label="Ingreso total semanal") #x,y,paramt
    plt.plot(df_egreso['Egreso total'], df_egreso['Estudiantes'], marker='s', color='b', label="Egreso total semanal")
    #plt.axvline(x = 26, color='g') borrar el # para añadir la linea
    plt.title('Poligono de frecuencia de Ingreso y Egresos Totales Semanales')
    plt.xlabel('Monto de dinero en soles')
    plt.ylabel('Estudiantes')
    plt.legend()
    plt.grid()
    plt.show()
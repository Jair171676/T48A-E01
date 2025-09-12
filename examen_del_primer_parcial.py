import numpy as np
nombre = "Jair de Jesus Nieto"
numero_de_matricula = 171676
fecha = '2025-11-09'

def capitalizacion():
    data = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(data)
    mediana = np.median(data)
    moda = stats.mode(data).mode[0]
    desv_est = np.std(data)
    return (media, mediana, moda, desv_est)

data = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(data)
    varianza = np.var(data)
    desv_est = np.std(data)
    return (rango, varianza, desv_est)

data = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(data)
    varianza = np.var(data)
    desv_est = np.std(data)
    return (rango, varianza, desv_est)



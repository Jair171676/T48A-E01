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

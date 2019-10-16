import pandas as pd

def comparacion(data):
    i = 0
    k = data.shape[0]
    while i < k:
        j = i
        while j < k:
            if data.iat[i, 0] == data.iat[j, 0] and i!=j:
                data.iat[i,3] = data.iat[i, 3] + data.iat[j, 3]
                data.drop([j], inplace=True)
                data.reset_index(drop=True, inplace=True)
                k = k - 1
            j = j + 1
        i = i + 1
    return data

print('PELICULAS DE BLOKBASTER')
pelisBlokbaster = pd.DataFrame({'nombre':['Jokar', 'Harry Popoter',
                                          'Rapidos y Jugosos', 'Los Revengadores'],
                                'existencia':[10, 23, 18, 25],
                                'prestamos':[8, 54, 46, 61],
                                'distribuidor':['DC comacs', 'Los Wrogser',
                                                '19 century' , 'Terrarial Studio']})

print('PELICULAS DE NETFLOX')
pelisNetflox = pd.DataFrame({'nombre' : ['Tranformistas', 'Jokar', 'Dino Park',
                                       'Piratas del Atlantico', 'Los Revengadores'],
                            'Val_Taquilla' : [5.4, 12.3, 9.3, 3.1, 6.5],
                            'Funciones_Emt' : [21, 9, 34, 19, 42],
                            'existencia': [5, 19, 7, 11, 13]})

# La empresa Netflox compro a Blokbaster, y desea saber su nuevo inventario
print(pelisBlokbaster)
print(pelisNetflox)

pelisUnion = pd.concat([pelisNetflox, pelisBlokbaster], axis = 0, join='outer',
                       join_axes = [pelisNetflox.columns], ignore_index = True)

comparacion(pelisUnion)
print('NUEVO INVENTARIO DE PELICULAS')
print(pelisUnion)

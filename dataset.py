import pandas as pd

def comparacion(data):
    for i in data.index:
        for j in data.index:
            if data.iat[i, 0] == data.iat[j, 0] and i!=j:
                data.iat[i,3] = data.iat[i, 3] + data.iat[j, 3]
                data.drop([j], inplace=True)
    return data

pelisBlokbaster = pd.DataFrame({'nombre':['Jokar', 'Harry Popoter',
                                          'Rapidos y Jugosos', 'Los Revengadores'],
                                'existencia':[10, 23, 18, 25],
                                'prestamos':[8, 54, 46, 61],
                                'distribuidor':['DC comacs', 'Los Wrogser',
                                                '19 century' , 'Terrarial Studio']})

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
print(pelisUnion)

comparacion(pelisUnion)
 

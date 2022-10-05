#Importar la libreria pandas
import pandas as pd
import cleanNewLine as cl

def newCsv ():
    #Importamos archivo csv
    df = pd.read_csv("filesToEdit\Kaps_adv_published.csv", sep=',')


    #Leemos cada título, le sacamos los '\n' y guardamos el titulo editado
    for frame in range(len(df)):
        singleFrame = df.loc[frame, 'title']
        #singleFrame = list(map(lambda l: l.rstrip('\n'), singleFrame))
        singleFrame = cl.cleanNewLine(singleFrame)
        finalString = "".join(singleFrame)
        
        df.loc[frame, 'title'] = finalString

    #Exportamos la data formateada a un nuevo csv
    df.to_csv('filesToEdit\Kaps_adv_published.csv', index = False)
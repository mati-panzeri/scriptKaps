#Importar la libreria pandas
import pandas as pd
import cleanNewLine as cl


#Importamos archivo csv y txt
df = pd.read_csv("filesToEdit/Kaps_adv_published.csv", sep=',')
archivoTxt = open('filesToEdit/advisories.txt')


#array de advisories
queue = archivoTxt.readlines()
updates = []
newAdvisories = []

#print(queue)


for adv in range(len(queue)):
    cleanTitle = cl.cleanNewLine(queue[adv])
    #list(map(lambda l: l.rstrip('\n'), newAdvisories[adv]))
    cleanTitle = "".join(cleanTitle)
    cleanTitle = cleanTitle.split(':', 1)
    cleanTitle = cleanTitle[1].strip()
    boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
    
    if boolean.any():
        updates.append(cleanTitle)
    else:
        newAdvisories.append(cleanTitle)
    #print(boolean)

    #updates.append(boolean['title'])

    #buscar cleanTitle en df titulos
        # updates.append(cleanTitle)
    #else:
    #    newAdvisories.append(cleanTitle)
    #arrAdvisories.append(cleanTitle)

#print(df['title'])
print(updates)
print (newAdvisories)

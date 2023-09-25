def append (boolean, cleanTitle, updates, newAdvisories):
    if boolean.any():
        updates.append(cleanTitle)
    else:
        newAdvisories.append(cleanTitle)
    
    #return updates, newAdvisories
def append (boolean, title, updates, newAdvisories):
    if boolean.any():
        updates.append(title)
    else:
        newAdvisories.append(title)
    
    #return updates, newAdvisories
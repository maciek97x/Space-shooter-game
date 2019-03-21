def getData():
    return open("data/data.txt").readlines()

def saveData(tab):
    f = open("data/data.txt", 'w')
    f.write(''.join(tab))
    f.close()


    
    
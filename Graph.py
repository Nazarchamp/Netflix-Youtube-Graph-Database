mList = []
pList = []
class Movie:
    lList = []

class Person:
    name = "John Doe"
    lList = []
    cList = []
    rMovies = []

def MakePerson(newName):    
    pList.append(Person())
    pList[len(pList)-1].name = newName
    RunThrough()
    
def RunThrough():
    for i in range(len(pList)):
        del pList[i].cList[:]
        for j in range(len(pList)):
            pList[i].cList.append(0)
    
def MakeMovie(movieName):
    mList.append(Movie())
    mList[len(mList)-1].name = movieName

def Like(pIndex, mIndex):
    pList[pIndex].lList.append(mIndex)
    print()
    for i in mList[mIndex].lList:
        pList[pIndex].cList[i] += 1
        pList[i].cList[pIndex] += 1
        
    mList[mIndex].lList.append(pIndex)

    
def Recommend(pIndex):
    rList = []
    rBool = True
    for idx, i in enumerate(pList[pIndex].cList):
        if(idx != pIndex):
            if(len(rList) != 0):
                if(i > rList[0]):
                    del rList[:]
                    rList.append(idx)
                if(i == rList[0]):
                    rList.append(idx)
            else:
                rList.append(idx)
            
    for i in rList:
        for j in pList[i].lList:
            for k in pList[pIndex].rMovies:
                if(mList[j].name == k[2:]):
                    rBool = False
                    break
                
            if(rBool):
                pList[pIndex].rMovies.append(str(j) + " " + mList[j].name)
                
            rBool = True
    
while True:
    n = input()
    exec(n)





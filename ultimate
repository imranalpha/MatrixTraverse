import numpy as np

def Traverse(matrix):
    TotalScore=0
    #all paths
    def findpaths(ret,mat,path,i,j):
        m=len(mat)
        n=len(mat[2])

        def isvalid(i,j):
            return(i>=0 and i<m and j>=0 and j<m)

        if(i==m-1 and j==n-1):
            ps=np.array(path)
            ret.append(ps)
            return
        if(mat[i][j]!=-1):
            d={"col":i,"row":j,"val":mat[i][j]}
            path.append(d)
        else:
            return

        #move horizontal
        if(isvalid(i,j+1)):
            findpaths(ret,mat,path,i,j+1)

        #move vertical
        if(isvalid(i+1,j)):
            findpaths(ret,mat,path,i+1,j)
        if(len(path)>0):
            path.pop()
        
    p=[]
    ret=[]
    findpaths(ret,matrix,p,0,0)


    #find forward path
    gopath=0
    ban=-1
    pathscore=0
    for i,x in enumerate(ret):
        score=0
        for j,y in enumerate(x):
            if(y['val']==-1):
                print("-1 at ",y)
                break
            score+=y['val']
        if(score>pathscore):
            pathscore=score
            gopath=i
    try: 
        print("Score- ",pathscore+matrix[-1][-1]," Farward with ",gopath,ret[gopath])
        TotalScore+=pathscore
    except:
        TotalScore=0
        return TotalScore

    #reseting 1s after using
    for i,x in enumerate(ret):
        for j,y in enumerate(x):
            for k in ret[gopath]:
                if(y['col']==k['col'] and y['row']==k['row']):
                    ret[i][j]['val']=0
    #backward path    
    gopath=0
    ban=-1
    pathscore=0
    for i,x in enumerate(ret):
        score=0
        for j,y in enumerate(x):
            if(y['val']==-1):
                break
            score+=y['val']
        if(score>pathscore):
            pathscore=score
            gopath=i
    print("Score- ",pathscore," Backward with ",gopath,ret[gopath])
    TotalScore+=pathscore
    TotalScore+=matrix[-1][-1]
    
    print(ret)
    return TotalScore

#inputs
matrix=[[1,-1,1],
        [1,-1,1],
        [1,1,1]]
#call the function with ant matrix
Traverse(matrix)

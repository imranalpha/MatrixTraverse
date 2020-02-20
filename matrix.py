def Traversing(mat):
    col=0
    row=0
    lastvalue=0
    score=0
    end_reched=False
    length=len(mat)
    if(mat[length-1][length-1]==-1) or (mat[0][0]==-1):
        score=0
        return score
    for x in mat:
        for y in x:
            print(col,row)
            if(col+1<len(mat)):
                if(row+1<len(x)):
                    if(mat[col+1][row]==1):
                        col+=1
                    elif(mat[col][row+1]==1):
                        row+=1
                    elif(mat[col+1][row]!=-1):
                        col+=1
                    elif(mat[col][row+1]!=-1):
                        row+=1
                    else:
                        break
                else:
                    if(mat[col+1][row]!=-1):
                        col+=1
                    elif(mat[col+1][row-1]!=-1):
                        score-=lastvalue
                        col+=1
                        row-=1
                    else:
                        break
                        
            elif(row+1<len(x)):
                    if(mat[col][row+1]!=-1):
                        row+=1
                    elif(mat[col-1][row+1]!=-1):
                        score-=lastvalue
                        col-=1
                        row+=1
                    else:
                        break
            lastvalue=mat[col][row]
            if(mat[col][row]==1):
                mat[col][row]=0
                score+=1
            if(col&row==2):
                end_reched=True
                break
    for x in mat:
        for y in x:
            print(col,row)
            if(col>0):
                if(row>0):
                    if(mat[col-1][row]==1):
                        col-=1
                    elif(mat[col][row-1]==1):
                        row-=1
                    elif(mat[col-1][row]!=-1):
                        col-=1
                    elif(mat[col][row-1]!=-1):
                        row-=1
                    else:
                        break
                else:
                    if(mat[col-1][row]!=-1):
                        row-=1
                    elif(mat[col-1][row+1]!=-1):
                        score-=lastvalue
                        col-=1
                        row+=1
                    else:
                        break
            elif(row>0):
                    if(mat[col][row-1]!=-1):
                        row-=1
                    else:
                        break
            lastvalue=mat[col][row]
            if(mat[col][row]==1):
                mat[col][row]=0
                score+=1
            if(col-2<0)and(row-2<0):
                break
    if(end_reched):
        return score
    return 0

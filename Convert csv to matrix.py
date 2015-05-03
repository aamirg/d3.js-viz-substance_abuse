#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: CSV TO MATRIX
#
# Author:      Aamir
#
# Created:     11/04/2015
# Copyright:   (c) Aamir 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
import json

def main():

    DATA={}

    file_input=open("data\drugs.csv","r")
    datareader=csv.reader(file_input)

    for row in datareader:
        row[0].replace(" ","")
        row[1].replace(" ","")
        if row[0] not in DATA.keys():
            DATA[row[0]]=[]
        DATA[row[0]].append(row[1])
    #print DATA

    RC_names=[]

    for x in DATA.keys():
        for y in DATA[x]:
            RC_names.append(y)
        RC_names.append(x)
    RC_names=list(set(RC_names))
    RC_names.sort()
    print RC_names

    temp=RC_names
    RC_names=[]
    x= [2,3,5,6,8,12,14,15,19,20,25,26,27,29,30]

    for i in range(len(temp)):
        if i in x:
            continue
        else:
            RC_names.append(temp[i])

    for i in x:
        RC_names.append(temp[i])


    print RC_names





    file_out=open("data\names.csv","w")
    file_out.write("name\n")

    for line in RC_names:
        file_out.write(line+"\n")
    file_out.close()

    NAMES_IDS={}

    n=len(RC_names)

    for i in xrange(n):
        NAMES_IDS[i]=RC_names[i]
    print NAMES_IDS

    matrix = [[0 for x in range(n)] for y in range(n)]



    for x in DATA:
        for y in DATA[x]:
            value=1

            for k, v in NAMES_IDS.iteritems():
                if v == y:
                     j=k

            for k, v in NAMES_IDS.iteritems():
                if v == x:
                     i=k
            #print i,j
            matrix[i][j]=value
            matrix[j][i]=value
    print




    #for i in x:
        #for j in range(len(matrix[i])):
            #matrix[i][j]=0.000001

    for i in matrix:
       print i

    file_op=open("data\matrix.json","w")
    json.dump(matrix,file_op)
    file_op.close()

if __name__ == '__main__':
    main()

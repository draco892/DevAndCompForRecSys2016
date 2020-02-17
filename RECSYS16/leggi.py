import csv

def impressions():
    imp_file = open('impressions.csv')
    imp_file.readline()
   
    for line in imp_file:
        line = line.strip().split('\t')
        val = (line[0],line[1],line[2],line[3].strip().split(','))
        yield val

def interactions():
    int_file = open('interactions.csv')
    int_file.readline()
   
    for line in int_file:
        line = line.strip().split('\t')
        val = (line[0],line[1],line[2],line[3])
        yield val

def items():
    it_file = open('items.csv')
    it_file.readline()
   
    for line in it_file:
        line = line.strip().split('\t')
        val = (line[0],line[1].strip().split(','),line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10].strip().split(','),line[11],line[12])
        yield val

def users():
    u_file = open('users.csv')
    u_file.readline()

    for line in u_file:
        line = line.strip().split('\t')
        if len(line)==11:
            val = (line[0],line[1].strip().split(','),line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],[])
        else:
            val = (line[0],line[1].strip().split(','),line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11].strip().split(','))
        yield val

    

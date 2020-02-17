"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import csv

#file contenete la classe di funzioni riguardanti la lettura del dataset

from lib2to3.pgen2.grammar import line

#classe Riguardante la lettura dei dati da file

class reader:

    #modulo riguardante l'inizializzazione della classe
    def __init__(self):
        self.fname_users = 'Dataset/users.csv';
        self.fname_items = 'Dataset/items.csv';
        self.fname_interactions = 'Dataset/interactions.csv';
        self.fname_impressions = 'Dataset/impressions.csv';

    #modulo riguardante la lettura da file
    def read(self,n_file):
        if (n_file == "users"):
            n_file = self.fname_users;
        elif (n_file == "items"):
            n_file = self.fname_items;
        elif (n_file == "interactions"):
            n_file = self.fname_interactions;
        elif (n_file == "impressions"):
            n_file = self.fname_impressions;
        else:
            print "Errore nella selezione del file da leggere\n";

        r_file = open(n_file);
        r_file.readline();

        if (n_file == self.fname_users):
            for line in r_file:
                line = line.strip().split('\t');
                if len(line)== 11:
                    val = (line[0], line[1].strip().split(','), line[2], line[3], line[4], line[5], line[6], line[7],
                        line[8], line[9], line[10], [])
                else:
                    val = (line[0], line[1].strip().split(','), line[2], line[3], line[4], line[5], line[6], line[7],
                        line[8], line[9], line[10], line[11].strip().split(','))
                yield val
        elif (n_file == self.fname_items):
            for line in r_file:
                line = line.strip().split('\t');
                val = (line[0], line[1].strip().split(','), line[2], line[3], line[4], line[5], line[6], line[7],
                       line[8], line[9], line[10].strip().split(','), line[11], line[12]);
                yield val;
        elif (n_file == self.fname_interactions):
            for line in r_file:
                line = line.strip().split('\t');
                val = (line[0], line[1], line[2], line[3]);
                yield val;
        elif (n_file == self.fname_impressions):
            for line in r_file:
                line = line.strip().split('\t');
                val = (line[0], line[1], line[2], line[3].strip().split(','));
                yield val;



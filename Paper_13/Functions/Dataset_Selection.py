"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

#File contenente la funzione di selezione della tipologia di Dataset

def d_s():
    while (True):
        print "Tipologie di Dataset:";
        print "\t1) Dataset Completo";
        print "\t2) Dataset Ridotto";
        sel = int(input("Selezione:\t"));
        if (sel == 1):
            return False;
        elif (sel == 2):
            return True;
        else:
            print "Errore:\tSelezione non valida\n";

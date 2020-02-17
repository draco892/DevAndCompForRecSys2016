"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from operator import itemgetter
from collections import OrderedDict

#File contenente la funzione riguardante la creazione della lista contenente i top30 users

def creation_top30_list(d_sc):
    d_sorted = OrderedDict(sorted(d_sc.items(), key=itemgetter(1), reverse=True));
    l = [];
    ccc = 0;
    for key in d_sorted:
        #print d_sorted[key];
        l.append(key);
        ccc += 1;
        if ccc == 30:
            break;
    return l;
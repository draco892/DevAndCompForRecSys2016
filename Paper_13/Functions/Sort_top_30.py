"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from collections import OrderedDict
from operator import itemgetter

#File contenente la funzione riguardante l'ordinamento degli score e la creazione della lista top 30

def Sort_t30(score_dict):
    d_sorted = OrderedDict(sorted(score_dict.items(), key=itemgetter(1), reverse=True));
    l_t30 = [];
    ccc = 0;
    for key in d_sorted:
        l_t30.append(key);
        ccc += 1;
        if ccc == 30:
            break;
    return l_t30;
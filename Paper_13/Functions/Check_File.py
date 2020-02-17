"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import os.path

#File contenente la funzione di controllo dell'esistenza di un file.

def check(f_name):
    return os.path.isfile(f_name);
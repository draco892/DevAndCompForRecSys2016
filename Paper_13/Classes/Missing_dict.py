"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from collections import defaultdict

#File contenente la classe missingdict e missingdict_items_si_so

class missingdict(defaultdict):
    def __missing__(self, key):
        return int(0);

class missingdict_items_si_so(defaultdict):
    def __missing__(self, key):
        return [int(0),float(0.0),int(0),float(0.0),int(0),float(0.0)];
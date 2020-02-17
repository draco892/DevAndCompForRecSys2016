"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

#File contenente la funzione che resistuisce il numero degli Items, la funzione riguardante la creazione/reset
# del dizionario degli scores e la funzione che genera una lista degli items.

def nr_items(c):
    c.execute('select count(id) as NumberOfItems from items');
    for r in c:
        n_items = int(r[0]);
    return n_items;

def item_list(c):
    c.execute('select id as item_id from items');
    item_l = [];
    for row in c:
        item_l.append(row['item_id'])
    return item_l;

def Create_Reset_scores(c,s_d):
    c.execute('select DISTINCT id as Item_id from items');
    for row in c:
        s_d[row['Item_id']] = 0.0;
    return s_d;
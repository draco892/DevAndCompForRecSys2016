"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

#File contenente la funzione che ritorna quante volte compare un item tra le impression di una settimana
# e la funzione che ritorna la lista degli items di un impressions

def c_i(c, item_id, imp_id):
    c.execute('select count(item_id.%s) from imp_items where (imp_id = %s)'%(item_id,imp_id));
    for r in c:
        n_i = int(r[0]);
    return n_i;

def l_i(c,imp_id,item_list):
    c.execute('select item_id as id from imp_terms where imp_id = %s'%(imp_id));
    for row in c:
        item_list.append(row['id']);
    return item_list;

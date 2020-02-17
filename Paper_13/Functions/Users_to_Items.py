"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Count_item

#File contenente la funzione riguardante la creazione della lista degli users
# e del dizionario u2i relativo alle interactions ed alle impressions

def users_list(c):
    c.execute('select id from users');
    users_l = [];
    for row in c:
        users_l.append(int(row['id']));
    users_l.sort(key=int);
    return users_l;

def user2items_int(c):
    c.execute('select user_id,item_id from interactions \
        where interaction_type="1" or interaction_type="2" \
        or interaction_type="3"');
    u2i_int = {};
    for row in c:
        if row['user_id'] not in u2i_int:
            u2i_int[row['user_id']]=set();
        u2i_int[row['user_id']].add(row['item_id']);
    return u2i_int;

def user2items_imp(c1,c2):
    c1.execute('select i1.id, i1.user_id, i1.week, i2.imp_id, i2.item_id, i2.ord\
              from impression i1\
              left join imp_terms i2 on i1.id = i2.imp_id');
    u2i_imp = {};
    for row in c1:
        if row['i1.user_id'] not in u2i_imp:
            u2i_imp[row['i1.user_id']]=set();
        if (row['i2.item_id'] not in u2i_imp[row['i1.user_id']])\
                and (row['i1.week'] not in u2i_imp[row['i1.user_id']]):
            item_list = [row['i2.item_id'], row['i1.week']];
            u2i_imp[row['i1.user_id']].add(row['i2.item_id']);
            u2i_imp[row['i1.user_id']].add(row['i1.week']);
            c_i_t = Count_item.c_i(c2,row['i2.item_id'],row['i1.id']);
            item_list.append(c_i_t);
            u2i_imp[row['i1.user_id']].add(item_list);
    return u2i_imp;
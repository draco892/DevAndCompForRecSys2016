"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Time_Calcolation as t_c

#File contenente le funzioni riguardanti la creazione di una lista degli item utili per un determinato user
# e per l'attribuizione degli score relaitivi alle tipologie di interactions

def Useful_items_interactions(c,fu):
    c.execute('select DISTINCT item_id from interactions\
              where (interaction_type="1" or interaction_type="2" or interaction_type="3")\
               and (user_id = %s)'%(fu));
    item_list_int = [];
    for row in c:
        item_list_int.append(row['item_id']);
    return item_list_int;

def Userful_items_impression(c,fu):
    c.execute('select id, week from impressions where (user_id = %s)'%(fu));
    item_list_imp = [];
    for row in c:
        item_list_imp.append(int(row['id']));
        #item_list_imp.append(int(row['Count']));
        item_list_imp.append(int(row['week']));
    return item_list_imp;

def Positive_Interaction(c,fu,fi,t_max,diff_max):
    c.execute('select created_at from interactions\
        where (interaction_type="1" or interaction_type="2" or interaction_type="3")\
              and (user_id = %s) and (item_id = %s)'%(fu,fi));
    score_int = float(0.0);
    for row in c:
        score_int = score_int + t_c.Time_decay(t_max,row['created_at'],diff_max);
    return score_int;

def Count_impressions_user(c,id_imp):
    c.execute('select count(imp_id) as Count from imp_items where imp_id = %s'%(id_imp));
    n_time = 0;
    for row in c:
        n_time = int(row['Count']);
    return n_time;

def Positive_Impressions(t_max,diff_max,t_current):
    score_imp = float(t_c.Time_decay(t_max,t_current,diff_max));
    score_imp = score_imp * float(0.05);
    return score_imp;

def Negative_Interactions(c,fu,s_d):
    c.execute('select item_id from interactions\
        where interaction_type="4" and user_id = %s'%(fu));
    for row in c:
        s_d[row['Item_id']] = 0.0;
    return s_d;

def impression_items_list(c,imp_id):
    c.execute('select DISTINCT item_id as id from imp_items where imp_id = %s'%(imp_id));
    item_list = []
    for row in c:
        item_list.append(row['id']);
    return item_list;

def impression_items_list_no_dist(c,imp_id):
    c.execute('select item_id as id from imp_items where imp_id = %s'%(imp_id));
    item_list = []
    for row in c:
        item_list.append(row['id']);
    return item_list;

def item_impression_count(c,imp_id,item_id):
    c.execute('select count(item_id) as Count from imp_items\
            where (imp_id = %s) and (item_id = %s)'%(imp_id,item_id));
    for row in c:
        nr_times = int(row['Count']);
    return nr_times;

def user_last_int(c,u_id,i_id):
    c.execute('select Max(created_at) as last_time from interactions\
            where (user_id = %s) and (item_id = %s)'%(u_id,i_id));
    for r in c:
        last_it_time = int(r['last_time']);
    return last_it_time;

def user_last_imp(c,u_id,i_id):
    c.execute('select Max(imp.week) as last_time from impressions as imp, imp_items as imp_it\
            where (imp.user_id = %s) and (imp_it.item_id = %s) and (imp_it.imp_id = imp.id)'%(u_id,i_id));
    for r in c:
        last_imp_time = int(r['last_time']);
    return last_imp_time;
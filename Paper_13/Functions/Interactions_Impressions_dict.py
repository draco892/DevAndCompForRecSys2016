"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import datetime
import Time_Calcolation as t_c

#File contenente le funzioni riguardanti la creazione dei dict e delle list riguardanti
# le impressions e le interactions

def imp_items_list(c):
    c.execute('select * from imp_items');
    imp_it_l = [];
    for r in c:
        it_l = [];
        it_l.append(int(r['imp_id']));
        it_l.append(int(r['item_id']));
        it_l.append(int(r['ord']));
        imp_it_l.append(it_l);
    return imp_it_l;

def imp_list(c):
    c.execute('select * from impressions');
    imp_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['id']));
        l_par.append(int(r['user_id']));
        imp_l.append(l_par);
    return imp_l;

def imp_d_creation(c,max_t,imp_items_l,max_imp_diff):
    #print "Inizio calcolo impressions";
    a = datetime.datetime.now();
    c.execute('select * from impressions');
    #print "parte_1";
    imp_d = {};
    for r in c:
        imp_l = [];
        imp_l.append(int(r['user_id']));
        imp_l.append(int(r['year']));
        imp_l.append(int(r['week']));
        diff_t = t_c.time_diff((int(r['week']) + (int(r['year']) * 52)),max_t);
        imp_l.append(diff_t);
        imp_l.append(int(0));
        items_imp_d = {};
        imp_l.append(items_imp_d);
        single_imp_score = t_c.Time_decay_diff(diff_t,max_imp_diff) * 0.05;
        imp_l.append(single_imp_score);
        imp_d[int(r['id'])] = imp_l;
    z = datetime.datetime.now();
    #print (z-a);
    #print "parte_2";
    e = datetime.datetime.now();
    if (len(imp_items_l)>0):
        for i in range(0,len(imp_items_l)):
            imp_id = imp_items_l[i][0];
            item_id = imp_items_l[i][1];
            imp_d[imp_id][4] += 1;
            if item_id not in imp_d[imp_id][5]:
                l = imp_d[imp_id][5];
                l[item_id] = 1;
                imp_d[imp_id][5] = l;
            else:
                l = imp_d[imp_id][5];
                l[item_id] += 1;
                imp_d[imp_id][5] = l;
    b = datetime.datetime.now();
    #print (e-z);
    #print "Fine calcolo Imp";
    #print "Tempo totale " + str(b - a);
    return imp_d;

def int_list(c,max_t):
    c.execute('select * from interactions');
    int_l = [];
    for r in c:
        i_par = [];
        i_par.append(int(r['user_id']));
        i_par.append(int(r['item_id']));
        i_par.append(int(r['interaction_type']));
        date = int(r['created_at']);
        i_par.append(date);
        i_par.append(t_c.time_diff(date,max_t));
        int_l.append(i_par);
    return int_l;

def int_d_creation(c,max_t,int_l,max_diff):
    #print "Inizio calcolo interactions";
    a = datetime.datetime.now();
    int_d = {};
    c.execute('select DISTINCT interaction_type as t from interactions');
    for r in c:
        int_d[int(r['t'])] = [];
    if (len(int_l)>0):
        for i in range(0,len(int_l)):
            l = int_d[int_l[i][2]];
            l_par = [];
            l_par.append(int_l[i][0]);
            l_par.append(int_l[i][1]);
            l_par.append(int_l[i][3]);
            diff_t = int_l[i][4];
            l_par.append(diff_t);
            score = t_c.Time_decay_diff(diff_t,max_diff);
            l_par.append(score);
            l.append(l_par);
            int_d[int_l[i][2]] = l;
    b = datetime.datetime.now();
    #print "Fine calcolo interactions";
    #print (b-a);
    return int_d;
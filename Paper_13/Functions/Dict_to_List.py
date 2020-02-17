"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

#File contenente le funzioni atte a trasformare le variabili dict in list

def users_event_list_creation(int_d,imp_l,imp_d):
    event_l = [];
    for int_type in int_d:
        if len(int_d[int_type])>0:
            for i in range(0,len(int_d[int_type])):
                item_id = int_d[int_type][i][0];
                score = int_d[int_type][i][3];
                event_l_par = [item_id,score];
                event_l.append(event_l_par);
    if len(imp_l)>0:
        for i in range(0,len(imp_l)):
            imp_id = imp_l[i];
            single_imp_score = imp_d[imp_id][6];
            if imp_d[imp_id][4]>0:
                for item_id in imp_d[imp_id][5]:
                    nr_times = imp_d[imp_id][5][item_id]
                    event_l_par = [item_id, single_imp_score*nr_times];
                    event_l.append(event_l_par);
    return event_l;


def user_d_to_list(user_d,imp_d):
    users_l = [];
    i = 0;
    perc = 5;
    for user_id in user_d:
        #print user_id;
        fos_l = user_d[user_id][9];
        jbrl_l = user_d[user_id][10];
        nr_groups = user_d[user_id][13];
        w_e = user_d[user_id][16];
        rctr_s = user_d[user_id][17];
        AS_score = user_d[user_id][18];
        event_l = users_event_list_creation(user_d[user_id][14],user_d[user_id][15],imp_d);
        us_l_par = [user_id,fos_l,jbrl_l,nr_groups,w_e,rctr_s,AS_score,event_l];
        users_l.append(us_l_par);
        i += 1;
        if (i%250)==0:
            print "\t" + str(perc) + "%";
            perc += 5;
    return users_l;

def item_sim_scores_dict_creation(old_sim_scores,items_d):
    sim_scores = {};
    for item_id in old_sim_scores:
        io_score = old_sim_scores[item_id][0];
        cos_score = old_sim_scores[item_id][1];
        iknn_si = items_d[item_id][21];
        l_par = [io_score,cos_score,iknn_si];
        sim_scores[item_id] = l_par;
    return sim_scores;

def items_d_to_list(items_d):
    items_l = [];
    i = 0;
    #print len(items_d);
    contr = len(items_d)/50;
    proc = 2;
    for item_id in items_d:
        #print item_id;
        ap_score = items_d[item_id][17];
        iknn_si = items_d[item_id][21]
        sim_scores = item_sim_scores_dict_creation(items_d[item_id][24],items_d);
        l_par = [item_id,ap_score,iknn_si,sim_scores];
        items_l.append(l_par);
        i += 1;
        if (i%contr)==0:
            print "\t" + str(proc) + "%";
            proc += 2;
    return items_l;

def score_items_list_creation(sc_i_d):
    sc_items_l = [];
    for item_id in sc_i_d:
        par_l = [item_id,float(0.0)];
        sc_items_l.append(par_l);
    return sc_items_l;
"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import math

#file contenente la funzione riguardante l'assegnazione dei valori di sim cos e io agli eventi

def Event_sim(u_int_d,u_imp_l,w_e,imp_d,item_d,item_id,lambd,alpha):
    iknn_score = 0.0;
    ms_score = 0.0;
    iknn_si = math.pow((item_d[item_id][21] + lambd),1.00 - alpha);
    for int_type in u_int_d:
        if (len(u_int_d[int_type]) > 0):
            for i in range(0,len(u_int_d[int_type])):
                event_score = u_int_d[int_type][i][3];
                event_item_id = u_int_d[int_type][i][0];
                iknn_si_event = math.pow((item_d[event_item_id][21] + lambd),alpha);
                sim_io = item_d[event_item_id][24][item_id][0];
                iknn_score += event_score * (sim_io / (iknn_si_event * iknn_si));
                ms_score += event_score * item_d[event_item_id][24][item_id][1];
    if (len(u_imp_l)>0):
        for i in range(0,len(u_imp_l)):
            imp_id = u_imp_l[i];
            score = imp_d[imp_id][6];
            if (imp_d[imp_id][4] > 0):
                imp_items_d = imp_d[imp_id][5];
                for event_item_id in imp_items_d:
                    event_score = score * imp_items_d[event_item_id];
                    iknn_si_event = math.pow((item_d[event_item_id][21] + lambd), alpha);
                    sim_io = item_d[event_item_id][24][item_id][0];
                    iknn_score += event_score * (sim_io / (iknn_si_event * iknn_si));
                    ms_score += event_score * item_d[event_item_id][24][item_id][1];
    iknn_score *= w_e;
    ms_score *= w_e;
    scores_l = [iknn_score,ms_score];
    return scores_l;
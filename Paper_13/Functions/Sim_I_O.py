"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import math

#File contenente la Funzione che calcola la similarita Input Output di un item rispetto a tutti gli altri items
# Continiene le varianti RR, CC ed RC, dove R sta per impressions e C per interactions

def co_occurence_RC(v2,v1):
    co_score = 0.0;
    if (len(v1) < len(v2)):
        for user_id in v1:
            co_score += v1[user_id][1]*v2[user_id][3];
    else:
        for user_id in v2:
            co_score += v1[user_id][1]*v2[user_id][3];
    return co_score;

def co_occurence_RR(v1,v2):
    co_score = 0.0;
    if (len(v1) < len(v2)):
        for user_id in v1:
            co_score += v1[user_id][3]*v2[user_id][3];
    else:
        for user_id in v2:
            co_score += v1[user_id][3]*v2[user_id][3];
    return co_score;

def co_occurence_CC(v1,v2):
    co_score = 0.0;
    if (len(v1) < len(v2)):
        for user_id in v1:
            co_score += v1[user_id][1]*v2[user_id][1];
    else:
        for user_id in v2:
            co_score += v1[user_id][1]*v2[user_id][1];
    return co_score;

def sim_calc_RC(item_dict,per,i_id_event,i_id_current,lambd,alpha):
    s_r_it_ev = math.pow((item_dict[i_id_event][18][per][3] + lambd),alpha);
    s_r_it_cu = math.pow((item_dict[i_id_current][18][per][3] + lambd), (1.00 - alpha));
    if (len(item_dict[i_id_current][18][per][0]) > 0) \
            and (len(item_dict[i_id_event][18][per][0]) > 0):
        s_i_o = co_occurence_RC(item_dict[i_id_current][18][per][0],\
                                item_dict[i_id_event][18][per][0]);
        score = s_i_o / (s_r_it_ev * s_r_it_cu);
    else:
        score = 0.0;
    return score;

def sim_calc_CC(item_dict,per,i_id_event,i_id_current,lambd,alpha):
    s_c_it_ev = math.pow((item_dict[i_id_event][18][per][2] + lambd),alpha);
    s_c_it_cu = math.pow((item_dict[i_id_current][18][per][2] + lambd), (1.00 - alpha));
    if (len(item_dict[i_id_current][18][per][0]) > 0) \
            and (len(item_dict[i_id_event][18][per][0]) > 0):
        s_i_o = co_occurence_CC(item_dict[i_id_current][18][per][0],\
                                item_dict[i_id_event][18][per][0]);
        score = s_i_o / (s_c_it_ev * s_c_it_cu);
    else:
        score = 0.0;
    return score;

def sim_calc_RR(item_dict,per,i_id_event,i_id_current,lambd,alpha):
    s_r_it_ev = math.pow((item_dict[i_id_event][18][per][3] + lambd),alpha);
    s_r_it_cu = math.pow((item_dict[i_id_current][18][per][3] + lambd), (1.00 - alpha));
    if (len(item_dict[i_id_current][18][per][0]) > 0)\
            and (len(item_dict[i_id_event][18][per][0]) > 0):
        s_i_o = co_occurence_RR(item_dict[i_id_current][18][per][0],\
                                item_dict[i_id_event][18][per][0]);
        score = s_i_o / (s_r_it_ev * s_r_it_cu);
    else:
        score = 0.0;
    return score;
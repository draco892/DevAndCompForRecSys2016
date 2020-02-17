"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Time_Calcolation as t_c
import Interactions_type as i_t

#File contenente le funzioni riguardanti il predittore RCTR

def s_c_calculation(c,i_id,max_time,max_time_difference):
    s_c_score = float(0.0);
    c.execute('select DISTINCT user_id as id from interactions\
            where (item_id = %s) and (interaction_type = "1")' %(i_id));
    for row in c:
            last_time = i_t.user_last_int(c, row['id'], i_id);
            s_c_score = s_c_score + t_c.Time_decay(max_time, last_time, max_time_difference);
    return s_c_score;

def s_r_calculation(c,i_id,max_time,max_time_difference):
    s_r_score = float(0.0);
    c.execute('select DISTINCT imp.user_id as id from imp_items as im_t, impressions as imp\
            where (im_t.item_id = %s) and (im_t.imp_id = imp.id)'%(i_id));
    for row in c:
        last_imp_time = i_t.user_last_imp(c, row['id'], i_id);
        s_r_score = s_r_score + i_t.Positive_Impressions(max_time, max_time_difference, last_imp_time);
    return s_r_score;

def RCTR_Calculation(c, item_id,max_int_time,max_int_diff,max_imp_time,max_imp_diff):
    score = float(0.0);
    s_c = s_c_calculation(c,item_id,max_int_time,max_int_diff);
    if (s_c > 0.0):
        s_r = s_r_calculation(c,item_id,max_imp_time,max_imp_diff);
        score = s_c / s_r;
    return score;
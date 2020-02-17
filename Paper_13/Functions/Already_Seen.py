"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Interactions_type as i_t

# File contenente le funzioni riguardanti il predittore AS

def As_calculation(c, u_id, max_time, max_diff,user_item_int):
    as_score = float(0.0);
    if (len(user_item_int)>0):
        for i in range(0,len(user_item_int)):
            as_score = as_score + i_t.Positive_Interaction(c,u_id,user_item_int[i],max_time,max_diff);
    return as_score;

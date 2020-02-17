"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Time_Calcolation as t_c

# File contenente le funzioni riguardanti il predittore AP

def max_t_calculation(c):
    c.execute('select max(created_at) as max_t from items where created_at != "NULL"');
    max_t = int(0.0);
    for r in c:
        max_t = int(r['max_t']);
    return max_t;

def max_diff_calculation(c,max_t):
    c.execute('select min(created_at) as min_t from items where created_at != "NULL"');
    min_t = int(0.0);
    for r in c:
        min_t = int(r['min_t']);
    diff = max_t - min_t;
    return diff;

def Item_check_date(c,i_id,max_t):
    c.execute('select created_at as date from items where id = %s'%(i_id));
    for r in c:
        if (r['date'] == 'NULL'):
            return False;
        else:
            t = max_t - int(r['date']);
            return t;

def AP_score_par_cal(max_t,max_diff,current_t):
    Ap_score_par = float(0.0);
    for k in range(1, 7):
        Ap_score_par = Ap_score_par + ((8-k) * t_c.Time_decay(max_t,current_t+k,max_diff));
    return Ap_score_par;

def AP_calculation(max_t,max_diff,current_t):
    Ap_score_par = AP_score_par_cal(max_t,max_diff,current_t);
    Ap_score = Ap_score_par / (28.00*t_c.Time_decay(max_t,current_t,max_diff));
    return Ap_score;
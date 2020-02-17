"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

# File contenente le funzioni riguardanti il calcolo temporale riguarndanti gli eventi

def Max_T_int(c):
    c.execute('select Max(created_at) as Max_time \
                       from interactions');
    for r in c:
        max_time_int = int(r[0]);
    return max_time_int;

def Max_T_imp(c):
    c.execute('select Max(week) as Max_time\
              from impressions');
    for r in c:
        max_time_imp = int(r[0]);
    return max_time_imp;

def Min_T_int(c):
    c.execute('select Min(created_at) as Max_time \
                       from interactions');
    for r in c:
        min_time_int = int(r[0]);
    return min_time_int;

def Min_T_imp(c,year):
    c.execute('select Min(week) as Min_time\
              from impressions where year = %s'%(year));
    for r in c:
        min_time_imp = int(r[0]);
    return min_time_imp;

def Max_T_items(c):
    c.execute('select max(created_at) as max_t from items where created_at != "NULL"');
    max_t = int(0.0);
    for r in c:
        max_t = int(r['max_t']);
    return max_t;

def Min_T_items(c):
    c.execute('select min(created_at) as min_t from items where created_at != "NULL"');
    min_t = int(0);
    for r in c:
        min_t = int(r['min_t']);
    return min_t;

def Max_year_imp(c):
    c.execute('select max(year) as y from impressions');
    max_y = int(0);
    for r in c:
        max_y = int(r['y']);
    return max_y;

def Min_year_imp(c):
    c.execute('select min(year) as y from impressions');
    min_y = int(0);
    for r in c:
        min_y = int(r['y']);
    return min_y;

def time_diff(current_t,max_t):
    return max_t-current_t;

def Time_decay(t_max, t_current, diff_max):
    diff = int(t_max) - int(t_current);
    t_d = 1.00 - (float(diff / diff_max)*0.25)+0.05;
    return t_d;

def Time_decay_diff(diff_t,diff_max):
    diff_t = float(diff_t);
    diff_max = float(diff_max);
    t_d = 1.00 - ((diff_t / diff_max)*0.25)+0.05;
    return t_d;
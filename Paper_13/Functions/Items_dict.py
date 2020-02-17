"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from collections import defaultdict
import datetime
import math
from Classes import Missing_dict as m_d
import Time_Calcolation as t_c

#File contenente le funzioni riguradanti la creazione di dict rigurandanti gli items e gli scores

def Item_score_dict(c):
    c.execute('select DISTINCT id from items');
    items_upop_score_d = {};
    in_score = float(0.0)
    for r in c:
        items_upop_score_d[int(r['id'])] = in_score;
    return items_upop_score_d;

def country_dict(c):
    c.execute('select DISTINCT country as co from items');
    co_dict = {};
    value = int(1);
    for r in c:
        co_dict[r['co']] = value;
        value += 1;
    return co_dict;

def Items_N_U_latitude(c):
    n_u_l = float(0.0);
    c.execute('select max(latitude) as l from items where latitude != "NULL"');
    for r in c:
        n_u_l = float(r['l']);
    n_u_l += 1.0;
    return n_u_l;

def Items_N_U_longitude(c):
    n_u_l = float(0.0);
    c.execute('select max(longitude) as l from items where longitude != "NULL"');
    for r in c:
        n_u_l = float(r['l']);
    n_u_l += 1.0;
    return n_u_l;

def User_key_dict(c):
    c.execute('select DISTINCT id from users');
    iknn_d = defaultdict(list);
    for r in c:
        iknn_d[int(r['id'])] = [int(0),float(0.0),int(0),float(0.0),int(0),float(0.0)];
    return iknn_d;

"""
# Versione senza divisioni temporali
def Items_d_creation(c,item_min_t,item_max_t,item_max_diff,country_d,titles_l,tags_l,titles_d,\
                     tags_d,int_l,int_max_diff,imp_d):
    a = datetime.datetime.now();
    items_d = {};
    items_d_tags = {};
    items_d_titles = {};
    n_u_lat = Items_N_U_latitude(c);
    n_u_lon = Items_N_U_longitude(c);
    titles_item_d = m_d.missingdict(list);
    tags_item_d = m_d.missingdict(list);
    int_items = [];
    imp_items = [];
    c.execute('select * from items');
    for r in c:
        sim_cos_den_titles = float(0.0);
        sim_cos_den_tags = float(0.0);
        rctr_single_score = float(0.0);
        iknn_si_score = float(0.0);
        iknn_so_score = float(0.0);
        if (str(r['career_level']) == ''):
            cr_l = int(0);
        else:
            cr_l = int(r['career_level']);
        it_l = [cr_l, int(r['discipline_id']), int(r['industry_id']), \
                country_d[r['country']], int(r['region'])];
        if (str(r['latitude']) == 'NULL'):
            it_l.append(n_u_lat);
        else:
            it_l.append(float(r['latitude']));
        if (str(r['longitude']) == 'NULL'):
            it_l.append(n_u_lon);
        else:
            it_l.append(float(r['longitude']));
        it_l.append(int(r['employment']));
        if (str(r['created_at']) == 'NULL'):
            cr_at = item_min_t;
        else:
            cr_at = int(r['created_at']);
        it_l.append(cr_at);
        diff_i = t_c.time_diff(cr_at, item_max_t);
        it_l.append(diff_i);
        it_l.append(int(r['active_during_test']));
        it_l.append(titles_item_d);
        it_l.append(tags_item_d);
        r_cos_v = [int(r['industry_id']),country_d[r['country']],int(r['region']),int(r['discipline_id'])];
        it_l.append(r_cos_v);
        pop_s = t_c.Time_decay_diff(diff_i,item_max_diff)*28;
        pop_s_k = float(0.0);
        for k in range(1, 7):
            pop_s_k += (8 - k) * (t_c.Time_decay_diff((diff_i + k), item_max_diff));
        AP_score = pop_s_k/pop_s;
        it_l.append(AP_score);
        it_l.append(sim_cos_den_titles);
        it_l.append(sim_cos_den_tags);
        users_si_so_scores = defaultdict(lambda: [int(0),float(0.0),int(0),float(0.0),int(0),float(0.0)]);
        it_l.append(users_si_so_scores);
        it_l.append(rctr_single_score);
        it_l.append(iknn_si_score);
        sim_cos_den_score = 0.0;
        for i in range(0,len(r_cos_v)):
            sim_cos_den_score +=  math.pow(r_cos_v[i],2);
        sim_cos_den_score = math.sqrt(sim_cos_den_score);
        it_l.append(sim_cos_den_score);
        it_l.append(iknn_so_score);
        items_d[int(r['id'])] = it_l;
        items_d_titles[int(r['id'])] = m_d.missingdict(list);
        items_d_tags[int(r['id'])] = m_d.missingdict(list);

    # titles
    print "\t\ttitles";
    for i in range(0, len(titles_l)):
        item_id = titles_l[i][0];
        title_id = titles_l[i][1];
        items_d_titles[item_id][title_id] = titles_d[title_id][2];
        items_d[item_id][11][title_id] = titles_d[title_id][2];
    #print items_d_titles[2828770];
    #print items_d[2828770][11];

    # tags
    print "\t\ttags";
    for i in range(0, len(tags_l)):
        item_id = tags_l[i][0];
        tags_id = tags_l[i][1];
        items_d_tags[item_id][tags_id] = tags_d[tags_id][2];

    # interactions
    print "\t\tinteractions"
    contr = len(int_l) / 4;
    perc = 25;
    ccc = 1;
    for i in range(0,len(int_l)):
        user_id = int_l[i][0];
        item_id = int_l[i][1];
        int_type = int_l[i][2];
        created_at = int_l[i][3];
        diff_t = int_l[i][4];
        score = t_c.Time_decay_diff(diff_t, int_max_diff);
        if item_id not in int_items:
            int_items.append(item_id);
        if (items_d[item_id][17][user_id][0] < created_at):
            items_d[item_id][17][user_id][0] = created_at;
            items_d[item_id][17][user_id][1] = score;
        if (items_d[item_id][17][user_id][4] < created_at) and (int_type == 1):
            items_d[item_id][17][user_id][4] = created_at;
            items_d[item_id][17][user_id][5] = score;
        if (ccc%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;
        ccc += 1;
    #print "Items_d[2828770]:";
    #print items_d[2828770][17];

    # impressions
    contr = len(imp_d)/10;
    perc = 10;
    ccc = 1;
    print "\t\timpressions";
    for imp_id in imp_d:
        user_id = imp_d[imp_id][0];
        created_at = (imp_d[imp_id][1]*52)+(imp_d[imp_id][2])
        nr_items = imp_d[imp_id][4];
        score_s_imp = imp_d[imp_id][6];
        if (nr_items > 0):
            imp_items_d = imp_d[imp_id][5];
            for item_id in imp_items_d:
                if (item_id not in imp_items):
                    imp_items.append(item_id);
                if (items_d[item_id][17][user_id][2] < created_at):
                    items_d[item_id][17][user_id][2] = created_at;
                    items_d[item_id][17][user_id][3] = score_s_imp;
        if (ccc%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 10;
        ccc += 1;

    # calcolo valori fissi
    print "\t\tcalcolo valori fissi:";
    print "\t\tparte 1";
    for item_id in items_d:
        #titles
        items_d[item_id][11] = items_d_titles[item_id];
        if len(items_d[item_id][11]) > 0:
            tf = 1.0/len(items_d[item_id][11]);
            for title_id in items_d[item_id][11]:
                items_d[item_id][11][title_id] *= tf;
                items_d[item_id][15] += math.pow(items_d[item_id][11][title_id],2);
            items_d[item_id][15] = math.sqrt(items_d[item_id][15]);
        #tags
        items_d[item_id][12] = items_d_tags[item_id];
        if len(items_d[item_id][12]) > 0:
            tf = 1.0/len(items_d[item_id][12]);
            for tags_id in items_d[item_id][12]:
                items_d[item_id][12][tags_id] *= tf;
                items_d[item_id][16] += math.pow(items_d[item_id][12][tags_id], 2);
            items_d[item_id][16] = math.sqrt(items_d[item_id][16]);
    print "\t\t\tparte 2";
    if (len(int_items)>0):
        for i in range(0,len(int_items)):
            item_id = int_items[i];
            sum_last_cl_ev = float(0.0);
            sum_last_imp_ev = float(0.0);
            iknn_si_sc = float(0.0);
            #sommatorie users
            for user_id in items_d[item_id][17]:
                sum_last_cl_ev += items_d[item_id][17][user_id][5];
                sum_last_imp_ev += items_d[item_id][17][user_id][3];
                iknn_si_sc += items_d[item_id][17][user_id][1];
            items_d[item_id][19] = iknn_si_sc;
            if (sum_last_imp_ev > 0) and (sum_last_cl_ev > 0):
                items_d[item_id][18] = sum_last_cl_ev/sum_last_imp_ev;
    print "\t\t\tparte 3";
    if ((len(imp_items)) > 0):
        for i in range(0,len(imp_items)):
            item_id = imp_items[i];
            iknn_so_sc = float(0.0);
            for user_id in items_d[item_id][17]:
                iknn_so_sc += items_d[item_id][17][user_id][3];
            items_d[item_id][21] = iknn_so_sc;

    b = datetime.datetime.now();
    print (b-a);
    return items_d;
"""

# Versione con divisione temporale
def Items_d_creation(c,item_min_t,item_max_t,item_max_diff,country_d,titles_l,tags_l,titles_d,\
                     tags_d,int_l,int_max_diff,imp_d,int_periods_t_lim_v,imp_periods_t_lim_v):
    a = datetime.datetime.now();
    items_d = {};
    items_d_tags = {};
    items_d_titles = {};
    n_u_lat = Items_N_U_latitude(c);
    n_u_lon = Items_N_U_longitude(c);
    titles_item_d = m_d.missingdict(list);
    tags_item_d = m_d.missingdict(list);
    int_items = [];
    imp_items = [];
    c.execute('select * from items');
    for r in c:
        sim_cos_den_titles = float(0.0);
        sim_cos_den_tags = float(0.0);
        rctr_single_score = float(0.0);
        iknn_si_score = float(0.0);
        iknn_so_score = float(0.0);

        users_si_so_scores = defaultdict(lambda: [int(0), float(0.0), int(0), float(0.0), int(0), float(0.0)]);
        periods_d = {};
        for i in range(1, 7):
            periods_d[i] = [users_si_so_scores.copy(), rctr_single_score, iknn_si_score, iknn_so_score];

        if (str(r['career_level']) == ''):
            cr_l = int(0);
        else:
            cr_l = int(r['career_level']);
        it_l = [cr_l, int(r['discipline_id']), int(r['industry_id']), \
                country_d[r['country']], int(r['region'])];
        if (str(r['latitude']) == 'NULL'):
            it_l.append(n_u_lat);
        else:
            it_l.append(float(r['latitude']));
        if (str(r['longitude']) == 'NULL'):
            it_l.append(n_u_lon);
        else:
            it_l.append(float(r['longitude']));
        it_l.append(int(r['employment']));
        if (str(r['created_at']) == 'NULL'):
            cr_at = item_min_t;
        else:
            cr_at = int(r['created_at']);
        it_l.append(cr_at);
        diff_i = t_c.time_diff(cr_at, item_max_t);
        it_l.append(diff_i);
        it_l.append(int(r['active_during_test']));
        it_l.append(titles_item_d);
        it_l.append(tags_item_d);
        r_cos_v = [int(r['industry_id']),country_d[r['country']],int(r['region']),int(r['discipline_id'])];
        it_l.append(r_cos_v);
        pop_s = t_c.Time_decay_diff(diff_i,item_max_diff)*28;
        pop_s_k = float(0.0);
        for k in range(1, 7):
            pop_s_k += (8 - k) * (t_c.Time_decay_diff((diff_i + k), item_max_diff));
        AP_score = pop_s_k/pop_s;
        it_l.append(AP_score);
        it_l.append(sim_cos_den_titles);
        it_l.append(sim_cos_den_tags);
        sim_cos_den_score = 0.0;
        for i in range(0, len(r_cos_v)):
            sim_cos_den_score += math.pow(r_cos_v[i], 2);
        sim_cos_den_score = math.sqrt(sim_cos_den_score);
        it_l.append(sim_cos_den_score);
        it_l.append(periods_d);
        items_d[int(r['id'])] = it_l;
        items_d_titles[int(r['id'])] = m_d.missingdict(list);
        items_d_tags[int(r['id'])] = m_d.missingdict(list);

    # titles
    print "\t\ttitles";
    for i in range(0, len(titles_l)):
        item_id = titles_l[i][0];
        title_id = titles_l[i][1];
        items_d_titles[item_id][title_id] = titles_d[title_id][2];
        items_d[item_id][11][title_id] = titles_d[title_id][2];
    #print items_d_titles[2828770];
    #print items_d[2828770][11];

    # tags
    print "\t\ttags";
    for i in range(0, len(tags_l)):
        item_id = tags_l[i][0];
        tags_id = tags_l[i][1];
        items_d_tags[item_id][tags_id] = tags_d[tags_id][2];

    #interactions
    print "\t\tinteractions"
    contr = len(int_l) / 4;
    perc = 25;
    ccc = 1;
    for i in range(0, len(int_l)):
        user_id = int_l[i][0];
        item_id = int_l[i][1];
        int_type = int_l[i][2];
        created_at = int_l[i][3];
        diff_t = int_l[i][4];
        score = t_c.Time_decay_diff(diff_t, int_max_diff);
        if (created_at < int_periods_t_lim_v[1]):
            period = 1;
        elif (int_periods_t_lim_v[1] <= created_at < int_periods_t_lim_v[2]):
            period = 2;
        elif (int_periods_t_lim_v[2] <= created_at < int_periods_t_lim_v[3]):
            period = 3;
        elif (int_periods_t_lim_v[3] <= created_at < int_periods_t_lim_v[4]):
            period = 4;
        elif (int_periods_t_lim_v[4] <= created_at < int_periods_t_lim_v[5]):
            period = 5;
        else: period = 6;
        if item_id not in int_items:
            int_items.append(item_id);
        for j in range(period,7):
            if (items_d[item_id][18][j][0][user_id][0] < created_at):
                items_d[item_id][18][j][0][user_id][0] = created_at;
                items_d[item_id][18][j][0][user_id][1] = score;
            if (items_d[item_id][18][j][0][user_id][4] < created_at) and (int_type == 1):
                items_d[item_id][18][j][0][user_id][4] = created_at;
                items_d[item_id][18][j][0][user_id][5] = score;
        if (ccc % contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;
        ccc += 1;
    #print "Items_d[2828770]:";
    #print items_d[2828770][18][6][0];
    #print len(items_d[2828770][18][6][0]);
    #for i in range(1,7):
        #print "period " + str(i) + ":";
        #print len(items_d[2828770][18][i][0]);
        #print items_d[2828770][18][i][0];
        #print "\n";

    # impressions
    contr = len(imp_d) / 10;
    perc = 10;
    ccc = 1;
    print "\t\timpressions";
    for imp_id in imp_d:
        user_id = imp_d[imp_id][0];
        created_at = (imp_d[imp_id][1] * 52) + (imp_d[imp_id][2])
        nr_items = imp_d[imp_id][4];
        score_s_imp = imp_d[imp_id][6];
        imp_week = imp_d[imp_id][2];
        if (imp_week < imp_periods_t_lim_v[1]):
            period = 1;
        elif (imp_periods_t_lim_v[1] <= imp_week < imp_periods_t_lim_v[2]):
            period = 2;
        elif (imp_periods_t_lim_v[2] <= imp_week < imp_periods_t_lim_v[3]):
            period = 3;
        elif (imp_periods_t_lim_v[3] <= imp_week < imp_periods_t_lim_v[4]):
            period = 4;
        elif (imp_periods_t_lim_v[4] <= imp_week < imp_periods_t_lim_v[5]):
            period = 5;
        else: period = 6;
        #print imp_week;
        #print period;
        if (nr_items > 0):
            imp_items_d = imp_d[imp_id][5];
            for item_id in imp_items_d:
                if (item_id not in imp_items):
                    imp_items.append(item_id);
                for i in range(period,7):
                    if (items_d[item_id][18][i][0][user_id][0] < imp_week):
                        items_d[item_id][18][i][0][user_id][4] = imp_week;
                        items_d[item_id][18][i][0][user_id][5] = score_s_imp;
        if (ccc % contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 10;
        ccc += 1;

    # calcolo valori fissi
    print "\t\tcalcolo valori fissi:";
    print "\t\t\tparte 1";
    for item_id in items_d:
        # titles
        items_d[item_id][11] = items_d_titles[item_id];
        if len(items_d[item_id][11]) > 0:
            tf = 1.0 / len(items_d[item_id][11]);
            for title_id in items_d[item_id][11]:
                items_d[item_id][11][title_id] *= tf;
                items_d[item_id][15] += math.pow(items_d[item_id][11][title_id], 2);
            items_d[item_id][15] = math.sqrt(items_d[item_id][15]);
        # tags
        items_d[item_id][12] = items_d_tags[item_id];
        if len(items_d[item_id][12]) > 0:
            tf = 1.0 / len(items_d[item_id][12]);
            for tags_id in items_d[item_id][12]:
                items_d[item_id][12][tags_id] *= tf;
                items_d[item_id][16] += math.pow(items_d[item_id][12][tags_id], 2);
            items_d[item_id][16] = math.sqrt(items_d[item_id][16]);
    print "\t\t\tparte 2";
    if (len(int_items) > 0):
        for i in range(0, len(int_items)):
            item_id = int_items[i];
            for j in range(1,7):
                sum_last_cl_ev = float(0.0);
                sum_last_imp_ev = float(0.0);
                iknn_si_sc = float(0.0);
                # sommatorie users
                if len(items_d[item_id][18][j][0]) > 0:
                    for user_id in items_d[item_id][18][j][0]:
                        sum_last_cl_ev += items_d[item_id][18][j][0][user_id][5];
                        sum_last_imp_ev += items_d[item_id][18][j][0][user_id][3];
                        iknn_si_sc += items_d[item_id][18][j][0][user_id][1];
                items_d[item_id][18][j][2] = iknn_si_sc;
                if (sum_last_imp_ev > 0) and (sum_last_cl_ev > 0):
                    items_d[item_id][18][j][1] = sum_last_cl_ev / sum_last_imp_ev;
    print "\t\t\tparte 3";
    if ((len(imp_items)) > 0):
        for i in range(0, len(imp_items)):
            item_id = imp_items[i];
            for j in range(1, 7):
                iknn_so_sc = float(0.0);
                if len(items_d[item_id][18][j][0]) > 0:
                    for user_id in items_d[item_id][18][j][0]:
                        iknn_so_sc += items_d[item_id][18][j][0][user_id][3];
                    items_d[item_id][18][j][3] = iknn_so_sc;

    b = datetime.datetime.now();
    print (b - a);
    return items_d;
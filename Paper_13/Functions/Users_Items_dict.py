"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import datetime
import math
from collections import defaultdict
from Classes import Missing_dict as m_d
import Time_Calcolation as t_c
import Sim_I_O as s_io
import Meta_Cosine as m_c


#File contenente le funzioni riguardanti la creazione dei dict degli users, items, iteractions,
# impressions,fos e jobroles


def country_dict(c):
    c.execute('select DISTINCT country as co from items');
    co_dict = {};
    value = int(1);
    for r in c:
        co_dict[r['co']] = value;
        value += 1;
    return co_dict;

def common_elements(list1, list2):
    return list(set(list1) & set(list2));

def users_d_creation(c,country_d,fos_d,fos_l,jobroles_d,jobroles_l,int_l,imp_d,int_diff_max,imp_diff_max,item_d):
    a = datetime.datetime.now();
    users_d = defaultdict(list);
    i = int(1);
    perc = int(5);
    fos = [];
    jobroles = [];
    u_int_d = defaultdict(list);
    u_imp_l = [];
    nr_fos = int(0);
    nr_jobroles = int(0);
    nr_groups = int(0);
    w_e = float(0.0);
    RCTR = float(0.0);
    AS_score = float(0.0);
    c.execute('select * from users');
    for r in c:
        u_id = int(r['id']);
        if (str(r['career_level'])=='NULL'):
            career_level = int(0);
        else:
            career_level = int(r['career_level']);
        discipline_id = int(r['discipline_id']);
        industry_id = int(r['industry_id']);
        country = country_d[r['country']];
        region = int(r['region']);
        if (str(r['experience_n_entries_class']) == 'NULL'):
            experience_n_entries_class = int(0);
        else:
            experience_n_entries_class = int(r['experience_n_entries_class']);
        if (str(r['experience_years_experience']) == 'NULL'):
            experience_years_experience = int(0);
        else:
            experience_years_experience = int(r['experience_years_experience']);
        if (str(r['experience_years_in_current']) == 'NULL'):
            experience_years_in_current = int(0);
        else:
            experience_years_in_current = int(r['experience_years_in_current']);
        edu_degree = int(r['edu_degree']);
        l_par = [career_level,discipline_id,industry_id,country,region,experience_n_entries_class,\
                 experience_years_experience,experience_years_in_current,edu_degree,fos,jobroles,\
                 nr_fos,nr_jobroles,nr_groups,u_int_d,u_imp_l,w_e,RCTR,AS_score];
        users_d[u_id] = l_par;
    print "\t\tfos"
    if (len(fos_l)>0):
        for i in range(0,len(fos_l)):
            user_id = fos_l[i][0];
            fos_id = fos_l[i][1];
            users_d[user_id][9].append(fos_id);
            users_d[user_id][11] += 1;
            users_d[user_id][13] += 1;
    print "\t\tjobroles"
    if (len(jobroles_l)>0):
        for i in range(0,len(jobroles_l)):
            user_id = jobroles_l[i][0];
            jbrl_id = jobroles_l[i][1];
            users_d[user_id][10].append(jbrl_id);
            users_d[user_id][12] += 1;
            users_d[user_id][13] += 1;
    print "\t\tinteractions"
    if (len(int_l)>0):
        for i in range(0,len(int_l)):
            user_id = int_l[i][0];
            item_id = int_l[i][1];
            type = int_l[i][2];
            created_at = int_l[i][3];
            diff_t = int_l[i][4];
            score = t_c.Time_decay_diff(diff_t,int_diff_max);
            l_par = [item_id,created_at,diff_t,score];
            users_d[user_id][14][type].append(l_par);
            par_we = score;
            users_d[user_id][16] += par_we;
            users_d[user_id][18] += par_we;
            if type == 1:
                users_d[user_id][17] += item_d[item_id][31];
            #print item_id;
            if (users_d[user_id][11] > 0):
                for key in users_d[user_id][9]:
                    fos_id = key;
                    fos_d[fos_id][2][item_id] += par_we;
            if (users_d[user_id][12] > 0):
                for key in users_d[user_id][10]:
                    jbrl_id = key;
                    jobroles_d[jbrl_id][2][item_id] += par_we;
    print "\t\timpressions"
    if (len(imp_d)>0):
        contr = len(imp_d)/50;
        perc = 2;
        i = 0;
        for key in imp_d:
            imp_id = key;
            user_id = imp_d[imp_id][0];
            nr_items = imp_d[imp_id][4];
            items = imp_d[imp_id][5];
            par_we = imp_d[imp_id][6];
            if nr_items > 0:
                users_d[user_id][15].append(imp_id);
                users_d[user_id][16] += par_we*nr_items;
                for item_id in items:
                    nr_times = items[item_id];
                    if (users_d[user_id][11] > 0):
                        for fos_id in users_d[user_id][9]:
                            fos_d[fos_id][2][item_id] += par_we * nr_times;
                    if (users_d[user_id][12] > 0):
                        for jbrl_id in users_d[user_id][10]:
                            jobroles_d[jbrl_id][2][item_id] += par_we * nr_times;
            #i += 1;
            #if (i%contr)==0:
                #print "\t\t\t" + str(perc) + "%";
                #perc += 2;
    print "\t\tcalcoli"
    for user_id in users_d:
        if users_d[user_id][16] > 0:
            users_d[user_id][16] = float(1.00/users_d[user_id][16]);
        else:
            users_d[user_id][16] = 0.0;
        if users_d[user_id][13]>0:
            users_d[user_id][13] = float(1.00/users_d[user_id][13]);
    b = datetime.datetime.now();
    #print (b-a);
    return users_d;

def Items_N_U_latitude(c):
    n_u_l = float(0.0);
    c.execute('select max(latitude) as l from items where latitude != "NULL"');
    for r in c:
        n_u_l = float(r['l']);
    n_u_l += float(1.0);
    return n_u_l;

def Items_N_U_longitude(c):
    n_u_l = float(0.0);
    c.execute('select max(longitude) as l from items where longitude != "NULL"');
    for r in c:
        n_u_l = float(r['l']);
    n_u_l += float(1.0);
    return n_u_l;

def User_key_dict(c):
    c.execute('select DISTINCT id from users');
    iknn_d = defaultdict(list);
    for r in c:
        iknn_d[int(r['id'])] = [int(0),float(0.0)];
    return iknn_d;

def Items_keys_dict(c):
    c.execute('select DISTINCT id from items');
    sim_scores = {};
    for r in c:
        sim_scores[int(r['id'])] = [float(0.0),float(1.0),int(0)];
    return sim_scores;

def items_d_creation(c,country_d,min_t,max_t,diff_max_t,int_l,imp_d,titles_d,tags_d,int_diff_max,imp_diff_max):
    a = datetime.datetime.now();
    items_d = defaultdict(list);
    n_u_lat = Items_N_U_latitude(c);
    n_u_lon = Items_N_U_longitude(c);
    titles_item_d = [];
    tags_item_d = [];
    int_item_d = defaultdict(list);
    iknn_si_d = User_key_dict(c);
    iknn_so_d = iknn_si_d;
    RCTR_cl_d = iknn_si_d;
    imp_item_l = [];
    ms_title_d = m_d.missingdict(list);
    ms_tags_d = m_d.missingdict(list);
    sim_scores = Items_keys_dict(c);
    iknn_si = float(0.0);
    sim_cos_den_titles = float(0.0);
    sim_cos_den_tags = float(0.0);
    int_items_l = [];
    imp_items_l = [];
    sum_last_cl_ev = float(0.0);
    sum_last_imp_ev = float(0.0);
    rtct_single_score = float(0.0);
    c.execute('select * from items');
    for r in c:
        if (str(r['career_level']) == ''):
            cr_l = int(0);
        else:
            cr_l = int(r['career_level']);
        it_l = [cr_l,int(r['discipline_id']),int(r['industry_id']),\
                country_d[r['country']],int(r['region'])];
        if (str(r['latitude']) == 'NULL'):
            it_l.append(n_u_lat);
        else:
            it_l.append(float(r['latitude']));
        if (str(r['longitude']) == 'NULL'):
            it_l.append(n_u_lon);
        else:
            it_l.append(float(r['longitude']));
        it_l.append(int(r['employment']));
        if(str(r['created_at']) == 'NULL'):
            cr_at = min_t;
        else:
            cr_at = int(r['created_at']);
        it_l.append(cr_at);
        diff_i = t_c.time_diff(cr_at,max_t);
        it_l.append(diff_i);
        it_l.append(int(r['active_during_test']));
        it_l.append(titles_item_d);
        it_l.append(tags_item_d);
        it_l.append(int_item_d);
        it_l.append(imp_item_l);
        pop_s = t_c.Time_decay_diff(diff_i,diff_max_t)*28;
        it_l.append(pop_s)
        pop_s_k = float(0.0);
        for k in range(1,7):
            pop_s_k += (8-k)*(t_c.Time_decay_diff((diff_i + k),diff_max_t));
        it_l.append(pop_s_k);
        AP_score = pop_s_k/pop_s;
        it_l.append(AP_score);
        it_l.append(ms_title_d);
        it_l.append(ms_tags_d);
        ms_rest_v = [int(r['industry_id']),country_d[r['country']],int(r['region']),int(r['discipline_id'])];
        sim_cos_den_rest = float(int(r['industry_id']) + country_d[r['country']] +\
                                 int(r['region']) + int(r['discipline_id']));
        it_l.append(ms_rest_v);
        it_l.append(iknn_si);
        it_l.append(iknn_si_d);
        it_l.append(iknn_so_d);
        it_l.append(sim_scores);
        it_l.append(sim_cos_den_titles);
        it_l.append(sim_cos_den_tags);
        it_l.append(sim_cos_den_rest);
        it_l.append(RCTR_cl_d);
        it_l.append(sum_last_cl_ev);
        it_l.append(sum_last_imp_ev);
        it_l.append(rtct_single_score);
        items_d[int(r['id'])] = it_l;
    #print "titles";
    for key in titles_d:
        if (len(titles_d[key][1]) > 0):
            for i in range(0, len(titles_d[key][1])):
                items_d[titles_d[key][1][i]][11].append(key);
                items_d[titles_d[key][1][i]][18][key] = 1;
                items_d[titles_d[key][1][i]][25] += 1;
    #print "tags";
    for key in tags_d:
        if (len(tags_d[key][1]) > 0):
            for i in range(0, len(tags_d[key][1])):
                items_d[tags_d[key][1][i]][12].append(key);
                items_d[tags_d[key][1][i]][19][key] = 1;
                items_d[tags_d[key][1][i]][26] += 1;
    #print "interactions";
    if (len(int_l)>0):
        for i in range(0,len(int_l)):
            user_id = int_l[i][0];
            item_id = int_l[i][1];
            type = int_l[i][2];
            created_at = int_l[i][3];
            diff_t = int_l[i][4];
            score = t_c.Time_decay_diff(diff_t,int_diff_max);
            l_par = [user_id,created_at,diff_t,score];
            items_d[item_id][13][type].append(l_par);
            temp_time = items_d[item_id][22][user_id][0];
            temp_time_clicks = items_d[item_id][28][user_id][0];
            if (created_at > temp_time):
                items_d[item_id][22][user_id][0] = created_at;
                items_d[item_id][22][user_id][1] = score;
            if (item_id not in int_items_l):
                int_items_l.append(item_id);
            if type == 1:
                if (created_at > temp_time_clicks):
                    items_d[item_id][28][user_id][0] = created_at;
                    items_d[item_id][28][user_id][1] = score;
    #print "Impressions";
    if (len(imp_d)>0):
        for key in imp_d:
            imp_id = key
            s_imp_items_d = imp_d[imp_id][5];
            user_id = imp_d[imp_id][0];
            created_at = imp_d[imp_id][2];
            diff_t = imp_d[imp_id][3];
            score = imp_d[imp_id][6];
            if (len(s_imp_items_d)>0):
                for k2 in s_imp_items_d:
                    item_id = k2;
                    items_d[item_id][14].append(imp_id);
                    temp_time = items_d[item_id][23][user_id][0];
                    if (created_at > temp_time):
                        items_d[item_id][23][user_id][0] = created_at;
                        items_d[item_id][23][user_id][1] = score;
                    if (item_id not in imp_items_l):
                        imp_items_l.append(item_id);
    #print "\t\tNr_int_items:\t" + str(len(int_items_l));
    #print "\t\tNr_imp_items:\t" + str(len(imp_items_l));
    for item_id in items_d:
        if (items_d[item_id][25] > 0):
            items_d[item_id][25] = math.sqrt(items_d[item_id][25]);
        if (items_d[item_id][26] > 0):
            items_d[item_id][26] = math.sqrt(items_d[item_id][26]);
        if (items_d[item_id][27] > 0):
            items_d[item_id][27] = math.sqrt(items_d[item_id][27]);
        for user_id in items_d[item_id][22]:
            items_d[item_id][21] += items_d[item_id][22][user_id][1];
            items_d[item_id][29] += items_d[item_id][28][user_id][1];
            items_d[item_id][30] += items_d[item_id][23][user_id][1];
        if (items_d[item_id][29]>0) and (items_d[item_id][30]>0):
            items_d[item_id][31] = items_d[item_id][29]/items_d[item_id][30];
    """
    # s_i_o score
    d = datetime.datetime.now();
    #print "\t\ts_i_o score";
    for i in range(0,len(int_items_l)):
        x = datetime.datetime.now();
        item_id_1 = int_items_l[i]
        print "\t\t\t" + str(item_id_1);
        for j in range(0,len(imp_items_l)):
            t = datetime.datetime.now();
            item_id_2 = imp_items_l[j];
            if item_id_1 != item_id_2:
                items_d[item_id_1][24][item_id_2][0] += s_io.co_occurrence_calc(items_d[item_id_1][22],\
                                                                                items_d[item_id_2][23]);
            r = datetime.datetime.now();
            print "\t\t\t\t" + str(r-t);
        z = datetime.datetime.now();
        print "\t\t\t" + str(z-x);
        print
    e = datetime.datetime.now();
    print (e-d);
    """
    """
    # cosine sim
    a = datetime.datetime.now();
    #print "\t\tcosine sim";
    for item_id in items_d:
        print "\t\t\t" + str(item_id);
        d = datetime.datetime.now();
        for item_id_2 in items_d:
            if (items_d[item_id][24][item_id_2][3] == 0) and (item_id != item_id_2):
                x = datetime.datetime.now();
                items_d[item_id][24][item_id_2][1] = 0.0;
                if (items_d[item_id][25] > 0) and (items_d[item_id_2][25] > 0):
                    score = m_c.cosine_similarity_dict(items_d[item_id][18],items_d[item_id_2][18],\
                                                        items_d[item_id][25],items_d[item_id_2][25]);
                    items_d[item_id][24][item_id_2][1] += score;
                if (items_d[item_id][26] > 0) and (items_d[item_id_2][26] > 0):
                    score = m_c.cosine_similarity_dict(items_d[item_id][19],items_d[item_id_2][19],\
                                                       items_d[item_id][26],items_d[item_id_2][26]);
                    items_d[item_id][24][item_id_2][1] += score;
                if (items_d[item_id][27] > 0) and (items_d[item_id_2][27] > 0):
                    score = m_c.cosine_similarity_vector(items_d[item_id][20],items_d[item_id_2][20],\
                                                         items_d[item_id][27],items_d[item_id_2][27]);
                    items_d[item_id][24][item_id_2][1] += score;
                items_d[item_id_2][24][item_id][1] = items_d[item_id][24][item_id_2][1];
                items_d[item_id][24][item_id_2][2] = 1;
                items_d[item_id_2][24][item_id][2] = 1;
                y = datetime.datetime.now();
                print "\t\t\t\t" + str(y-x);
            e = datetime.datetime.now();
        print (e-d);
    """
    b = datetime.datetime.now();
    #print (b-a);
    return items_d;

def Groups_items_upop_d(c):
    c.execute('select DISTINCT id from items');
    items_upop_score_d = {};
    in_score = float(0.0)
    for r in c:
        items_upop_score_d[int(r['id'])] = in_score;
    return items_upop_score_d;

def Jobroles_Dist_list(c):
    c.execute('select DISTINCT jobrole as jb from us_jobroles');
    job_roles_l = [];
    for r in c:
        job_roles_l.append(int(r['jb']));
    return job_roles_l;

def Jobroles_list(c):
    c.execute('select * from us_jobroles');
    jbr_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['user_id']));
        l_par.append(int(r['jobrole']));
        jbr_l.append(l_par);
    return jbr_l;

def jobroles_d_creation(c,jbr_l,items_upop_score_d):
    #print "Inizio calcolo Jobroles";
    a = datetime.datetime.now();
    jobroles_d = {};
    jbr_d_l = Jobroles_Dist_list(c);
    if (len(jbr_d_l)>0):
        for i in range(0,len(jbr_d_l)):
            jobroles_d[jbr_d_l[i]] = [int(0),[],items_upop_score_d];
    if (len(jbr_l)>0):
        for i in range(0,len(jbr_l)):
            if jbr_l[i][0] not in jobroles_d[jbr_l[i][1]][1]:
                jobroles_d[jbr_l[i][1]][0] += 1;
                l = jobroles_d[jbr_l[i][1]][1];
                l.append(jbr_l[i][0]);
                jobroles_d[jbr_l[i][1]][1] = l;
    for key in jobroles_d:
        if (jobroles_d[key][0]>0):
            jobroles_d[key][0] = float(1.00/jobroles_d[key][0]);
    b = datetime.datetime.now();
    #print "Fine calcolo Jobroles";
    #print (b-a);
    return jobroles_d;

def Fos_Dist_list(c):
    c.execute('select DISTINCT fos as f from us_fos');
    f_l = [];
    for r in c:
        f_l.append(int(r['f']));
    return f_l;

def Fos_list(c):
    c.execute('select * from us_fos');
    fos_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['user_id']));
        l_par.append(int(r['fos']));
        fos_l.append(l_par);
    return fos_l;

def fos_d_creation(c,fos_l,items_upop_score_d):
    #print "Inizio calcolo Fos";
    a = datetime.datetime.now();
    fos_d = {};
    fos_di_l = Fos_Dist_list(c);
    if (len(fos_di_l)>0):
        for i in range(0,len(fos_di_l)):
            fos_d[fos_di_l[i]] = [int(0),[],items_upop_score_d];
    if (len(fos_l)>0):
        for i in range(0,len(fos_l)):
            if fos_l[i][0] not in fos_d[fos_l[i][1]][1]:
                fos_d[fos_l[i][1]][0] += 1;
                l = fos_d[fos_l[i][1]][1];
                l.append(fos_l[i][0]);
                fos_d[fos_l[i][1]][1] = l;
    for key in fos_d:
        if (fos_d[key][0]>0):
            fos_d[key][0] = float(1.00/fos_d[key][0]);
    b = datetime.datetime.now();
    #print "Fine calcolo Fos";
    #print (b - a);
    return fos_d;

def Tag_Not_used(c):
    c.execute('select max(tag) as t from it_tags where tag != ""');
    n_u_t = int(0);
    for r in c:
        n_u_t = int(r['t']);
    n_u_t += 1;
    return n_u_t;

def Tags_Dist_list(c,n_u_t):
    c.execute('select DISTINCT tag as t from it_tags');
    t_l = [];
    for r in c:
        if (str(r['t']) != ''):
            t_l.append(int(r['t']));
    t_l.append(n_u_t);
    return t_l;

def Tags_list(c,n_u_t):
    c.execute('select * from it_tags');
    tags_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['item_id']));
        if (str(r['tag']) == ''):
            l_par.append(n_u_t);
        else:
            l_par.append(int(r['tag']));
        tags_l.append(l_par);
    return tags_l;

def tags_d_creation(c,tags_l,n_u_t):
    #print "Inizio calcolo Tags";
    a = datetime.datetime.now();
    tags_d = {};
    tags_di_l = Tags_Dist_list(c,n_u_t);
    if (len(tags_di_l)>0):
        for i in range(0,len(tags_di_l)):
            tags_d[tags_di_l[i]] = [int(0),[]];
    if (len(tags_l)>0):
        for i in range(0,len(tags_l)):
            if tags_l[i][0] not in tags_d[tags_l[i][1]][1]:
                tags_d[tags_l[i][1]][0] += 1;
                l = tags_d[tags_l[i][1]][1];
                l.append(tags_l[i][0]);
                tags_d[tags_l[i][1]][1] = l;
    b = datetime.datetime.now();
    #print "Fine calcolo Tags";
    #print (b - a);
    return tags_d;

def Title_Not_used(c):
    c.execute('select max(title) as t from it_titles where title != ""');
    n_u_t = int(0);
    for r in c:
        n_u_t = int(r['t']);
    n_u_t += 1;
    return n_u_t;

def Titles_Dist_list(c,n_u_t):
    c.execute('select DISTINCT title as t from it_titles');
    t_l = [];
    for r in c:
        if (str(r['t']) != ''):
            t_l.append(int(r['t']));
    t_l.append(int(0));
    return t_l;

def Titles_list(c,n_u_t):
    c.execute('select * from it_titles');
    titles_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['item_id']));
        if (str(r['title']) == ''):
            l_par.append(int(0));
        else:
            l_par.append(int(r['title']));
        titles_l.append(l_par);
    #print titles_l;
    return titles_l;

def titles_d_creation(c,titles_l,n_u_t):
    #print "Inizio calcolo Titles";
    a = datetime.datetime.now();
    titles_d = {};
    t_di_l = Titles_Dist_list(c,n_u_t);
    if (len(t_di_l)>0):
        for i in range(0,len(t_di_l)):
            titles_d[t_di_l[i]] = [int(0),[]];
    if (len(titles_l)>0):
        for i in range(0,len(titles_l)):
            if titles_l[i][0] not in titles_d[titles_l[i][1]][1]:
                titles_d[titles_l[i][1]][0] += 1;
                l = titles_d[titles_l[i][1]][1];
                l.append(titles_l[i][0]);
                titles_d[titles_l[i][1]][1] = l;
    b = datetime.datetime.now();
    #print "Fine calcolo Titles";
    #print (b - a);
    return titles_d;

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
        single_imp_score = t_c.Time_decay_diff(diff_t,max_imp_diff);
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
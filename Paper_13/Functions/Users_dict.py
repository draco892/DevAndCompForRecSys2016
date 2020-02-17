"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import datetime
import Time_Calcolation as t_c

#File contenente la funzione riguardante la creazione del users dict

"""
def Users_d_creation(c,country_d,fos_l,jbrl_l,fos_d,jobroles_d,int_max_diff,int_l,imp_d,items_d,int_periods_t_lim_v):
    a = datetime.datetime.now();
    users_d = {};
    u_int_d = {};
    u_int_type_d = {};
    for i in range(1, 5):
        u_int_type_d[i] = [];
    for i in range(1, 7):
        u_int_d[i] = u_int_type_d.copy();
    c.execute('select * from users');
    for r in c:
        fos = [];
        jobroles = [];
        nr_groups = int(0);
        u_int_l = u_int_d.copy();
        #u_int_l = [];
        u_imp_l = [];
        w_e = float(0.0);
        RCTR = float(0.0);
        AS_score_v = [0.0,0.0,0.0,0.0];
        u_id = int(r['id']);
        if (str(r['career_level']) == 'NULL'):
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
                 nr_groups,u_int_l,u_imp_l,w_e,RCTR,AS_score_v];
        users_d[u_id] = l_par;

    # fos
    print "\t\tfos";
    for i in range(0,len(fos_l)):
        user_id = fos_l[i][0];
        fos_id = fos_l[i][1];
        l = users_d[user_id][9];
        if fos_id not in l:
            l.append(fos_id);
        users_d[user_id][9] = l;
        users_d[user_id][11] += 1;

    # jobroles
    print "\t\tjobroles";
    for i in range(0,len(jbrl_l)):
        user_id = jbrl_l[i][0];
        jbrl_id = jbrl_l[i][1];
        l = users_d[user_id][10];
        if jbrl_id not in l:
            l.append(jbrl_id);
        users_d[user_id][10] = l;
        users_d[user_id][11] += 1;

    # interactions
    print "\t\tinteractions";
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
        #print score;
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
        l = users_d[user_id][12][period][int_type];
        l_par = [item_id,score];
        l.append(l_par);
        users_d[user_id][12][period][int_type] = l;
        users_d[user_id][14] += score;
        users_d[user_id][16][(int_type - 1)] += score;
        if (len(users_d[user_id][9]) > 0):
            for j in range(0, len(users_d[user_id][9])):
                fos_id = users_d[user_id][9][j];
                fos_d[fos_id][2][item_id] += score;
        if (len(users_d[user_id][10]) > 0):
            for j in range(0, len(users_d[user_id][10])):
                jobroles_id = users_d[user_id][10][j];
                jobroles_d[jobroles_id][2][item_id] += score;
        if (ccc%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;
        ccc += 1;

    # Vecchia Versione senza i periods
    for i in range(0,len(int_l)):
        user_id = int_l[i][0];
        item_id = int_l[i][1];
        int_type = int_l[i][2];
        diff_t = int_l[i][4];
        score = t_c.Time_decay_diff(diff_t, int_max_diff);
        l = users_d[user_id][12];
        l_par = [item_id,int_type,score];
        l.append(l_par);
        users_d[user_id][12] = l;
        #RCTR_par_score = items_d[item_id][18];
        users_d[user_id][14] += score;
        #users_d[user_id][15] += RCTR_par_score;
        users_d[user_id][16][(int_type - 1)] += score;
        if (len(users_d[user_id][9]) > 0):
            for j in range(0,len(users_d[user_id][9])):
                fos_id = users_d[user_id][9][j];
                fos_d[fos_id][2][item_id] += score;
        if (len(users_d[user_id][10]) > 0):
            for j in range(0,len(users_d[user_id][10])):
                jobroles_id = users_d[user_id][10][j];
                jobroles_d[jobroles_id][2][item_id] += score;
    
    # impressions
    contr = len(imp_d) / 4;
    perc = 25;
    ccc = 1;
    print "\t\tImpressions";
    for imp_id in imp_d:
        user_id = imp_d[imp_id][0];
        nr_items = imp_d[imp_id][4];
        score_s_imp = imp_d[imp_id][6];
        l = users_d[user_id][13];
        if imp_id not in l:
            l.append(imp_id);
        users_d[user_id][13] = l;
        if (nr_items > 0):
            for item_id in imp_d[imp_id][5]:
                nr_times = imp_d[imp_id][5][item_id];
                score_imp_item = score_s_imp * nr_times;
                RCTR_par_score = items_d[item_id][18];
                users_d[user_id][14] += score_imp_item;
                users_d[user_id][15] += RCTR_par_score;
                if (len(users_d[user_id][9]) > 0):
                    for j in range(0, len(users_d[user_id][9])):
                        fos_id = users_d[user_id][9][j];
                        fos_d[fos_id][2][item_id] += score_imp_item;
                if (len(users_d[user_id][10]) > 0):
                    for j in range(0, len(users_d[user_id][10])):
                        jobroles_id = users_d[user_id][10][j];
                        jobroles_d[jobroles_id][2][item_id] += score_imp_item;
        if (ccc%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;
        ccc += 1;

    # calcolo valori fissi
    print "\t\tcalcolo valori fissi"
    for user_id in users_d:
        if (users_d[user_id][11] > 0):
            users_d[user_id][11] = 1.0/users_d[user_id][11];
        if (users_d[user_id][14] > 0):
            users_d[user_id][14] = 1.0/users_d[user_id][14];

    b = datetime.datetime.now();
    print (b-a);
    return users_d;
    """

def Users_d_creation(c,country_d,fos_l,jbrl_l,fos_d,jobroles_d,int_max_diff,int_l,imp_d,items_d,\
                     int_periods_t_lim_v,imp_periods_t_lim_v):
    a = datetime.datetime.now();
    users_d = {};
    u_int_d = {};
    u_int_type_d = {};
    c.execute('select * from users');
    for r in c:
        fos = [];
        jobroles = [];
        nr_groups = int(0);
        periods_d = {};
        for i in range(1, 7):
            periods_d[i] = [[],[],0.0,0.0,[0.0, 0.0, 0.0, 0.0],[]];
        u_id = int(r['id']);
        if (str(r['career_level']) == 'NULL'):
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
                 nr_groups,periods_d];
        users_d[u_id] = l_par;

    # fos
    print "\t\tfos";
    for i in range(0,len(fos_l)):
        user_id = fos_l[i][0];
        fos_id = fos_l[i][1];
        l = users_d[user_id][9];
        if fos_id not in l:
            l.append(fos_id);
        users_d[user_id][9] = l;
        users_d[user_id][11] += 1;

    # jobroles
    print "\t\tjobroles";
    for i in range(0,len(jbrl_l)):
        user_id = jbrl_l[i][0];
        jbrl_id = jbrl_l[i][1];
        l = users_d[user_id][10];
        if jbrl_id not in l:
            l.append(jbrl_id);
        users_d[user_id][10] = l;
        users_d[user_id][11] += 1;

    #print "User 10866:";
    #print "Fos:";
    #print len(users_d[10866][9]);
    #print users_d[10866][9];
    #print "Jobroles:";
    #print len(users_d[10866][10]);
    #print users_d[10866][10];
    #print "Nr_groups:";
    #print users_d[10866][11];

    # interactions
    print "\t\tinteractions";
    contr = len(int_l) / 4;
    perc = 25;
    for i in range(0,len(int_l)):
        user_id = int_l[i][0];
        item_id = int_l[i][1];
        int_type = int_l[i][2];
        created_at = int_l[i][3];
        diff_t = int_l[i][4];
        score = t_c.Time_decay_diff(diff_t, int_max_diff);
        #print score;
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
        if (int_type == 1):
            l = users_d[user_id][12][period][5];
            if item_id not in l:
                l.append(item_id);
            users_d[user_id][12][period][5] = l;
        for j in range(period,7):
            l = users_d[user_id][12][j][0];
            l_par = [item_id,int_type,created_at,score];
            l.append(l_par);
            users_d[user_id][12][j][0] = l;
            users_d[user_id][12][j][2] += score;
            users_d[user_id][12][j][4][(int_type - 1)] += score;
            if (len(users_d[user_id][9]) > 0):
                for k in range(0,len(users_d[user_id][9])):
                    fos_id = users_d[user_id][9][k];
                    fos_d[fos_id][2][j][item_id] += score;
            if (len(users_d[user_id][10]) > 0):
                for k in range(0,len(users_d[user_id][10])):
                    jobroles_id = users_d[user_id][10][k];
                    jobroles_d[jobroles_id][2][j][item_id] += score;
        if ((i+1)%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;

    #print "User 10866:";
    #print users_d[10866][12][6][0];
    #print "Test set user 4869:";
    #print len(users_d[4869][12][6][5]);
    #print users_d[4869][12][6][5];

    # impressions
    contr = len(imp_d) / 4;
    perc = 25;
    ccc = 1;
    print "\t\tImpressions";
    for imp_id in imp_d:
        user_id = imp_d[imp_id][0];
        imp_week = imp_d[imp_id][2];
        nr_items = imp_d[imp_id][4];
        score_s_imp = imp_d[imp_id][6];
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
        for j in range(period,7):
            l = users_d[user_id][12][j][1];
            if imp_id not in l:
                l.append(imp_id);
            users_d[user_id][12][j][1] = l;
            if (nr_items > 0):
                imp_items_d = imp_d[imp_id][5];
                for item_id in imp_items_d:
                    nr_times = imp_items_d[item_id];
                    score_imp_item = score_s_imp * nr_times;
                    RCTR_par_score = items_d[item_id][18][j][1] * nr_times;
                    users_d[user_id][12][j][2] += score_imp_item;
                    users_d[user_id][12][j][3] += RCTR_par_score;
                    if (len(users_d[user_id][9]) > 0):
                        for k in range(0, len(users_d[user_id][9])):
                            fos_id = users_d[user_id][9][k];
                            fos_d[fos_id][2][j][item_id] += score_imp_item;
                    if (len(users_d[user_id][10]) > 0):
                        for k in range(0, len(users_d[user_id][10])):
                            jobroles_id = users_d[user_id][10][k];
                            jobroles_d[jobroles_id][2][j][item_id] += score_imp_item;
        if (ccc%contr) == 0:
            print "\t\t\t" + str(perc) + "%";
            perc += 25;
        ccc += 1;

    # calcolo valori fissi
    print "\t\tcalcolo valori fissi"
    for user_id in users_d:
        if (users_d[user_id][11] > 0):
            users_d[user_id][11] = 1.0/users_d[user_id][11];
        for i in range(1,7):
            if(users_d[user_id][12][i][2] > 0):
                users_d[user_id][12][i][2] = 1.0/users_d[user_id][12][i][2];

    b = datetime.datetime.now();
    print (b-a);
    return users_d;

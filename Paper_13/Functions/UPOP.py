"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import Interactions_type as i_t

# File contenente le funzioni riguardanti il predittore UPOP

def Identify_group_user_jobroles(c,id_user):
    c.execute('select DISTINCT jobrole as u_g from us_jobroles where user_id = %s'%(id_user));
    job_roles_groups = [];
    for r in c:
        job_roles_groups.append(r['u_g']);
    return job_roles_groups;

def Identify_group_user_fos(c,id_user):
    c.execute('select DISTINCT fos as u_g from us_fos where user_id = %s'%(id_user));
    fos_groups = [];
    for r in c:
        fos_groups.append(r['u_g']);
    return fos_groups;

def Count_users_group_jobroles(c,id_group):
    c.execute('select count(user_id) as count from us_jobroles where jobrole = %s'%(id_group));
    nr_users_jbrl = int(0);
    for r in c:
        nr_users_jbrl = int(r['count']);
    return nr_users_jbrl;

def Count_users_group_fos(c,id_group):
    c.execute('select count(user_id) as count from us_fos where fos = %s'%(id_group));
    nr_users_fos = int(0);
    for r in c:
        nr_users_fos = int(r['count']);
    return nr_users_fos;

def Count_users_group_jobroles_item(c,id_group,i_id_1,i_id_2):
    c.execute('select DISTINCT u.user_id as id\
                    from us_jobroles as u, impressions as imp, imp_items as imp_i, interactions as int\
                     where (u.jobrole = %s)\
                      and (((int.item_id = %s) and (int.user_id = u.user_id))\
                       or ((imp_i.item_id = %s) and (imp.id = imp_i.imp_id)\
                        and (imp.user_id = u.user_id)) )' % (id_group, i_id_1, i_id_2));
    user_list_jbr_i = [];
    for r in c:
        user_list_jbr_i.append(r['id']);
    return user_list_jbr_i;

def Count_users_group_jobroles_item_int(c,id_group,i_id):
    c.execute('select DISTINCT u.user_id as id\
                    from us_jobroles as u, interactions as int\
                     where (u.jobrole = %s) and (int.item_id = %s) and (int.user_id = u.user_id)\
                      and (int.interaction_type="1" or int.interaction_type="2"\
                       or int.interaction_type="3")' % (id_group, i_id));
    user_list_jbr_i_int = [];
    for r in c:
        user_list_jbr_i_int.append(r['id']);
    return user_list_jbr_i_int;

def Count_users_group_jobroles_item_imp(c,id_group,i_id):
    c.execute('select DISTINCT u.user_id as id\
                    from us_jobroles as u, impressions as imp, imp_items as ii\
                     where (u.jobrole = %s) and (ii.item_id = %s) and (imp.user_id = u.user_id)\
                      and (imp.id = ii.imp_id)' % (id_group, i_id));
    user_list_jbr_i_imp = [];
    for r in c:
        user_list_jbr_i_imp.append(r['id']);
    return user_list_jbr_i_imp;


def Count_users_group_fos_item(c,id_group,i_id_1,i_id_2):
    c.execute('select DISTINCT u.user_id as id\
                        from us_fos as u, impressions as imp, imp_items as imp_i, interactions as int\
                         where (u.fos = %s)\
                          and (((int.item_id = %s) and (int.user_id = u.user_id))\
                           or ((imp_i.item_id = %s) and (imp.id = imp_i.imp_id)\
                            and (imp.user_id = u.user_id)))' % (id_group, i_id_1, i_id_2));
    user_list_fos_i = [];
    for r in c:
        user_list_fos_i.append(r['id']);
    return user_list_fos_i;

def Count_users_group_fos_item_int(c,id_group,i_id):
    c.execute('select DISTINCT u.user_id as id\
                    from us_fos as u, interactions as int\
                     where (u.fos = %s) and (int.item_id = %s) and (int.user_id = u.user_id)\
                      and (int.interaction_type="1" or int.interaction_type="2"\
                       or int.interaction_type="3")' % (id_group, i_id));
    user_list_f_i_int = [];
    for r in c:
        user_list_f_i_int.append(r['id']);
    return user_list_f_i_int;

def Count_users_group_fos_item_imp(c,id_group,i_id):
    c.execute('select DISTINCT u.user_id as id\
                    from us_fos as u, impressions as imp, imp_items as ii\
                     where (u.fos = %s) and (ii.item_id = %s) and (imp.user_id = u.user_id)\
                      and (imp.id = ii.imp_id)' % (id_group, i_id));
    user_list_f_i_imp = [];
    for r in c:
        user_list_f_i_imp.append(r['id']);
    return user_list_f_i_imp;

def Count_users_group_fos_imp_item(c,id_group,i_id):
    c.execute('select DISTINCT u.user_id as id from us_fos as u, impressions as imp, imp_items as imp_i\
                where (u.fos = %s) and (imp_i.item_id = %s)\
                 and (imp.id = imp_i.imp_id) and (imp.user_id = u.user_id)'%(id_group, i_id));
    user_list_fos_i_imp = [];
    for r in c:
        user_list_fos_i_imp.append(r['id']);
    return user_list_fos_i_imp;

def Jobroles_list_users(c,id_group):
    c.execute('select DISTINCT user_id as id from us_jobroles where jobrole = %s'%(id_group));
    user_list_jbr = [];
    for r in c:
        user_list_jbr.append(r['id']);
    return user_list_jbr;

def Fos_list_users(c,id_group):
    c.execute('select DISTINCT user_id as id from us_fos where fos = %s'%(id_group));
    user_list_fos = [];
    for r in c:
        user_list_fos.append(r['id']);
    return user_list_fos;

def List_union_no_dupicates(first_list,second_list):
    in_first = set(first_list);
    in_second = set(second_list);
    in_second_but_not_in_first = in_second - in_first;
    result = first_list + list(in_second_but_not_in_first);
    return result;

def Jbrl_score_calculation(c,i_id,jbrl_id,t_max_int,max_diff_int,t_max_imp,max_diff_imp):
    u_d_j = 1.00 / Count_users_group_jobroles(c, jbrl_id);
    #print "ciao 2";
    #list = Jobroles_list_users(c,jbrl_id);
    #print list;
    user_list_j_int = Count_users_group_jobroles_item_int(c,jbrl_id,i_id);
    #print user_list_j_int;
    user_list_j_imp = Count_users_group_jobroles_item_imp(c,jbrl_id,i_id);
    #print user_list_j_imp;
    user_list_j = List_union_no_dupicates(user_list_j_int,user_list_j_imp);
    #print user_list_j;
    score_j = float(0.0);
    if (len(user_list_j)>0):
        for j in range(0, len(user_list_j)):
            user_int_j = i_t.Useful_items_interactions(c,user_list_j[j]);
            user_imp_j = i_t.Userful_items_impression(c,user_list_j[j]);
            nr_imp_j = len(user_imp_j)/2;
            if (len(user_int_j)>0):
                for w in range(0,len(user_int_j)):
                    score_j = score_j + i_t.Positive_Interaction(c,user_list_j[j],user_int_j[w],t_max_int,max_diff_int);
            if (nr_imp_j > 0):
                for w in range(0,nr_imp_j):
                    h = w*2;
                    score_j = score_j + i_t.Positive_Impressions(t_max_imp,max_diff_imp,user_imp_j[h+1]);
        score_j = u_d_j * score_j;
    else:
        score_j = 0.0;
    return score_j;

def Fos_score_calculation(c,i_id,fos_id,t_max_int,max_diff_int,t_max_imp,max_diff_imp):
    u_d_f = 1.00 / Count_users_group_jobroles(c, fos_id);
    user_list_f_int = Count_users_group_fos_item_int(c,fos_id,i_id);
    user_list_f_imp = Count_users_group_fos_item_imp(c,fos_id,i_id)
    #user_list_f = Count_users_group_jobroles_item(c,jbrl_id,i_id,i_id);
    user_list_f = List_union_no_dupicates(user_list_f_int,user_list_f_imp);
    score_f = float(0.0);
    if (len(user_list_f)>0):
        for j in range(0, len(user_list_f)):
            user_int_f = i_t.Useful_items_interactions(c,user_list_f[j]);
            user_imp_f = i_t.Userful_items_impression(c,user_list_f[j]);
            nr_imp_f = len(user_imp_f)/2;
            if (len(user_int_f)>0):
                for w in range(0,len(user_int_f)):
                    score_f = score_f + i_t.Positive_Interaction(c,user_list_f[j],user_int_f[w],t_max_int,max_diff_int);
            if (nr_imp_f > 0):
                for w in range(0,nr_imp_f):
                    h = w*2;
                    score_f = score_f + i_t.Positive_Impressions(t_max_imp,max_diff_imp,user_imp_f[h+1]);
    score_f = u_d_f * score_f;
    return score_f;

def UPOP_calculation_low_ram(c,u_id,i_id,int_t_max,int_max_diff,imp_t_max,imp_max_diff,lambd):
    jobroles = Identify_group_user_jobroles(c,u_id);
    fos = Identify_group_user_fos(c,u_id);
    #print jobroles;
    #print fos;
    upop_score_par = float(0.0);
    if ((len(jobroles)>0)or(len(fos)>0)):
        if (len(jobroles)>0):
            for i in range(0,len(jobroles)):
                #print "ciao 1"
                pop_g = Jbrl_score_calculation(c, i_id, jobroles[i], int_t_max, int_max_diff, imp_t_max, imp_max_diff);
                upop_score_par = upop_score_par + (pop_g/(pop_g + lambd));
        if (len(fos)>0):
            for i in range(0,len(fos)):
                pop_g = Fos_score_calculation(c, i_id, fos[i],int_t_max, int_max_diff, imp_t_max, imp_max_diff);
                upop_score_par = upop_score_par + (pop_g/(pop_g + lambd));
        upop_score = (1.00/(len(jobroles)+len(fos))) * upop_score_par;
    else:
        upop_score = 0.0;
    return upop_score;

def UPOP_calculation(u_v_fos,u_v_jbrl,nr_fos,nr_jbrls,fos_d,jbrl_d,item_id,lambd,one_div_nr_groups):
    upop_score = 0.0;
    if (nr_fos > 0):
        for i in range(0,len(u_v_fos)):
            pop_g = fos_d[u_v_fos[i]][2][item_id];
            upop_score += pop_g/(pop_g + lambd);
    if (nr_jbrls > 0):
        for i in range(0,len(u_v_jbrl)):
            pop_g = jbrl_d[u_v_jbrl[i]][2][item_id];
            upop_score += pop_g / (pop_g + lambd);
    upop_score *= one_div_nr_groups;
    return upop_score;
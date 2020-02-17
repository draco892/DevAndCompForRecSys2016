"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import datetime
import math
from collections import defaultdict

#File contenente le funzioni riguardanti la creazione dei dict rigurandanti i gruppi degli items e degli users



def Nr_items(c):
    c.execute('select count(id) as co from items');
    nr_it = 0;
    for r in c:
        nr_it = int(r['co']);
    return nr_it;

def Jobroles_list(c):
    c.execute('select * from us_jobroles');
    jbr_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['user_id']));
        l_par.append(int(r['jobrole']));
        jbr_l.append(l_par);
    return jbr_l;

def Jobroles_Dist_list(c):
    c.execute('select DISTINCT jobrole as jb from us_jobroles');
    job_roles_l = [];
    for r in c:
        job_roles_l.append(int(r['jb']));
    return job_roles_l;

"""
# Versione senza divisione temporale
def Jobroles_d_creation(c,jbr_l,items_upop_score_d):
    #print "Inizio calcolo Jobroles";
    a = datetime.datetime.now();
    jobroles_d = {};
    jbr_d_l = Jobroles_Dist_list(c);
    items_upop_sc_d = defaultdict(lambda: 0);
    if (len(jbr_d_l)>0):
        for i in range(0,len(jbr_d_l)):
            jobroles_d[jbr_d_l[i]] = [int(0),[],items_upop_sc_d.copy()];
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
"""

def Jobroles_d_creation(c,jbr_l):
    #print "Inizio calcolo Jobroles";
    a = datetime.datetime.now();
    jobroles_d = {};
    jbr_d_l = Jobroles_Dist_list(c);
    #items_upop_sc_d = defaultdict(lambda: 0);
    if (len(jbr_d_l)>0):
        for i in range(0,len(jbr_d_l)):
            p = {};
            for k in range(1,7):
                p[k] = defaultdict(lambda: 0.0);
            jobroles_d[jbr_d_l[i]] = [int(0),[],p];
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

def Fos_list(c):
    c.execute('select * from us_fos');
    fos_l = [];
    for r in c:
        l_par = [];
        l_par.append(int(r['user_id']));
        l_par.append(int(r['fos']));
        fos_l.append(l_par);
    return fos_l;

def Fos_Dist_list(c):
    c.execute('select DISTINCT fos as f from us_fos');
    f_l = [];
    for r in c:
        f_l.append(int(r['f']));
    return f_l;

"""
# Versione senza divisione temporale
def Fos_d_creation(c,fos_l,items_upop_score_d):
    #print "Inizio calcolo Fos";
    a = datetime.datetime.now();
    fos_d = {};
    fos_di_l = Fos_Dist_list(c);
    items_upop_sc_d = defaultdict(lambda: 0);
    if (len(fos_di_l)>0):
        for i in range(0,len(fos_di_l)):
            fos_d[fos_di_l[i]] = [int(0),[],items_upop_sc_d.copy()];
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
"""

def Fos_d_creation(c,fos_l):
    #print "Inizio calcolo Fos";
    a = datetime.datetime.now();
    fos_d = {};
    fos_di_l = Fos_Dist_list(c);
    if (len(fos_di_l)>0):
        for i in range(0,len(fos_di_l)):
            p = {};
            for k in range(1,7):
                p[k] = defaultdict(lambda: 0.0);
            fos_d[fos_di_l[i]] = [int(0),[],p];
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

def Tags_d_creation(c,tags_l,n_u_t,nr_items):
    #print "Inizio calcolo Tags";
    a = datetime.datetime.now();
    tags_d = {};
    tags_di_l = Tags_Dist_list(c,n_u_t);
    if (len(tags_di_l)>0):
        for i in range(0,len(tags_di_l)):
            tf_idf_sc = float(0.0);
            tags_d[tags_di_l[i]] = [int(0),[],tf_idf_sc];
    if (len(tags_l)>0):
        for i in range(0,len(tags_l)):
            if tags_l[i][0] not in tags_d[tags_l[i][1]][1]:
                tags_d[tags_l[i][1]][0] += 1;
                l = tags_d[tags_l[i][1]][1];
                l.append(tags_l[i][0]);
                tags_d[tags_l[i][1]][1] = l;
    for tag_id in tags_d:
        nr_users_group = tags_d[tag_id][0];
        if (nr_users_group > 0):
            idf = math.log(nr_items/nr_users_group);
            tags_d[tag_id][2] = idf;
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

def Titles_d_creation(c,titles_l,n_u_t,nr_items):
    #print "Inizio calcolo Titles";
    a = datetime.datetime.now();
    titles_d = {};
    t_di_l = Titles_Dist_list(c,n_u_t);
    if (len(t_di_l)>0):
        for i in range(0,len(t_di_l)):
            tf_idf_sc = float(0.0);
            titles_d[t_di_l[i]] = [int(0),[],tf_idf_sc];
    if (len(titles_l)>0):
        for i in range(0,len(titles_l)):
            if titles_l[i][0] not in titles_d[titles_l[i][1]][1]:
                titles_d[titles_l[i][1]][0] += 1;
                l = titles_d[titles_l[i][1]][1];
                l.append(titles_l[i][0]);
                titles_d[titles_l[i][1]][1] = l;
    for title_id in titles_d:
        nr_users_group = titles_d[title_id][0];
        if (nr_users_group > 0):
            idf = math.log(nr_items / nr_users_group);
            titles_d[title_id][2] = idf;
    b = datetime.datetime.now();
    #print "Fine calcolo Titles";
    #print (b - a);
    return titles_d;
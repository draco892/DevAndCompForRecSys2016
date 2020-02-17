"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import sqlite3
import Sys_Flush as s_f

#File contenente le funzioni utili ad eliminare dal db le interactions ed impressions contenenti items/users
# inesistenti.


def Users_list(c):
    c.execute('select DISTINCT id as i from users');
    users_l = [];
    for r in c:
        users_l.append(int(r['i']));
    return users_l;

def Items_List(c):
    c.execute('select DISTINCT id as i from items');
    items_l = [];
    for r in c:
        items_l.append(int(r['i']));
    return items_l;

def Interactions_items_list(c):
    c.execute('select DISTINCT item_id as i from interactions');
    int_it_l = [];
    for r in c:
        int_it_l.append(int(r['i']));
    return int_it_l;

def Interactions_users_list(c):
    c.execute('select DISTINCT user_id as i from interactions');
    int_us_l = [];
    for r in c:
        int_us_l.append(int(r['i']));
    return int_us_l;

def Impressions_items_list(c):
    c.execute('select DISTINCT item_id as i from imp_items');
    imp_it_l = [];
    for r in c:
        imp_it_l.append(int(r['i']));
    return imp_it_l;

def Impressions_users_list(c):
    c.execute('select DISTINCT user_id as i from impressions');
    imp_us_l = [];
    for r in c:
        imp_us_l.append(int(r['i']));
    return imp_us_l;

def Finding_impostors(list_1,list_2):
    impostors_l = [];
    if (len(list_1)>0):
        for i in range(0,len(list_1)):
            if list_1[i] not in list_2:
                impostors_l.append(list_1[i]);
    return impostors_l;

def Delete_interactions_items(c,i_l):
    contr = len(i_l)/5;
    per = 20;
    for i in range(0,len(i_l)):
        print "\t\tEliminazione:\t" + str(i_l[i]);
        c.execute('DELETE FROM interactions where item_id = %s'%(i_l[i]));
        if ((i%contr)==0) and (i!=0):
            #print str(per) + "%";
            #per += 20;
            s_f.fl();
    s_f.fl();

def Delete_interactions_users(c,u_l):
    contr = len(u_l) / 5;
    per = 20;
    for i in range(0,len(u_l)):
        print "\t\tEliminazione:\t" + str(u_l[i]);
        c.execute('DELETE FROM interactions where user_id = %s' % (u_l[i]));
        if ((i%contr)==0) and (i!=0):
            print str(per) + "%";
            per += 20;
            s_f.fl();
    s_f.fl();

def Delete_imp_items_items(c,i_l):
    contr = len(i_l) / 10;
    per = 10;
    for i in range(0,len(i_l)):
        #print "\t\tEliminazione:\t" + str(i_l[i]);
        c.execute('DELETE FROM imp_items where item_id = %s'%(i_l[i]));
        if ((i%contr)==0) and (i!=0):
            print str(per) + "%";
            per += 10;
            s_f.fl();
    s_f.fl();

def Delete_imp_users(c,i_l):
    for i in range(0,len(i_l)):
        print "users:\t" + str(i_l[i]);
        imp_l = [];
        c.execute('select DISTINCT id as i from impressions where user_id = %s'%(i_l[i]));
        for r in c:
            imp_l.append(int(r['i']));
        for i in range(0,len(imp_l)):
            c.execute('DELETE FROM imp_items where imp_id = %s' % (imp_l[i]));
            c.execute('DELETE FROM impressions where id = %s'%(imp_l[i]));

def Smooting(d_l):
    if (d_l == True):
        db_path = 'File_db/recsys16_lite.db';
    else:
        db_path = 'File_db/recsys16.db';
    conn = sqlite3.connect(db_path);
    conn.row_factory = sqlite3.Row;
    c = conn.cursor();
    items_l = Items_List(c);
    users_l = Users_list(c);
    int_u_l = Interactions_users_list(c);
    int_i_l = Interactions_items_list(c);
    imp_u_l = Impressions_users_list(c);
    imp_i_l = Impressions_items_list(c);
    impostors_int_i_l = Finding_impostors(int_i_l,items_l);
    impostors_int_u_l = Finding_impostors(int_u_l,users_l);
    impostors_imp_i_l = Finding_impostors(imp_i_l,items_l);
    impostors_imp_u_l = Finding_impostors(imp_u_l,users_l);
    print "impostors_int_i_l";
    if (len(impostors_int_i_l)>0):
        print len(impostors_int_i_l);
        #for i in range(0,len(impostors_int_i_l)):
             #print impostors_int_i_l[i];
        Delete_interactions_items(c,impostors_int_i_l);
        conn.commit();
    else:
        print "\t Nothing Found";
    print "impostors_int_u_l";
    if (len(impostors_int_u_l)>0):
        print len(impostors_int_u_l);
        #for i in range(0,len(impostors_int_u_l)):
            #print impostors_int_u_l[i];
        Delete_interactions_users(c,impostors_int_u_l);
        conn.commit();
    else:
        print "\t Nothing Found";
    print "impostors_imp_i_l"
    if (len(impostors_imp_i_l)):
        print "\t" + str(len(impostors_imp_i_l)) + " impostors";
        print impostors_imp_i_l;
        Delete_imp_items_items(c,impostors_imp_i_l);
        conn.commit();
    else:
        print "\t Nothing Found";
    print "impostors_imp_u_l"
    if (len(impostors_imp_u_l)>0):
        print "\t" + str(len(impostors_imp_u_l)) + " impostors";
        print impostors_imp_u_l;
        Delete_imp_users(c,impostors_imp_u_l);
        conn.commit();
    else:
        print "\t Nothing Found";
    conn.commit();
    conn.close();
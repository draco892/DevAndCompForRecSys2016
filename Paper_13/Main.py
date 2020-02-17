"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import datetime
import sys
from Classes import Sqlite as sq
from Classes import Transfer_to_RAM as tr
from Classes import Predictors as pr
from Classes import Pikle_operations as p_o
from Functions import Check_File as cf
from Functions import Dataset_Selection as data
from Functions import Sys_Flush as sf
from Functions import Smooth_db


#file contenete il Main del programma

def main():
    print "Inizio Lettura File\n";

    """
    if (cf.check('Dataset/users.csv') == False)\
            or (cf.check('Dataset/items.csv') == False) \
            or (cf.check('Dataset/interactions.csv') == False)\
            or (cf.check('Dataset/impressions.csv') == False):
        print "Errore: File .csv necessari non presenti";
        return 1;
    """

    #ds_lite = data.d_s();
    ds_lite = True;

    # In tale controllo suppongo che se il file recsys16.db esiste,
    # esso sia anche completo.
    if (cf.check('File_db/recsys16.db') == False) and (ds_lite == False):
        print 'File recsys16.db non esistente.\nInizio creazione file:';

        r = sq.Sqlite(ds_lite);

        print 'create users';
        sf.fl();
        r.create_users();
        r.fill_users();
        print "\tLettura del file users.csv completata";

        print 'create interactions';
        sf.fl();
        r.create_interactions();
        r.fill_interactions();
        print "\tLettura del file interactions.csv completata";

        print 'create items';
        sf.fl();
        r.create_items();
        r.fill_items();
        print "\tLettura del file items.csv completata";

        print 'create impressions';
        sf.fl();
        r.create_impressions();
        r.fill_impressions();
        print "\tLettura del file impressions.csv completata";

        r.end_read();

        print 'Controllo dati anomali'
        Smooth_db.Smooting(ds_lite);

        print "Creazione file .db completata con successo";
    elif (cf.check('File_db/recsys16_lite.db') == False) and (ds_lite == True):
        print 'Inizio creazione file:';

        r = sq.Sqlite(ds_lite);

        n = int(input("\tInserire il numero di utenti del Dataset:\t"));

        print 'create users ('+ str(n) +' users)';
        sf.fl();
        r.create_users();
        r.fill_users_lite(n);
        print "\tLettura del file users.csv completata";

        print 'create interactions';
        sf.fl();
        r.create_interactions();
        r.fill_interactions_lite();
        print "\tLettura del file interactions.csv completata";

        print 'create impressions';
        sf.fl();
        r.create_impressions();
        r.fill_impressions_lite();
        print "\tLettura del file impressions.csv completata";

        print 'create items';
        sf.fl();
        r.create_items();
        r.fill_items_lite();
        print "\tLettura del file items.csv completata";

        r.end_read();

        print 'Controllo dati anomali'
        Smooth_db.Smooting(ds_lite);

    else:
        print "file .db esistente."

    #print "Fine Lettura File\n"
    print "Inizio caricamento dati in RAM:";
    t = tr.T_to_RAM(ds_lite);
    user_dict = t.users_dict();
    item_dict = t.items_dict();
    imp_d = t.imp_dict();
    item_score_dict = t.items_score_dict();
    fos_d = t.fos_dict();
    jobroles_d = t.jobroles_dict();
    print "Fine caricamento dati in RAM\n";

    #return 0;

    print "Inizio Calcolo Predittori:";
    a = datetime.datetime.now();
    p = pr.Predictors(item_score_dict);

    lambd = 0.01;
    alpha = 0.4;

    users_active_period = [[],[],[],[],[]];
    users_list = [];

    nr_active_users = 0;

    for i in range(0,5):
        per = 6 - i;
        for user_id in user_dict:
            if len(user_dict[user_id][12][per][5]) > 0:
                kkk = 0;
                if per < 6:
                    for j in range(0,i):
                        if user_id in users_active_period[j]:
                            kkk = 1;
                    if kkk == 0:
                        users_active_period[i].append(user_id);
                        users_list.append([user_id, per]);
                else:
                    users_active_period[i].append(user_id);
                    users_list.append([user_id, per]);

        #print "Period " + str(per);
        #print len(users_active_period[i]);
        nr_active_users += len(users_active_period[i]);

    #print len(users_list)
    #print nr_active_users;
    #print users_list;

    """
    for i in range(0,len(users_list)):
        user_id = users_list[i][0];
        if user_id == 1827:
            print users_list[i];
    """
    #return 0;

    nr_jobs = int(sys.argv[1]);
    program_job = int(sys.argv[2]);

    #nr_jobs = 50;
    #program_job = 50;

    int_l = [];
    kkk = 0;

    usrs_j = nr_active_users/nr_jobs;
    resto = nr_active_users%nr_jobs;

    while (kkk <= nr_active_users):
        int_l.append(kkk);
        if (resto > 0):
            kkk += usrs_j + 1;
            resto -= 1;
        else: kkk += usrs_j;

    inizio = int_l[program_job - 1];
    fine = int_l[program_job];

    #print inizio;
    #print fine;

    #return 0;

    score = 0.0;

    if (len(users_list) > 0):
        #for i in range(0,len(users_list)):
        #for i in range(0, 1):
        for i in range(inizio,fine):
            ini = datetime.datetime.now();
            user_id = users_list[i][0];
            per_ts = users_list[i][1];
            per_lim_tr = per_ts - 1;
            print user_id;
            #print (i+1);
            #print per_ts;
            #print per_lim_tr;
            score += p.All_predictors_calc(user_dict[user_id],per_lim_tr,per_ts,\
                                           imp_d,item_dict,fos_d,jobroles_d,lambd,alpha);
            fin = datetime.datetime.now();
            #print (fin-ini);

    print "Score:\t" + str(score);
    b = datetime.datetime.now();
    print "Fine Cacolo Predittori";
    print str(b - a) + "\n";
    print score;
    print "So long and thanks for all the fish :D";
    return 0;

if __name__ == "__main__":
    main();
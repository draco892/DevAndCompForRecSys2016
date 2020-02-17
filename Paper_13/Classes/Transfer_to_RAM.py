"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import sqlite3
import datetime
import Pikle_operations as p_o
from Functions import Time_Calcolation as tc
from Functions import Users_dict as u_d
from Functions import Items_dict as i_d
from Functions import Users_Items_groups_dict as g_d
from Functions import Interactions_Impressions_dict as int_imp_d

#File contenente la classe T_to_RAM

class T_to_RAM:

    # Modulo riguardante l'inizializzazione della classe
    def __init__(self, d_l):
        a = datetime.datetime.now();
        if (d_l == True):
            db_path = 'File_db/recsys16_lite.db';
        else:
            db_path = 'File_db/recsys16.db';
        conn = sqlite3.connect(db_path);
        conn.row_factory = sqlite3.Row;
        c = conn.cursor();

        pik = p_o.Pickle_operator(d_l);

        nr_items = g_d.Nr_items(c);

        if (pik.check_int_max_time_file() == False):
            self.int_max_time = tc.Max_T_int(c);
            pik.save_int_max_time(self.int_max_time);
        else:
            self.int_max_time = pik.load_int_max_time();

        if (pik.check_int_max_diff_file() == False):
            self.int_max_diff = self.int_max_time - tc.Min_T_int(c);
            pik.save_int_max_diff(self.int_max_diff);
        else:
            self.int_max_diff = pik.load_int_max_diff();


        # divisioni periodi temporali interactions
        #print self.int_max_diff;
        t_period = self.int_max_diff / 7;
        #print t_period;
        t_rest = self.int_max_diff%t_period;
        #print t_rest;
        period_test = tc.Min_T_int(c);
        int_periods_t_lim_v = [];
        for i in range(0,6):
            #print period_test;
            int_periods_t_lim_v.append(period_test);
            period_test += t_period;
        period_test += t_period + t_rest;
        int_periods_t_lim_v.append(period_test);
        #print int_periods_t_lim_v;
        #print self.int_max_time;

        # divisioni periodi temporali impressions
        imp_periods_t_lim_v = [];
        for i in range(0,len(int_periods_t_lim_v)):
            tmsp = int_periods_t_lim_v[i];
            week = datetime.datetime.fromtimestamp(tmsp).isocalendar()[1];
            imp_periods_t_lim_v.append(week);
        #print imp_periods_t_lim_v;


        if (pik.check_imp_max_time_file() == False):
            self.imp_max_time = tc.Max_T_imp(c);
            imp_max_year = tc.Max_year_imp(c);
            self.imp_max_time += (imp_max_year * 52);
            pik.save_imp_max_time(self.imp_max_time);
        else:
            self.imp_max_time = pik.load_imp_max_time();

        if (pik.check_imp_max_diff_file() == False):
            imp_min_year = tc.Min_year_imp(c);
            self.imp_max_diff = self.imp_max_time - (tc.Min_T_imp(c,imp_min_year)+(imp_min_year*52));
            pik.save_imp_max_diff(self.imp_max_diff);
        else:
            self.imp_max_diff = pik.load_imp_max_diff();

        if (pik.check_item_max_time_file() == False):
            self.item_max_time = tc.Max_T_items(c);
            pik.save_item_max_time(self.item_max_time);
        else:
            self.item_max_time = pik.load_item_max_time();

        if (pik.check_item_min_time_file() == False):
            Min_t = tc.Min_T_items(c);
            pik.save_item_min_time(Min_t);
        else:
            Min_t = pik.load_item_min_time();

        if (pik.check_item_max_diff_file() == False):
            self.item_max_diff = self.item_max_time - Min_t;
            pik.save_item_max_diff(self.item_max_diff);
        else:
            self.item_max_diff = pik.load_item_max_diff();

        print "\tItems score dict";
        if (pik.check_item_score_dict_file() == False):
            self.items_score_d = i_d.Item_score_dict(c);
            pik.save_item_score_dict(self.items_score_d);
        else:
            self.items_score_d = pik.load_item_score_dict();

        print "\tJobroles";
        if (pik.check_jobroles_list_file() == False):
            jobroles_l = g_d.Jobroles_list(c);
            pik.save_jobroles_list(jobroles_l);
        else:
            jobroles_l = pik.load_jobroles_list();
        self.jobroles_d = g_d.Jobroles_d_creation(c,jobroles_l);

        #print "Jobrole 996660"
        #print self.jobroles_d[996660][0];
        #print len(self.jobroles_d[996660][1]);
        #print self.jobroles_d[996660][1];
        #print self.jobroles_d[996660][2];

        #return 0;

        print "\tFos";
        if (pik.check_fos_list_file() == False):
            fos_l = g_d.Fos_list(c);
            pik.save_fos_list(fos_l);
        else:
            fos_l = pik.load_fos_list();
        self.fos_d = g_d.Fos_d_creation(c,fos_l);

        #print "Fos 1:";
        #print self.fos_d[1][0];
        #print self.fos_d[1][1];
        #print len(self.fos_d[1][1]);
        #print self.fos_d[1][2];
        #print self.fos_d[2][2];

        #return 0;

        print "\tTags";
        if (pik.check_tags_list_file() == False):
            tags_l = g_d.Tags_list(c,0);
            pik.save_tags_list(tags_l);
        else:
            tags_l = pik.load_tags_list();
        if (pik.check_tags_dict_file() == False):
            self.tags_d = g_d.Tags_d_creation(c,tags_l,0,nr_items);
            pik.save_tags_dict(self.tags_d);
        else:
            self.tags_d = pik.load_tags_dict();

        #print "Tag NULL:"
        #print self.tags_d[0][0];
        #print self.tags_d[0][1];
        #print self.tags_d[0][2];

        print "\tTitles";
        if (pik.check_titles_list_file() == False):
            titles_l = g_d.Titles_list(c,0);
            pik.save_titles_list(titles_l);
        else:
            titles_l = pik.load_titles_list();
        if (pik.check_titles_dict_file() == False):
            self.titles_d = g_d.Titles_d_creation(c,titles_l,0,nr_items);
            pik.save_titles_dict(self.titles_d);
        else:
            self.titles_d = pik.load_titles_dict();

        #print "Title NULL:";
        #print self.titles_d[0][0];
        #print self.titles_d[0][1];
        #print self.titles_d[0][2];

        print "\tInteractions";
        if (pik.check_int_list_file() == False):
            int_list = int_imp_d.int_list(c,self.int_max_time);
            pik.save_int_list(int_list);
        else:
            int_list = pik.load_int_list();
        if (pik.check_int_dist_file() == False):
            self.int_d = int_imp_d.int_d_creation(c,self.int_max_time,int_list,self.int_max_diff);
            pik.save_int_dist(self.int_d);
        else:
            self.int_d = pik.load_int_dist();

        #print "Interactions list i = 14 :";
        #print int_list[14];
        #print "Interactions dict type=4 i=165:";
        #print len(self.int_d[4]);
        #print self.int_d[4][165];

        print "\tImpressions";
        if (pik.check_imp_dict_file() == False):
            if (pik.check_item_imp_list_file() == False):
                imp_items_l = int_imp_d.imp_items_list(c);
                pik.save_item_imp_list(imp_items_l);
            else:
                imp_items_l = pik.load_item_imp_list();
            if (pik.check_imp_list_file() == False):
                imp_l = int_imp_d.imp_list(c);
                pik.save_imp_list(imp_l);
            else:
                imp_l = pik.load_imp_list();
            self.imp_d = int_imp_d.imp_d_creation(c,self.imp_max_time,imp_items_l,self.imp_max_diff);
            pik.save_imp_dict(self.imp_d);
        else:
            self.imp_d = pik.load_imp_dict();
            imp_l = pik.load_imp_list();

        #print "Imp items list i=13:"
        #print imp_items_l[13];
        #print "Imp list i=156:";
        #print imp_l[156];
        #print "Imp dict 10128439:";
        #print self.imp_d[10128439];

        print "\tCountry Dict";
        if (pik.check_country_dict_file() == False):
            country_dict = i_d.country_dict(c);
            pik.save_country_dict(country_dict);
        else:
            country_dict = pik.load_country_dict();

        #print "Country Dict:";
        #print country_dict;

        #return 0;

        print "\tItems";
        self.items_d = i_d.Items_d_creation(c,Min_t,self.item_max_time,self.item_max_diff,country_dict,\
                                            titles_l, tags_l, self.titles_d,\
                                            self.tags_d, int_list, self.int_max_diff, self.imp_d,\
                                            int_periods_t_lim_v, imp_periods_t_lim_v);
        #print "Items_d[2828770]:";
        #print "titles:";
        #print len(self.items_d[2828770][11]);
        #print self.items_d[2828770][11];
        #print "tags:";
        #print len(self.items_d[2828770][12]);
        #print self.items_d[2828770][12];
        #print "AP score:";
        #print self.items_d[2828770][14];
        #print "sim_cos_tit and tag";
        #print self.items_d[2828770][15];
        #print self.items_d[2828770][16];
        #print "IKNN_SI:";
        #print self.items_d[2828770][18][6][2];
        #print "Last_int:";
        #print self.items_d[2828770][18][6][0][3245];
        #print self.items_d[2828770][18][6][0][1884];
        #print self.items_d[2828770][18][6][0][7449];

        #print "fos prima:";
        #print self.fos_d[1][2];

        #print int_periods_t_lim_v;

        #b = datetime.datetime.now();
        #print "Tempo totale fino ad items dict:\t" + str(b - a);

        #return 0;

        #self.items_d = 0;

        print "\tUsers";
        self.users_d = u_d.Users_d_creation(c,country_dict,fos_l,jobroles_l,self.fos_d,self.jobroles_d,\
                                            self.int_max_diff, int_list, self.imp_d, self.items_d,\
                                            int_periods_t_lim_v, imp_periods_t_lim_v);
        pik.save_users_dict(self.users_d);

        #print "fos dopo:";
        #print self.fos_d[1][2];
        #print "User 10866:";
        #print "Fos:";
        #print self.users_d[10866][9];
        #print "Jobroles:";
        #print self.users_d[10866][10];
        #print "Nr_groups:";
        #print self.users_d[10866][11];
        #print "Interactions:";
        #print self.users_d[10866][12];
        #print "Impressions:";
        #print self.users_d[10866][13];
        #print "W_e:";
        #print self.users_d[10866][14];
        #print "RTCR_score:";
        #print self.users_d[10866][15];
        #print "AS_score:";
        #print self.users_d[10866][16];

        b = datetime.datetime.now();
        print "Tempo totale creazione dict:\t" + str(b - a);
        conn.commit();
        conn.close();

    def items_score_dict(self):
        return self.items_score_d;

    def users_dict(self):
        return self.users_d;

    def items_dict(self):
        return self.items_d;

    def jobroles_dict(self):
        return self.jobroles_d;

    def fos_dict(self):
        return self.fos_d;

    def tags_dict(self):
        return self.tags_d;

    def titles_dict(self):
        return self.titles_d;

    def imp_dict(self):
        return self.imp_d;

    def int_dict(self):
        return self.int_d;

    def int_m_time(self):
        return self.int_max_time;

    def int_m_diff(self):
        return self.int_max_diff;

    def imp_m_time(self):
        return self.imp_max_time;

    def imp_m_diff(self):
        return self.imp_max_diff;

    def item_m_diff(self):
        return self.item_max_diff;
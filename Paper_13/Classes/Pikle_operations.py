"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import cPickle as Pickle
from Functions import Check_File as cf

#File contenente la classe che si occupa del salvataggio dei vari dizionari nei file .pik

class Pickle_operator:

    def __init__(self,d_l):
        if (d_l == True):
            self.country_dict_path = 'Files_pik/Country_d_lite.pik';
            self.users_d_path = 'Files_pik/users_d_lite.pik';
            self.users_l_path = 'Files_pik/users_l_lite.pik';
            self.items_d_path = 'Files_pik/items_d_lite.pik';
            self.items_l_path = 'Files_pik/items_l_lite.pik';
            self.int_l_path = 'Files_pik/int_l_lite.pik';
            self.int_d_path = 'Files_pik/int_d_lite.pik';
            self.item_imp_l_path = 'Files_pik/item_imp_l_lite.pik';
            self.imp_l_path = 'Files_pik/imp_l_lite.pik';
            self.imp_d_path = 'Files_pik/imp_d_lite.pik';
            self.item_score_d_path = 'Files_pik/item_score_d_lite.pik';
            self.int_max_diff_path = 'Files_pik/int_max_diff_lite.pik';
            self.imp_max_diff_path = 'Files_pik/imp_max_diff_lite.pik';
            self.item_max_diff_path = 'Files_pik/item_max_diff_lite.pik';
            self.int_max_time_path = 'Files_pik/int_max_time_lite.pik';
            self.imp_max_time_path = 'Files_pik/imp_max_time_lite.pik';
            self.item_max_time_path = 'Files_pik/item_max_time_lite.pik';
            self.item_min_time_path = 'Files_pik/item_min_time_lite.pik';
            self.fos_l_path = 'Files_pik/fos_l_lite.pik';
            self.fos_d_path = 'Files_pik/fos_d_lite.pik';
            self.jobroles_l_path = 'Files_pik/jobroles_l_lite.pik';
            self.jobroles_d_path = 'Files_pik/jobroles_d_lite.pik';
            self.title_not_used = 'Files_pik/title_not_used_lite.pik';
            self.titles_l_path = 'Files_pik/title_l_lite.pik';
            self.titles_d_path = 'Files_pik/title_d_lite.pik';
            self.tags_not_used = 'Files_pik/tag_not_used_lite.pik';
            self.tags_l_path = 'Files_pik/tags_l_lite.pik';
            self.tags_d_path = 'Files_pik/tags_d_lite.pik';
        else:
            self.country_dict_path = 'Files_pik/Country_d.pik';
            self.users_d_path = 'Files_pik/users_d.pik';
            self.users_l_path = 'Files_pik/users_l.pik';
            self.items_d_path = 'Files_pik/items_d.pik';
            self.items_l_path = 'Files_pik/items_l.pik';
            self.int_l_path = 'Files_pik/int_l.pik';
            self.int_d_path = 'Files_pik/int_d.pik';
            self.item_imp_l_path = 'Files_pik/item_imp_l.pik';
            self.imp_l_path = 'Files_pik/imp_l.pik';
            self.imp_d_path = 'Files_pik/imp_d.pik';
            self.item_score_d_path = 'Files_pik/item_score_d.pik';
            self.int_max_diff_path = 'Files_pik/int_max_diff.pik';
            self.imp_max_diff_path = 'Files_pik/imp_max_diff.pik';
            self.item_max_diff_path = 'Files_pik/item_max_diff.pik';
            self.int_max_time_path = 'Files_pik/int_max_time.pik';
            self.imp_max_time_path = 'Files_pik/imp_max_time.pik';
            self.item_max_time_path = 'Files_pik/item_max_time.pik';
            self.item_min_time_path = 'Files_pik/item_min_time.pik';
            self.fos_l_path = 'Files_pik/fos_l.pik';
            self.fos_d_path = 'Files_pik/fos_d.pik';
            self.jobroles_l_path = 'Files_pik/jobroles_l.pik';
            self.jobroles_d_path = 'Files_pik/jobroles_d.pik';
            self.title_not_used = 'Files_pik/title_not_used.pik';
            self.titles_l_path = 'Files_pik/title_l.pik';
            self.titles_d_path = 'Files_pik/title_d.pik';
            self.tags_not_used = 'Files_pik/tag_not_used.pik';
            self.tags_l_path = 'Files_pik/tags_l.pik';
            self.tags_d_path = 'Files_pik/tags_d.pik';

    def check_country_dict_file(self):
        return cf.check(self.country_dict_path);

    def save_country_dict(self,obj):
        fileobj = open(self.country_dict_path, 'wb');
        Pickle.dump(obj,fileobj);
        fileobj.close();

    def load_country_dict(self):
        with open(self.country_dict_path, 'rb') as pickle_file:
            country_dict = Pickle.load(pickle_file);
        return country_dict;

    def check_users_dict_file(self):
        return cf.check(self.users_d_path);

    def save_users_dict(self,obj):
        fileobj = open(self.users_d_path, 'wb');
        Pickle.dump(obj,fileobj);
        fileobj.close();

    def load_users_dict(self):
        with open(self.users_d_path, 'rb') as pickle_file:
            users_d = Pickle.load(pickle_file);
        return users_d;

    def check_users_list_file(self):
        return cf.check(self.users_l_path);

    def save_users_list(self,obj):
        fileobj = open(self.users_l_path, 'wb');
        Pickle.dump(obj,fileobj);
        fileobj.close();

    def load_users_list(self):
        with open(self.users_l_path, 'rb') as pickle_file:
            users_l = Pickle.load(pickle_file);
        return users_l;

    def check_items_list_file(self):
        return cf.check(self.items_l_path);

    def save_items_list(self,obj):
        fileobj = open(self.items_l_path, 'wb');
        Pickle.dump(obj,fileobj);
        fileobj.close();

    def load_items_list(self):
        with open(self.items_l_path, 'rb') as pickle_file:
            items_l = Pickle.load(pickle_file);
        return items_l;

    def check_int_list_file(self):
        return cf.check(self.int_l_path);

    def save_int_list(self, obj):
        fileobj = open(self.int_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_int_list(self):
        with open(self.int_l_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_int_dist_file(self):
        return cf.check(self.int_d_path);

    def save_int_dist(self, obj):
        fileobj = open(self.int_d_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_int_dist(self):
        with open(self.int_d_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_item_imp_list_file(self):
        return cf.check(self.item_imp_l_path);

    def save_item_imp_list(self, obj):
        fileobj = open(self.item_imp_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_imp_list(self):
        with open(self.item_imp_l_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_imp_list_file(self):
        return cf.check(self.imp_l_path);

    def save_imp_list(self, obj):
        fileobj = open(self.imp_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_imp_list(self):
        with open(self.imp_l_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_imp_dict_file(self):
        return cf.check(self.imp_d_path);

    def save_imp_dict(self, obj):
        fileobj = open(self.imp_d_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_imp_dict(self):
        with open(self.imp_d_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_item_score_dict_file(self):
        return cf.check(self.item_score_d_path);

    def save_item_score_dict(self, obj):
        fileobj = open(self.item_score_d_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_score_dict(self):
        with open(self.item_score_d_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_int_max_diff_file(self):
        return cf.check(self.int_max_diff_path);

    def save_int_max_diff(self, obj):
        fileobj = open(self.int_max_diff_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_int_max_diff(self):
        with open(self.int_max_diff_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_imp_max_diff_file(self):
        return cf.check(self.imp_max_diff_path);

    def save_imp_max_diff(self, obj):
        fileobj = open(self.imp_max_diff_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_imp_max_diff(self):
        with open(self.imp_max_diff_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_fos_list_file(self):
        return cf.check(self.fos_l_path);

    def save_fos_list(self, obj):
        fileobj = open(self.fos_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_fos_list(self):
        with open(self.fos_l_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_jobroles_list_file(self):
        return cf.check(self.jobroles_l_path);

    def save_jobroles_list(self, obj):
        fileobj = open(self.jobroles_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_jobroles_list(self):
        with open(self.jobroles_l_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_int_max_time_file(self):
        return cf.check(self.int_max_time_path);

    def save_int_max_time(self, obj):
        fileobj = open(self.int_max_time_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_int_max_time(self):
        with open(self.int_max_time_path, 'rb') as pickle_file:
            int_max_time = Pickle.load(pickle_file);
        return int_max_time;

    def check_imp_max_time_file(self):
        return cf.check(self.imp_max_time_path);

    def save_imp_max_time(self, obj):
        fileobj = open(self.imp_max_time_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_imp_max_time(self):
        with open(self.imp_max_time_path, 'rb') as pickle_file:
            imp_max_time = Pickle.load(pickle_file);
        return imp_max_time;

    def check_item_max_time_file(self):
        return cf.check(self.item_max_time_path);

    def save_item_max_time(self, obj):
        fileobj = open(self.item_max_time_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_max_time(self):
        with open(self.item_max_time_path, 'rb') as pickle_file:
            item_max_time = Pickle.load(pickle_file);
        return item_max_time;

    def check_item_max_diff_file(self):
        return cf.check(self.item_max_diff_path);

    def save_item_max_diff(self, obj):
        fileobj = open(self.item_max_diff_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_max_diff(self):
        with open(self.item_max_diff_path, 'rb') as pickle_file:
            item_max_diff = Pickle.load(pickle_file);
        return item_max_diff;

    def check_title_not_used_file(self):
        return cf.check(self.title_not_used);

    def save_title_not_used(self, obj):
        fileobj = open(self.title_not_used, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_title_not_used(self):
        with open(self.title_not_used, 'rb') as pickle_file:
            titles_dict = Pickle.load(pickle_file);
        return titles_dict;

    def check_titles_list_file(self):
        return cf.check(self.titles_l_path);

    def save_titles_list(self, obj):
        fileobj = open(self.titles_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_titles_list(self):
        with open(self.titles_l_path, 'rb') as pickle_file:
            titles_dict = Pickle.load(pickle_file);
        return titles_dict;

    def check_titles_dict_file(self):
        return cf.check(self.titles_d_path);

    def save_titles_dict(self, obj):
        fileobj = open(self.titles_d_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_titles_dict(self):
        with open(self.titles_d_path, 'rb') as pickle_file:
            titles_dict = Pickle.load(pickle_file);
        return titles_dict;

    def check_tag_not_used_file(self):
        return cf.check(self.tags_not_used);

    def save_tag_not_used(self, obj):
        fileobj = open(self.tags_not_used, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_tag_not_used(self):
        with open(self.tags_not_used, 'rb') as pickle_file:
            titles_dict = Pickle.load(pickle_file);
        return titles_dict;

    def check_tags_list_file(self):
        return cf.check(self.tags_l_path);

    def save_tags_list(self, obj):
        fileobj = open(self.tags_l_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_tags_list(self):
        with open(self.tags_l_path, 'rb') as pickle_file:
            tags_dict = Pickle.load(pickle_file);
        return tags_dict;

    def check_tags_dict_file(self):
        return cf.check(self.tags_d_path);

    def save_tags_dict(self, obj):
        fileobj = open(self.tags_d_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_tags_dict(self):
        with open(self.tags_d_path, 'rb') as pickle_file:
            tags_dict = Pickle.load(pickle_file);
        return tags_dict;

    def check_item_min_time_file(self):
        return cf.check(self.item_min_time_path);

    def save_item_min_time(self, obj):
        fileobj = open(self.item_min_time_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_min_time(self):
        with open(self.item_min_time_path, 'rb') as pickle_file:
            item_min_time = Pickle.load(pickle_file);
        return item_min_time;
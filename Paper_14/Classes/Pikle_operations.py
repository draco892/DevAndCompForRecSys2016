"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import cPickle as Pickle
from Functions import Check_File as cf

#File contenente la classe che si occupa del salvataggio dei vari dizionari nei file .pik

class Pickle_operator:

    def __init__(self):
        self.users_d_path = 'Files_pik/users_d_lite.pik';
        self.int_l_path = 'Files_pik/int_l_lite.pik';
        self.int_d_path = 'Files_pik/int_d_lite.pik';
        self.item_imp_l_path = 'Files_pik/item_imp_l_lite.pik';
        self.imp_l_path = 'Files_pik/imp_l_lite.pik';
        self.imp_d_path = 'Files_pik/imp_d_lite.pik';
        self.item_score_d_path = 'Files_pik/item_score_d_lite.pik';
        self.item_list_path = 'Files_pik/item_list_lite.pik';
        self.users_list_path = 'Files_pik/users_list_lite.pik';
        self.filtered_pik_path = 'Files_pik/filtered.pik';

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

    def check_item_list_file(self):
        return cf.check(self.item_list_path);

    def save_item_list(self, obj):
        fileobj = open(self.item_list_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_item_list(self):
        with open(self.item_list_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_users_list_file(self):
        return cf.check(self.users_list_path);

    def save_users_list(self, obj):
        fileobj = open(self.users_list_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_users_list(self):
        with open(self.users_list_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;

    def check_filtered_file(self):
        return cf.check(self.filtered_pik_path);

    def save_filtered_file(self, obj):
        fileobj = open(self.filtered_pik_path, 'wb');
        Pickle.dump(obj, fileobj);
        fileobj.close();

    def load_filtered_file(self):
        with open(self.filtered_pik_path, 'rb') as pickle_file:
            items_d = Pickle.load(pickle_file);
        return items_d;
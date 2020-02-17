"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import sqlite3
import Read_data
from Functions import Sys_Flush


#file contenete la classe di funzioni riguardanti la creazione del dataset SQLite

#classe Riguardante la lettura dei dati da file

class Sqlite:

    #modulo riguardante l'inizializzazione della classe
    def __init__(self, l):
        self.fname_users = 'Dataset/users.csv';
        self.fname_items = 'Dataset/items.csv';
        self.fname_interactions = 'Dataset/interactions.csv';
        self.fname_impressions = 'Dataset/impressions.csv';

        self.users_c = 892;
        self.items_c = 892;
        self.interactions_c = 892;
        self.impressions_c = 892;

        if (l == True):
            self.conn = sqlite3.connect('File_db/recsys16_lite.db');
            self.items_l = [];
            self.users_l = [];
        else:
            self.conn = sqlite3.connect('File_db/recsys16.db');

    def create_users(self):
        self.users_c = 0;
        c = self.conn.cursor();
        c.execute('CREATE TABLE users \
            (id int not null primary key, career_level text, discipline_id text, industry_id text, \
            country text, region text, experience_n_entries_class text, experience_years_experience text,\
             experience_years_in_current text, edu_degree text)');
        c.execute('CREATE TABLE us_jobroles \
            (user_id int not null, jobrole text)');
        c.execute('CREATE TABLE us_fos \
            (user_id int not null, fos text)');

    def fill_users(self):
        if (self.users_c != 0):
            print "Error:\n\tNo Users Table create";
            return 1;
        reader = Read_data.reader();
        users = reader.read("users");
        user_dict = {}
        #unique_users = [];
        for u in users:
            if (u[0] not in user_dict):
                user_dict[u[0]] = u;
        #user_list = sorted([(u[0],u) for u in users]);
        c = self.conn.cursor();
        limit = 1;
        for i, k in enumerate(user_dict):
            line = user_dict[k];
            val = (int(line[0]), line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]);
            c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)", val);
            val_jobroles = line[1];
            for e, t in enumerate(val_jobroles):
                val_us_jobrole = (int(line[0]), t);
                c.execute("INSERT INTO us_jobroles VALUES (?,?)", val_us_jobrole);
            val_fos = line[11];
            for e, t in enumerate(val_fos):
                val_us_fos = (int(line[0]), t);
                if t != '0':
                    c.execute("INSERT INTO us_fos VALUES (?,?)", val_us_fos);
            if (i + 1) % 100000 == 0:
                print '\t\t%d processed' % (i + 1);
                Sys_Flush.fl();

    def fill_users_lite(self, n):
        if (self.users_c != 0):
            print "Error:\n\tNo Users Table create";
            return 1;
        reader = Read_data.reader();
        users = reader.read("users");
        user_dict = {};
        limit = 0;
        for u in users:
            if (u[0] not in user_dict):
                user_dict[u[0]] = u;
                limit = limit +1;
                if (limit >= n):
                    break;
        c = self.conn.cursor();
        for i, k in enumerate(user_dict):
            line = user_dict[k];
            val = (int(line[0]), line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]);
            self.users_l.append(int(line[0]));
            #print self.users_l;
            c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)", val);
            val_jobroles = line[1];
            for e, t in enumerate(val_jobroles):
                val_us_jobrole = (int(line[0]), t);
                c.execute("INSERT INTO us_jobroles VALUES (?,?)", val_us_jobrole);
            val_fos = line[11];
            for e, t in enumerate(val_fos):
                val_us_fos = (int(line[0]), t);
                if t != '0':
                    c.execute("INSERT INTO us_fos VALUES (?,?)", val_us_fos);
            if (i + 1) % 1000 == 0:
                print '\t\t%d processed' % (i + 1);
                Sys_Flush.fl();

    def create_items(self):
        self.items_c = 0;
        c = self.conn.cursor();
        c.execute('CREATE TABLE items \
            (id int not null primary key, career_level text, discipline_id text, industry_id text, \
            country text, region text, latitude text, longitude text, employment text,\
             created_at text, active_during_test text)');
        c.execute('CREATE TABLE it_titles \
            (item_id int not null, title text)');
        c.execute('CREATE TABLE it_tags \
            (item_id int not null, tag text)');

    def fill_items(self):
        if (self.items_c != 0):
            print "Error:\n\tNo Items Table create";
            return 1;
        it_file = open(self.fname_items);
        it_file.readline();
        c = self.conn.cursor();
        for i, line in enumerate(it_file):
            line = line.strip().split('\t');
            val = (
            int(line[0]), line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[11], line[12]);
            c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)", val);
            val_titles = line[1].strip().split(',');
            for e, t in enumerate(val_titles):
                val_it_title = (int(line[0]), t);
                c.execute("INSERT INTO it_titles VALUES (?,?)", val_it_title);
            val_tags = line[10].strip().split(',');
            for e, t in enumerate(val_tags):
                val_it_tag = (int(line[0]), t);
                c.execute("INSERT INTO it_tags VALUES (?,?)", val_it_tag);
            if (i+1)%100000==0:
                print '\t\t%d processed' % (i + 1);
                Sys_Flush.fl();

    def fill_items_lite(self):
        if (self.items_c != 0):
            print "Error:\n\tNo Items Table create";
            return 1;
        it_file = open(self.fname_items);
        it_file.readline();
        c = self.conn.cursor();
        for i, line in enumerate(it_file):
            line = line.strip().split('\t');
            val = (
            int(line[0]), line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[11], line[12]);
            if (((int(line[0])) in self.items_l) == True):
                c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)", val);
                val_titles = line[1].strip().split(',');
                for e, t in enumerate(val_titles):
                    val_it_title = (int(line[0]), t);
                    c.execute("INSERT INTO it_titles VALUES (?,?)", val_it_title);
                val_tags = line[10].strip().split(',');
                for e, t in enumerate(val_tags):
                    val_it_tag = (int(line[0]), t);
                    c.execute("INSERT INTO it_tags VALUES (?,?)", val_it_tag);
                if (i+1)%100000==0:
                    print '\t\t%d processed' % (i + 1);
                    Sys_Flush.fl();

    def create_interactions(self):
        self.interactions_c = 0;
        c = self.conn.cursor();
        c.execute('CREATE TABLE interactions \
            (user_id int not null, item_id int not null, interaction_type text, created_at text)');

    def fill_interactions(self):
        if (self.interactions_c != 0):
            print "Error:\n\tNo Interactions Table create";
            return 1;
        int_file = open(self.fname_interactions);
        int_file.readline();
        c = self.conn.cursor();
        for i, line in enumerate(int_file):
            #print 'fill_interactions:',i;
            line = line.strip().split('\t');
            val = (int(line[0]), int(line[1]), line[2], line[3]);
            c.execute("INSERT INTO interactions VALUES (?,?,?,?)", val);
            if (i + 1) % 100000 == 0:
                print '\t\t%d processed' % (i + 1);
                Sys_Flush.fl();

    def fill_interactions_lite(self):
        if (self.interactions_c != 0):
            print "Error:\n\tNo Interactions Table create";
            return 1;
        int_file = open(self.fname_interactions);
        int_file.readline();
        c = self.conn.cursor();
        for i, line in enumerate(int_file):
            #print 'fill_interactions:',i;
            line = line.strip().split('\t');
            val = (int(line[0]), int(line[1]), line[2], line[3]);
            if ((int(line[0]) in self.users_l) == True):
                if (((int(line[1])) in self.items_l) == False):
                    self.items_l.append(int(line[1]));
                c.execute("INSERT INTO interactions VALUES (?,?,?,?)", val);
                if (i + 1) % 100000 == 0:
                    print '\t\t%d processed' % (i + 1);
                    Sys_Flush.fl();
        #print self.items_l;

    def create_impressions(self):
        self.impressions_c = 0;
        c = self.conn.cursor();
        c.execute('CREATE TABLE impressions \
            (id int not null primary key, user_id int not null, year text, week text)');
        c.execute('CREATE TABLE imp_items \
            (imp_id int not null, item_id int not null, ord int)');

    def fill_impressions(self):
        if (self.impressions_c != 0):
            print "Error:\n\tNo Impressions Table create";
            return 1;
        imp_file = open(self.fname_impressions);
        imp_file.readline();
        c = self.conn.cursor();
        for i,line in enumerate(imp_file):
            #print 'fill_impressions:',i;
            line = line.strip().split('\t');
            val_imp = (i, int(line[0]), line[1], line[2]);
            c.execute("INSERT INTO impressions VALUES (?,?,?,?)", val_imp);
            items = line[3].strip().split(',');
            for e, it in enumerate(items):
                val_imp_item = (i, int(it), e);
                c.execute("INSERT INTO imp_items VALUES (?,?,?)", val_imp_item);
            if (i + 1) % 100000 == 0:
                print '\t\t%d processed' % (i + 1);
                Sys_Flush.fl();

    def fill_impressions_lite(self):
        if (self.impressions_c != 0):
            print "Error:\n\tNo Impressions Table create";
            return 1;
        imp_file = open(self.fname_impressions);
        imp_file.readline();
        c = self.conn.cursor();
        for i,line in enumerate(imp_file):
            #print 'fill_impressions:',i;
            line = line.strip().split('\t');
            val_imp = (i, int(line[0]), line[1], line[2]);
            if (((int(line[0])) in self.users_l) == True):
                c.execute("INSERT INTO impressions VALUES (?,?,?,?)", val_imp);
                items = line[3].strip().split(',');
                for e, it in enumerate(items):
                    val_imp_item = (i, int(it), e);
                    c.execute("INSERT INTO imp_items VALUES (?,?,?)", val_imp_item);
                    if (((int(it)) in self.items_l) == False):
                        self.items_l.append(int(it));
                if (i + 1) % 100000 == 0:
                    print '\t\t%d processed' % (i + 1);
                    Sys_Flush.fl();

    def end_read(self):
        self.conn.commit();
        self.conn.close();
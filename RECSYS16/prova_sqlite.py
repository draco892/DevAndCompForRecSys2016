
import sys
def fl():
    sys.stdout.flush()

import sqlite3
conn = sqlite3.connect('recsys16.db')

def create_interactions():
    c = conn.cursor()
    c.execute('CREATE TABLE interactions \
        (user_id int not null, item_id int not null, interaction_type text, created_at text)')

def fill_interactions():
    int_file = open('interactions.csv')
    int_file.readline()

    c = conn.cursor()
    for i,line in enumerate(int_file):
        #print 'fill_interactions:',i
        line = line.strip().split('\t')
        val = (int(line[0]),int(line[1]),line[2],line[3])
        c.execute("INSERT INTO interactions VALUES (?,?,?,?)",val)
        if (i+1)%100000==0:
            print '%d processed'%(i+1)
            fl()

print 'create interactions'
fl()
create_interactions()
fill_interactions()

def create_impressions():
    c = conn.cursor()
    c.execute('CREATE TABLE impressions \
        (id int not null primary key, user_id int not null, year text, week text)')
    c.execute('CREATE TABLE imp_items \
        (imp_id int not null, item_id int not null, ord int)')

def fill_impressions():
    imp_file = open('impressions.csv')
    imp_file.readline()

    c = conn.cursor()
    for i,line in enumerate(imp_file):
        #print 'fill_impressions:',i
        line = line.strip().split('\t')
        val_imp = (i,int(line[0]),line[1],line[2])
        c.execute("INSERT INTO impressions VALUES (?,?,?,?)",val_imp)
        items = line[3].strip().split(',')
        for e,it in enumerate(items):
            val_imp_item = (i,int(it),e)
            c.execute("INSERT INTO imp_items VALUES (?,?,?)",val_imp_item)
        if (i+1)%100000==0:
            print '%d processed'%(i+1)
            fl()
            
print 'create impressions'
fl()
create_impressions()
fill_impressions()

def create_items():
    c = conn.cursor()
    c.execute('CREATE TABLE items \
        (id int not null primary key, career_level text, discipline_id text, industry_id text, \
        country text, region text, latitude text, longitude text, employment text, created_at text, active_during_test text)')
    c.execute('CREATE TABLE it_titles \
        (item_id int not null, title text)')
    c.execute('CREATE TABLE it_tags \
        (item_id int not null, tag text)')
    
def fill_items():
    it_file = open('items.csv')
    it_file.readline()

    c = conn.cursor()
    for i,line in enumerate(it_file):
        line = line.strip().split('\t')
        val = (int(line[0]),line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[11],line[12])
        c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
        val_titles = line[1].strip().split(',')
        for e,t in enumerate(val_titles):
            val_it_title = (int(line[0]),t)
            c.execute("INSERT INTO it_titles VALUES (?,?)",val_it_title)
        val_tags = line[10].strip().split(',')
        for e,t in enumerate(val_tags):
            val_it_tag = (int(line[0]),t)
            c.execute("INSERT INTO it_tags VALUES (?,?)",val_it_tag)  
        
        if (i+1)%100000==0:
            print '%d processed'%(i+1)
            fl()

print 'create items'
fl()
create_items()
fill_items()

def create_users():
    c = conn.cursor()
    c.execute('CREATE TABLE users \
        (id int not null primary key, career_level text, discipline_id text, industry_id text, \
        country text, region text, experience_n_entries_class text, experience_years_experience text, experience_years_in_current text, edu_degree text)')
    c.execute('CREATE TABLE us_jobroles \
        (user_id int not null, jobrole text)')
    c.execute('CREATE TABLE us_fos \
        (user_id int not null, fos text)')

def fill_users():
    import leggi
    users = leggi.users()
    user_dict = {}
    for u in users:
        user_dict[u[0]]=u

    #user_list = sorted([(u[0],u) for u in users])
    
    c = conn.cursor()
    for i,k in enumerate(user_dict):
        line = user_dict[k]
        val = (int(line[0]),line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?)",val)
        val_jobroles = line[1]
        for e,t in enumerate(val_jobroles):
            val_us_jobrole = (int(line[0]),t)
            c.execute("INSERT INTO us_jobroles VALUES (?,?)",val_us_jobrole)
        val_fos = line[11]
        for e,t in enumerate(val_fos):
            val_us_fos = (int(line[0]),t)
            if t!='0': 
                c.execute("INSERT INTO us_fos VALUES (?,?)",val_us_fos)  
        
        if (i+1)%100000==0:
            print '%d processed'%(i+1)
            fl()
print 'create users'
fl()
create_users()
fill_users()

conn.commit()
conn.close()

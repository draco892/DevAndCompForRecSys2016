import sys,time

def fl():
    sys.stdout.flush()

import unixtime as ut

import sqlite3
conn = sqlite3.connect('recsys16.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def user2items():
    c.execute('select user_id,item_id from interactions \
        where interaction_type="1" or interaction_type="2" \
        or interaction_type="3"')
    u2i = {}
    for row in c:
        if row['user_id'] not in u2i:
            u2i[row['user_id']]=set()
        u2i[row['user_id']].add(row['item_id'])
    return u2i

def item2users():
    c.execute('select user_id,item_id from interactions \
        where interaction_type="1" or interaction_type="2" \
        or interaction_type="3"')
    i2u = {}
    for row in c:
        if row['item_id'] not in i2u:
            i2u[row['item_id']]=set()
        i2u[row['item_id']].add(row['user_id'])
    return i2u

def active_items():
    c.execute('select id from items where active_during_test="1"')
    return c

def stat_items():
    c.execute('select id,career_level,discipline_id,industry_id,\
    country,region,employment,active_during_test from items')
    d = {'career_level':{},'discipline_id':{},'industry_id':{},'country':{},
         'region':{},'employment':{},'active_during_test':{}}
    for row in c:
        for s in ('career_level','discipline_id','industry_id',
        'country','region','employment','active_during_test'):
            if row[s] not in d[s]:
                d[s][row[s]] = 0
            d[s][row[s]]+=1
    return d

def stat_users():
    c.execute('select id,career_level,discipline_id,industry_id,\
    country,region,experience_n_entries_class,experience_years_experience,\
    experience_years_in_current,edu_degree from users')
    names = ('career_level','discipline_id','industry_id',
    'country','region','experience_n_entries_class','experience_years_experience',
    'experience_years_in_current','edu_degree')
    d = {names[0]:{},names[1]:{},names[2]:{},names[3]:{},
         names[4]:{},names[5]:{},names[6]:{},names[7]:{},
         names[8]:{}}
    for row in c:
        for s in names:
            if row[s] not in d[s]:
                d[s][row[s]] = 0
            d[s][row[s]]+=1
    return d

def user2jr():
    c.execute('select user_id,jobrole from us_jobroles')
    u2jr = {}
    for row in c:
        if row[0] not in u2jr:
            u2jr[row[0]]=set()
        u2jr[row[0]].add(row[1])
    return u2jr

def user2fos():
    c.execute('select user_id,tag from us_fos')
    u2fos = {}
    for row in c:
        if row[0] not in u2fos:
            u2fos[row[0]]=set()
        u2fos[row[0]].add(row[1])
    return u2fos

def a2b(field1,field2,table):
    c.execute('select %s,%s from %s'%(field1,field2,table))
    a2b = {}
    for row in c:
        if row[0] not in a2b:
            a2b[row[0]]=set()
        a2b[row[0]].add(row[1])
    return a2b

def valid_items():
    import unixtime as ut
    c.execute('select item_id,interaction_type,created_at from interactions')
    vi = {}
    for row in c:
        dt = ut.convert(int(row[2]))
        if dt.year==2015 and dt.month==11:
            if row[0] not in vi:
                vi[row[0]]=list()
            vi[row[0]].append((dt.year,dt.month,dt.day))
    return vi

def frequencies(fu,fi):
    t = time.clock()
    print 'executing query'
    c.execute('select users.%s,items.%s from users,items,interactions \
        where (interactions.interaction_type=1 or interactions.interaction_type=2 or interactions.interaction_type=3) \
        and (interactions.user_id=users.id and interactions.item_id=items.id)'%(fu,fi))
    print 'producing results..'
    d={}
    for i,row in enumerate(c):
        p = (row[0],row[1])
        if p not in d:
            d[p]=0
        d[p]+=1
        if (i+1)%100000==0:
            print "%dk"%((i+1)/1000)
    print 'done in %d secs!'%(time.clock()-t)
    return d
#conn.close()

def run_freq(fu,fi):
    t = time.clock()
    print 'executing query'
    c.execute('select count(*),users.%s,items.%s from users,items,interactions \
        where (interactions.interaction_type=1 or interactions.interaction_type=2 or interactions.interaction_type=3) \
        and (interactions.user_id=users.id and interactions.item_id=items.id) \
        group by users.%s,items.%s'%(fu,fi,fu,fi))
    d = {}
    for row in c:
        d[(row[1],row[2])]=row[0]
    print 'done in %d secs!'%(time.clock()-t)
    return d

def test_v_interactions():
    u2i_test = {}
    i2u_test = {}
    item_set = set()
    c.execute('select user_id, item_id, interaction_type, created_at from interactions')
    for r in c:
        #print r
        u = r[0]
        i = r[1]
        i_type = r[2]
        c_at = r[3]
        if ut.convert(int(c_at)).month == 11:
            item_set.add(i)
            if i_type == '1' or i_type == '2' or i_type == '3':
                if u not in u2i_test:
                    u2i_test[u]=set()
                u2i_test[u].add(i)
                if i not in i2u_test:
                    i2u_test[i]=set()
                i2u_test[i].add(u)
    return (u2i_test,i2u_test,item_set)

def train_v_interactions():
    u2i_train = {}
    i2u_train = {}
    item_set = set()
    c.execute('select user_id, item_id, interaction_type, created_at from interactions')
    for r in c:
        #print r
        u = r[0]
        i = r[1]
        i_type = r[2]
        c_at = r[3]
        if ut.convert(int(c_at)).month < 11:
            item_set.add(i)
            if i_type == '1' or i_type == '2' or i_type == '3':
                if u not in u2i_train:
                    u2i_train[u]=set()
                u2i_train[u].add(i)
                if i not in i2u_train:
                    i2u_train[i]=set()
                i2u_train[i].add(u)
    return (u2i_train,i2u_train,item_set)

def target_users():
    f = open('target_users.csv')
    f.readline()
    tu = []
    for line in f:
        tu.append(int(line))
    return tu

def target_items():
    c.execute('select id from items where active_during_test=1')
    s = set()
    for r in c:
        s.add(r[0])
    return s

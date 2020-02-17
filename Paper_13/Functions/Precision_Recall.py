"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

#File contenente le funzioni Precision, Recall, User Succes ed User Score

def Precision_lim(v,lim,ts):
    sc_s_occ = 1.0 / lim;
    score = 0.0;
    for i in range(0,lim):
        value = v[i];
        for j in range(0,len(ts)):
            if (ts[j] == value):
                score += sc_s_occ;
    return score;

def Recall(v,ts):
    sc_s_occ = 1.0 / len(ts);
    score = 0.0;
    for i in range(0,len(v)):
        value = v[i];
        for j in range(0,len(ts)):
            if (ts[j] == value):
                score += sc_s_occ;
    return score;

def user_succ(v,ts):
    for i in range(0,len(v)):
        for j in range(0,len(ts)):
            if v[i] == ts[j]:
                return 1.0;
    return 0.0;

def user_score(p2,p4,p6,p20,r,s):
    return 20.0*(p2+p4+r+s)+10.0*(p6+p20);

def Score_Calc(v,ts):
    p2 = Precision_lim(v,2,ts);
    p4 = Precision_lim(v,4,ts);
    p6 = Precision_lim(v,6,ts);
    p20 = Precision_lim(v,20,ts);
    r = Recall(v,ts);
    s = user_succ(v,ts);
    score = user_score(p2,p4,p6,p20,r,s);
    return score;
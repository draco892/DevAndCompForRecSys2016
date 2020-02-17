"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from itertools import izip

#Fine contenente le funzioni riguardanti il calcolo della similarita coseno

def dot_product(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)));

def cosine_similarity_vector(v1, v2,den_v1,den_v2):
    prod = dot_product(v1, v2);
    len1 = den_v1;
    len2 = den_v2;
    sim_score = prod / (len1 * len2)
    return sim_score;

def prod_calc_dict(d1,d2):
    prod = 0;
    for key in d1:
        prod += d1[key]*d2[key];
    return 0;

def cosine_similarity_dict(d1,d2,den_d1,den_d2):
    if (len(d1)<len(d2)):
        prod = prod_calc_dict(d1,d2);
    else:
        prod = prod_calc_dict(d2, d1);
    sim_score = prod / (den_d1 * den_d2);
    return sim_score;

def cosine_sim(tags_d_1,tags_d_2,tags_den_1,tags_den_2,titles_d_1,titles_d_2,titles_den_1,titles_den_2,\
               v1,v2,den_v1,den_v2):
    score = 0.0;
    if (len(tags_d_1) > 0) and (len(tags_d_2) > 0):
        score += cosine_similarity_dict(tags_d_1,tags_d_2,tags_den_1,tags_den_2);
    if (len(titles_d_1) > 0) and (len(titles_d_2) > 0):
        score += cosine_similarity_dict(titles_d_1,titles_d_2,titles_den_1,titles_den_2);
    score += cosine_similarity_vector(v1,v2,den_v1,den_v2);
    return score;
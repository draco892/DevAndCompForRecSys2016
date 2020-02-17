"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

from Functions import Sim_I_O as iknn
from Functions import Meta_Cosine as m_c
from Functions import Precision_Recall as p_r
from Functions import Top_30_list as t30

#file contenete la classe riguardante i predittori

class Predictors:

    # Modulo riguardante l'inizializzazione della classe
    def __init__(self, score_dict):
        self.final_score_dict = score_dict;

    def All_predictors_calc(self,u_v,lim_tr,per_ts,imp_d,item_dict,fos_d,\
                            jobroles_d,lambd,alpha):
        us_ts = u_v[12][per_ts][5];
        w_e = u_v[12][lim_tr][2];
        RCTR_score = u_v[12][lim_tr][3];
        AS_score_1 = u_v[12][lim_tr][4][0];
        AS_score_3 = u_v[12][lim_tr][4][2];
        AS_score_4 = u_v[12][lim_tr][4][3];
        base_score = RCTR_score + AS_score_1 + AS_score_3 + AS_score_4;
        for item_id in item_dict:
            #print item_id;
            Upop_score = u_v[11];
            AP_score = item_dict[item_id][14];
            Upop_sum_sc = 0.0;
            iknn_score = 0.0;
            ms_score = 0.0;

            #Upop
            if (len(u_v[9])>0):
                for i in range(0, len(u_v[9])):
                    fos_id = u_v[9][i];
                    pop_g = fos_d[fos_id][2][lim_tr][item_id];
                    Upop_sum_sc += pop_g / (pop_g + lambd);
                    del pop_g;
            if (len(u_v[10])>0):
                for i in range(0, len(u_v[10])):
                    jobroles_id = u_v[10][i];
                    pop_g = jobroles_d[jobroles_id][2][lim_tr][item_id];
                    Upop_sum_sc += pop_g / (pop_g + lambd);
                    del pop_g;

            # Interactions
            if (len(u_v[12][lim_tr][0])):
                for i in range(0,len(u_v[12][lim_tr][0])):
                    item_event_id = u_v[12][lim_tr][0][i][0];
                    par_we = u_v[12][lim_tr][0][i][3];
                    if (item_event_id != item_id):
                        iknn_score += par_we * iknn.sim_calc_CC(item_dict,lim_tr,\
                                                                item_event_id, item_id,\
                                                                lambd, alpha);
                        iknn_score += par_we * iknn.sim_calc_RR(item_dict, lim_tr,\
                                                                item_event_id, item_id,\
                                                                lambd, alpha);
                        iknn_score += par_we * iknn.sim_calc_RC(item_dict, lim_tr,\
                                                                item_event_id, item_id,\
                                                                lambd, alpha);
                    ms_score += par_we * m_c.cosine_sim(item_dict[item_id][12],\
                                                        item_dict[item_event_id][12],\
                                                        item_dict[item_id][16],\
                                                        item_dict[item_event_id][16],\
                                                        item_dict[item_id][11],\
                                                        item_dict[item_event_id][11],\
                                                        item_dict[item_id][15],\
                                                        item_dict[item_event_id][15],
                                                        item_dict[item_id][13],\
                                                        item_dict[item_event_id][13],\
                                                        item_dict[item_id][17],\
                                                        item_dict[item_event_id][17]);

            # Impressions
            if (len(u_v[12][lim_tr][1]) > 0):
                for i in range(0,len(u_v[12][lim_tr][1])):
                    imp_id = u_v[12][lim_tr][1][i];
                    score_single_imp = imp_d[imp_id][6];
                    if (imp_d[imp_id][4] > 0):
                        for item_event_id in imp_d[imp_id][5]:
                            nr_times = imp_d[imp_id][5][item_event_id];
                            par_we = score_single_imp * nr_times;
                            if (item_event_id != item_id):
                                iknn_score += par_we * iknn.sim_calc_CC(item_dict,lim_tr,\
                                                                        item_event_id,\
                                                                        item_id,lambd,\
                                                                        alpha);
                                iknn_score += par_we * iknn.sim_calc_RR(item_dict,lim_tr,\
                                                                        item_event_id,\
                                                                        item_id,lambd,\
                                                                        alpha);
                                iknn_score += par_we * iknn.sim_calc_RC(item_dict,lim_tr,\
                                                                        item_event_id,\
                                                                        item_id,lambd,\
                                                                        alpha);
                            ms_score += par_we * m_c.cosine_sim(item_dict[item_id][12], \
                                                                item_dict[item_event_id][12], \
                                                                item_dict[item_id][16], \
                                                                item_dict[item_event_id][16], \
                                                                item_dict[item_id][11], \
                                                                item_dict[item_event_id][11], \
                                                                item_dict[item_id][15], \
                                                                item_dict[item_event_id][15],
                                                                item_dict[item_id][13], \
                                                                item_dict[item_event_id][13], \
                                                                item_dict[item_id][17],\
                                                                item_dict[item_event_id][17]);

            Upop_score *= Upop_sum_sc;
            iknn_score *= w_e;
            ms_score *= w_e;
            self.final_score_dict[item_id] = base_score + AP_score +\
                                             Upop_score + iknn_score + ms_score;
            #print self.final_score_dict[item_id];

        # Calcolo score user
        top30_l = t30.creation_top30_list(self.final_score_dict);
        us_sc = p_r.Score_Calc(top30_l,us_ts);
        #print us_ts;
        #print top30_l;
        #for j in range(0,len(top30_l)):
            #print self.final_score_dict[top30_l[j]];
        #print us_sc;

        return us_sc;
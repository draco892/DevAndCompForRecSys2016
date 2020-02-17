"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import random
import cPickle as pickle

# File contenente la classe Predictors

class Pred:
    # Generic Predictor
    def __init__(self, rep_users, rep_items, item_set, filtered):
        self.u_rep = rep_users;
        self.i_rep = rep_items;
        self.item_set = item_set;
        self.filtered = filtered;
        self.scores = {};

    def save_scores(self, fname):
        pickle.dump(self.scores, open(fname, "wb"));

    def load_scores(self, fname):
        print "Loading scores...";
        self.scores = pickle.load(open(fname, "rb"));
        print "Done!";
        return self.scores;

    # Random
    def score_items(self, u):
        if u in self.scores:
            return self.scores[u];
        d = {}
        for i in self.item_set:
            d[i] = random.random();
        self.scores[u] = d;
        return self.scores[u];

    def score(self, u, i):
        if u in self.scores:
            if i in self.scores[u]:
                return self.scores[u][i];
        return random.random();

class PredU(Pred):
    # UB based predictor
    def __init__(self,rep_users, rep_items, item_set, filtered):
        Pred.__init__(self, rep_users, rep_items, item_set, filtered);

    def score_items(self, u):
        if u in self.scores:
            return self.scores[u];
        sco = {};
        for ind, i in enumerate(self.filtered[u]):
            sco[i] = 0.0;
            if i in self.i_rep.data:
                ir = self.i_rep.get(i);
                for v in ir:
                    sco[i] += self.u_rep.get(u, v);
            # Normalizzazione
            if sco[i] != 0.0:
                sco[i] /= self.u_rep.norm(u) * self.i_rep.norm(i);
        self.scores[u] = sco;
        return self.scores[u];

    def score(self, u, i):
        if u in self.scores:
            if i in self.scores[u]:
                return self.scores[u][i];
        sco = 0.0
        if i in self.filtered[u]:
            if i in self.i_rep.data:
                ir = self.i_rep.get(i);
                for v in ir:
                    sco += self.u_rep.get(u, v);
        # Normalizzazione
        if sco != 0.0:
            sco /= self.u_rep.norm(u) * self.i_rep.norm(i);
        return sco;

class PredI(Pred):
    #IB based predictor
    def __init__(self, rep_users, rep_items, item_set, filtered):
        Pred.__init__(self, rep_users, rep_items, item_set, filtered);

    def score_items(self, u):
        if u in self.scores:
            return self.scores[u];
        sco = {};
        ur = self.u_rep.get(u);
        for ind, i in enumerate(self.filtered[u]):
            sco[i] = 0.0;
            if i in self.i_rep.data:
                for j in ur:
                    sco[i] += self.i_rep.get(i, j);
            # Normalizzazione
            if sco[i] != 0.0:
                sco[i] /= self.i_rep.norm(i) * self.u_rep.norm(u);
        self.scores[u] = sco;
        return self.scores[u];

    def score(self, u, i):
        if u in self.scores:
            if i in self.scores[u]:
                return self.scores[u][i];
        sco = 0.0;
        if i in self.filtered[u]:
            if i in self.i_rep.data:
                if u in self.u_rep.data:
                    ur = self.u_rep.get(u);
                    for j in ur:
                        sco += self.i_rep.get(i, j);
        # Normalizzazione
        if sco != 0.0:
            sco /= self.i_rep.norm(i) * self.u_rep.norm(u);
        return sco;

class PredPO(Pred):
    #Popularity based predictor
    def __init__(self, rep_users, rep_items, item_set, filtered):
        Pred.__init__(self, rep_users, rep_items, item_set, filtered);

    def score_items(self, u):
        sco = {};
        for i in self.filtered[u]:
            if i not in self.scores:
                if i not in self.i_rep.data:
                    self.scores[i] = 0.0;
                else:
                    self.scores[i] = len(self.i_rep.get(i)) / (self.i_rep.norm(i) * self.u_rep.norm(u));
            sco[i] = self.scores[i];
        return sco;

    def score(self, u, i):
        if i in self.scores:
            return self.scores[i]
        if i not in self.filtered[u]:
            return 0.0;
        if i not in self.i_rep.data:
            return 0.0;
        return len(self.i_rep.get(i)) / (self.i_rep.norm(i) * self.u_rep.norm(u));
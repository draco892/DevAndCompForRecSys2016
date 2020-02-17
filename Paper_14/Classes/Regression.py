"""
@author: Andrea Domenico Giuliano
@contact: andreadomenico.giuliano@studenti.unipd.it
@organization: University of Padua
"""

import cvxopt as co
import cvxopt.solvers as solver
from Functions import Utils as ut
from datetime import datetime

# File contenente la classe Regression e Regression2

class Regression():
    def __init__(self, predictors, target_users, filtered, u2i_train, c=[0.75, 0.25], lamb=0.00):
        self.c = c
        self.u2i = u2i_train
        self.target_users = target_users
        self.filtered = filtered
        self.predictors = predictors
        self.lamb = lamb
        self.eta = {}

    def train(self):
        K = len(self.predictors)

        for u in self.filtered:
            inizio_t = datetime.now();
            #print u
            S = co.matrix(0.0, (K, K));
            Sp = co.matrix(0.0, (K, 1));

            for i in self.filtered[u]:
                neg = u not in self.u2i or not (i in self.u2i[u]);
                coeff = self.c[neg];
                # print neg;

                si = co.matrix([[p.score(u, i) for p in self.predictors]]);
                ki = si * si.T;
                S += coeff * ki;

                if not neg:
                    Sp += si;

            Sp *= self.c[0];
            S += ut.diag(co.matrix([self.lamb] * K))

            G = -ut.identity(K)
            h = ut.zeroes_vec(K)
            A = ut.ones_vec(K).T
            b = co.matrix([[1.0]], (1, 1))

            solver.options['show_progress'] = False;  # True
            sol = solver.qp(S, Sp, G, h, A, b);
            # eta:
            self.eta[u] = sol['x'];
            #print self.eta[u]
            fine_t = datetime.now();
            #print (fine_t - inizio_t);
        #return self.eta;

    def get_params(self):
        return {"cp": self.c[0], "cn": self.c[1]};

class Regression2():
    def __init__(self, predictors, S, labels, u2i_train, c=[0.75, 0.25], lamb=0.00):
        self.c = c;
        self.u2i = u2i_train;
        self.S = S;
        self.labels = labels;
        self.predictors = predictors;
        self.lamb = lamb;
        self.eta = {};

    def train(self):
        K = len(self.predictors)

        S = co.matrix(0.0, (K, K));
        Sp = co.matrix(0.0, (K, 1));

        #print S;
        #print Sp;
        #print S.size[0];

        #for i in S.size[0]:
        for i in range(0,S.size[0]):
            coeff = self.c[0 if self.labels > 0 else 1];
            si = S[i, :].T;
            ki = si * si.T;
            S += coeff * ki;

        Sp *= self.c[0];
        S += ut.diag(co.matrix([self.lamb] * K));

        G = -ut.identity(K);
        h = ut.zeroes_vec(K);
        A = ut.ones_vec(K).T;
        b = co.matrix([[1.0]], (1, 1));

        solver.options['show_progress'] = False;  # True
        sol = solver.qp(S, Sp, G, h, A, b);
        #print sol;
        self.eta = sol['x'];
        return self.eta;

    def get_params(self):
        return {"cp": self.c[0], "cn": self.c[1]};
#coding: utf-8

import numpy as np

class MovieBase():


    def read_from_csv(self, file_path):
        f = open(file_path, 'r')
        self.matrix = np.loadtxt(f, delimiter=',')
        self.shape = self.matrix.shape
        f.close()

    def get_user_unseen_films(self, user_idx):
        if user_idx >= self.shape[1]:
            raise ValueError(u"Matrix only has {} rows. Cannot access row {}".format(self.shape[0], user_idx))

        return [i for i, rating in enumerate(self.matrix[user_idx]) if rating == 0]

    def normalize_base(self):
        self.user_means = self._get_user_means()

        print self.user_means

        movie_ratings = self._replace_zero_entries(self.matrix)

        # Replacing the 0 entries by the mean rating of the
        #   movie of the col it is located in
        self.norm_matrix = self.matrix + movie_ratings

        # Subtracting the mean rating for each user from its row
        user_means = self._subtract_row_means(self.norm_matrix)

        self.norm_matrix += user_means

    def _get_user_means(self):
        means = []

        for row in self.matrix:
            row_mean = np.mean(filter(lambda rating: rating != 0, row))
            means.append(row_mean)

        #return means

        return self.matrix.mean(axis=1)

    def _subtract_row_means(self, matrix):
        # M is the matrix
        _m = np.ones(self.shape)

        row_means = self.matrix.mean(axis=1)

        for i, row in enumerate(matrix):
            _m *= -row_means[i]

        return _m


    def _replace_zero_entries(self, matrix):
        
        _m = np.zeros(self.shape)

        for j in range(self.shape[1]):
            col = matrix[:, j]
            col_mean = np.mean(filter(lambda rating: rating != 0, col))

            for i, row in enumerate(col):
                if row == 0:
                    _m[i, j] = col_mean

        return _m

    def factor_svd(self):

        self.U, self._S, self.V_t = np.linalg.svd(self.norm_matrix, full_matrices=True)
        #self.U, self._S, self.V_t = np.linalg.svd(self.matrix, full_matrices=True)
        self.S = np.diag(self._S)

    def low_rank_approximate(self, k):
        self.U_k = self.U[:,range(k)]
        self.S_k = np.diag(self._S[:k])
        self._S_k = np.diag(self.S_k)
        self.Vk_t = self.V_t[range(k)]

        self.R_k = self.U_k.dot(self.S_k).dot(self.Vk_t)

    def build_aspect_matrices(self):
        # user-aspect = Uk * sqrt(Sk)
        self.user_aspect = self.U_k.dot(np.sqrt(self.S_k))

        # movie-aspect = sqrt(Sk) * Vk_t
        self.movie_aspect = np.sqrt(self.S_k).dot(self.Vk_t)

        print self.user_aspect
        print self.movie_aspect

    def get_prediction(self, user, movie):
        rating = self.user_aspect[user].dot(self.movie_aspect[:, movie]) #+ self.user_means[user]

        return int(rating)

    def do_stuff(self):
        self.read_from_csv('test.csv')

        unseen = {}

        for i in range(self.shape[0]):
            unseen_list = self.get_user_unseen_films(user_idx=i)
            if unseen_list:
                unseen[i] = unseen_list
        
        self.normalize_base()
        self.factor_svd()
        self.low_rank_approximate(k=2)
        self.build_aspect_matrices()

        for user, movie_list in unseen.iteritems():
            for movie in movie_list:
                prediction = self.get_prediction(user=user, movie=movie)
                print "Prediction for user {} and movie {}: {}".format(user, movie, prediction)

        # l_r_appr = np.zeros(self.shape)

        # for i in range(k):
        #     l_r_appr += self._S[i] * np.dot(self.U.transpose()[i], self.V_t[:,i])

        # print l_r_appr

        # Uk, _Sk, Vk_t = np.linalg.svd(l_r_appr, full_matrices=True)

        # print "Uk: {}".format(Uk)

        # print "_Sk: {}".format(_Sk)

        # print "Vk_t: {}".format(Vk_t)



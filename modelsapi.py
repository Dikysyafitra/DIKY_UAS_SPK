
import numpy as np
import pandas as pd

class Movie():
    def __init__(self) -> None:
        self.movies = pd.read_csv('ml-latest-small/movies.csv')
        self.matrix = pd.read_csv('ml-latest-small/matrix_by_id.csv')
        self.films = np.array(self.movies)

    @property
    def film_data(self):
        data = []
        for film in self.films:
            data.append({'movie_id': film[0],'movie_title': film[1]})
        return data

    @property
    def film_data_dict(self):
        data = {}
        for film in self.films:
            data[film[0]] = film[1] 
        return data
    
    def pearson(self, s1, s2):
        s1_c = s1-s1.mean()
        s2_c = s2-s2.mean()
        return np.sum(s1_c*s2_c)/np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))
    
    def get_recs(self, movie_id, num):
        reviews = []
        movie_id = str(movie_id)
        for id in self.matrix.columns:
            if id == movie_id:
                continue
            cor = self.pearson(self.matrix[movie_id], self.matrix[id])
            if np.isnan(cor):
                continue
            else:
                reviews.append((id, cor))
            reviews.sort(key=lambda tup: tup[1], reverse=True)
        return reviews[:num]

class LaptopRecommender:
    def __init__(self):
        self.leptop = pd.read_csv('ml-latest-small/tbl_laptop.csv')
        self.matrix_lp = pd.read_csv('ml-latest-small/matrix_laptop.csv')
        self.lpt = self.leptop.to_numpy()

    @property
    def lppt_data(self):
        data = [{'ID': lppt[0], 'brand_title': lppt[2]} for lppt in self.lpt]
        return data

    @property
    def lppt_data_dict(self):
        data = {lppt[0]: lppt[2] for lppt in self.lpt}
        return data

    def pearson(self, s1, s2):
        s1_c = s1 - s1.mean()
        s2_c = s2 - s2.mean()
        numerator = np.sum(s1_c * s2_c)
        denominator = np.sqrt(np.sum(s1_c**2) * np.sum(s2_c**2))
        if denominator == 0:
            return 0  # Handle the case where the denominator is zero to avoid division by zero
        return numerator / denominator

    def get_recs(self, ID, num):
        reviews = []
        ID = str(ID)
        for ID in self.matrix_lp.columns:
            if ID == ID:
                continue
            cor = self.pearson(self.matrix_lp[ID], self.matrix_lp[ID])
            if not np.isnan(cor):
                reviews.append((ID, cor))

        reviews.sort(key=lambda tup: tup[1], reverse=True)
        return reviews[:num]

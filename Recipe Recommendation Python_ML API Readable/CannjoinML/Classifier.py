import re
import unidecode
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, recall_score, precision_score
import xgboost as xgb
from sklearn import preprocessing
import pickle

class cannjoin_xgboost:
    
    def __init__(self):
        print('Created')

    def classifyReview(self, raw_json):
        
        review_df = pd.DataFrame.from_dict(raw_json, orient='index')
        
        review_df = review_df.drop(['strain_id','username', 'comment', 'strain_id', 'commnet_polarity', 'comment_subjectivity', 'rating'], axis=1)
        
        review_df['hybrid'] = review_df.hybrid.astype(float)
        review_df['sativa'] = review_df.sativa.astype(float)
        review_df['indica'] = review_df.indica.astype(float)
        review_df['is_desert'] = review_df.is_desert.astype(float)
        review_df['uses_butter'] = review_df.uses_butter.astype(float)
        review_df['uses_oil'] = review_df.uses_oil.astype(float)
        review_df['relief'] = review_df.relief.astype(int)
        
        # Lets now normalize the floating point attirbutes between 0-1 that needs it
        review_df['cooking_time_min'] = (review_df['cooking_time_min']-review_df['cooking_time_min'].min()) / (review_df['cooking_time_min'].max()-review_df['cooking_time_min'].min())
        review_df['thc_percent'] = (review_df['thc_percent']-review_df['thc_percent'].min()) / (review_df['thc_percent'].max()-review_df['thc_percent'].min())
        review_df['cbd_percent'] = (review_df['cbd_percent']-review_df['cbd_percent'].min()) / (review_df['cbd_percent'].max()-review_df['cbd_percent'].min())
        review_df['avg_subjectivity'] = (review_df['avg_subjectivity']-review_df['avg_subjectivity'].min()) / (review_df['avg_subjectivity'].max()-review_df['avg_subjectivity'].min())
        review_df['avg_polarity'] = (review_df['avg_polarity']-review_df['avg_polarity'].min()) / (review_df['avg_polarity'].max()-review_df['avg_polarity'].min())
        review_df['avg_rating'] = (review_df['avg_rating']-review_df['avg_rating'].min()) / (review_df['avg_rating'].max()-review_df['avg_rating'].min())
        review_df['oven_percentage_power'] = (review_df['oven_percentage_power']-review_df['oven_percentage_power'].min()) / (review_df['oven_percentage_power'].max()-review_df['oven_percentage_power'].min())
        review_df['percent_serving_weight_weed_ingredient'] = (review_df['percent_serving_weight_weed_ingredient']-review_df['percent_serving_weight_weed_ingredient'].min()) / (review_df['percent_serving_weight_weed_ingredient'].max()-review_df['percent_serving_weight_weed_ingredient'].min())
        
        
        review_df = pd.get_dummies(review_df, columns=['condition'])
        
        bins = [-np.inf, 0.65, 0.8, 1.0]
        labels=['cool','moderate','hot']
        review_df['oven_power_cat'] = pd.cut(review_df.oven_percentage_power, bins=bins, labels=labels)
        
        review_df = pd.get_dummies(review_df, columns=['oven_power_cat'])
        
        review_df = review_df.drop(['oven_percentage_power'], axis=1)


        current_classifier = pickle.load(open("classifier.pickle.dat", "rb"))
        prediction = current_classifier.predict(review_df)
            
        return {'with_provide_relief'}



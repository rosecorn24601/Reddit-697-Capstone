import pandas as pd
import numpy as np  
import psycopg2 
from functions import Team_Augury_SQL_func
from functions.Team_Augury_feature_functions import generate_features_csv, feature_to_x_y
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import pickle

rnd_state = 42

choice = input("Load data (Y) or Run full featurization (N)?:").upper()

if choice == 'N':

  # connect to database
  print("Connecting to database and loading posts/comments...")
  conn = psycopg2.connect(
      host = 'capstone697.czsaza7am68b.us-east-1.rds.amazonaws.com' ,
      port = '5432',
      database = 'Capstone697', 
      user = 'read_o',  
      password = 'EAC697Reddit' , 
      connect_timeout=3)

  ### NEW SQL Variables
  sr_id = '(4, 31760, 31764, 31766)'   #[(4, '2qhhq', 'investing'), (16, 'mouw', 'science'), (130, '2qh1i', 'AskReddit'), (18162, '2qh3l', 'news'), (31760, '2qjuv', 'StockMarket'), (31764, '2qjfk', 'stocks'), (31766, '2th52', 'wallstreetbets')]
  lower_timestamp = '2022-04-18 11:00:00'
  upper_timestamp = '2022-04-21 01:00:00' 

  #get data
  post_data, comments_data = Team_Augury_SQL_func.sql_by_timestamp(conn,sr_id,lower_timestamp,upper_timestamp)
  print("Loaded {} posts".format(len(post_data.post_id.unique())))
  print("Loaded {} comments".format(len(comments_data.post_id.unique())))

  csv_folder = "saved_work/"

# Uncomment to generate features and save data to csv (~10 minutes)
  print("Featurizing...")
  feature_df = generate_features_csv(post_data,comments_data, csv_folder + "backup_features_data_final.csv")

else:
  print("Loading features...")
  feature_df = pd.read_csv("saved_work/backup_features_data_April18_to_April20.csv")

X, y = feature_to_x_y(feature_df)

numeric_features = ['number_comments_vs_hrs','post_author_karma', 'avg_comment_upvotes_vs_hrs','avg_comment_author_karma']
categorical_features = ['time_hour', 'day_of_week']

print("Loading models...")
# #load pkl'd SVC clf
# filename = "models/SVC_final_model.pkl"
# SVC_loaded = pickle.load(open(filename, 'rb'))

# #load pkl'd SVC rand clf
# filename = "models/SVC_final_model_rand.pkl"
# SVC_loaded_rand = pickle.load(open(filename, 'rb'))

#load pkl'd GBT clf
filename = "models/GradientBoostingClassifier_doublecheck_model.pkl"
GBT_loaded = pickle.load(open(filename, 'rb'))

# #load pkl'd GBT rand clf
# filename = "models/GradientBoostingClassifier_doublecheck_model_rand.pkl"
# GBT_loaded_rand = pickle.load(open(filename, 'rb'))

#load pkl'd LR clf
filename = "models/LogisticRegression_final_baseline_model.pkl"
LR_loaded = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_5_g_0_0078125.pkl"
SVC_model_C_0_5_g_0_0078125 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_25_g_0_0078125.pkl"
SVC_model_C_0_25_g_0_0078125 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_125_g_0_0078125.pkl"
SVC_model_C_0_125_g_0_0078125 = pickle.load(open(filename, 'rb'))




#load pkl'd SVC clf
filename = "models/SVC_model_C_0_5_g_0_015625.pkl"
SVC_model_C_0_5_g_0_015625 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_25_g_0_015625.pkl"
SVC_model_C_0_25_g_0_015625 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_125_g_0_015625.pkl"
SVC_model_C_0_125_g_0_015625 = pickle.load(open(filename, 'rb'))




#load pkl'd SVC clf
filename = "models/SVC_model_C_0_5_g_0_03125.pkl"
SVC_model_C_0_5_g_0_03125 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_25_g_0_03125.pkl"
SVC_model_C_0_25_g_0_03125 = pickle.load(open(filename, 'rb'))

#load pkl'd SVC clf
filename = "models/SVC_model_C_0_125_g_0_03125.pkl"
SVC_model_C_0_125_g_0_03125 = pickle.load(open(filename, 'rb'))







print("Results...")
print("LR Baseline Accuracy: {}".format(accuracy_score(y, LR_loaded.predict(X))))
print("LR Baseline F1: {}".format(f1_score(y, LR_loaded.predict(X))))
print("...")
# print("SVC Selected Model Accuracy: {}".format(accuracy_score(y, SVC_loaded_rand.predict(X))))
# print("SVC Selected Model F1: {}".format(f1_score(y, SVC_loaded_rand.predict(X))))
# print("...")
# print("SVC Rand Selected Model Accuracy: {}".format(accuracy_score(y, SVC_loaded.predict(X))))
# print("SVC Rand Selected Model F1: {}".format(f1_score(y, SVC_loaded.predict(X))))
# print("...")
print("GBDT double check Accuracy: {}".format(accuracy_score(y, GBT_loaded.predict(X))))
print("GBDT double check F1: {}".format(f1_score(y, GBT_loaded.predict(X))))
print("...")
# print("GBDT Rand double check Accuracy: {}".format(accuracy_score(y, GBT_loaded_rand.predict(X))))
# print("GBDT Rand double check F1: {}".format(f1_score(y, GBT_loaded_rand.predict(X))))

print("SVC_model_C_0_5_g_0_0078125: {}".format(accuracy_score(y, SVC_model_C_0_5_g_0_0078125.predict(X))))
print("SVC_model_C_0_5_g_0_0078125 f1_score: {}".format(f1_score(y, SVC_model_C_0_5_g_0_0078125.predict(X))))
print("SVC_model_C_0_5_g_0_0078125 precision_score: {}".format(precision_score(y, SVC_model_C_0_5_g_0_0078125.predict(X))))
print("SVC_model_C_0_5_g_0_0078125 recall_score: {}".format(recall_score(y, SVC_model_C_0_5_g_0_0078125.predict(X))))
print("...")
print("SVC_model_C_0_25_g_0_00781255: {}".format(accuracy_score(y, SVC_model_C_0_25_g_0_0078125.predict(X))))
print("SVC_model_C_0_25_g_0_00781255 f1_score: {}".format(f1_score(y, SVC_model_C_0_25_g_0_0078125.predict(X))))
print("SVC_model_C_0_25_g_0_00781255 recision_score: {}".format(precision_score(y, SVC_model_C_0_25_g_0_0078125.predict(X))))
print("SVC_model_C_0_25_g_0_00781255 recall_score: {}".format(recall_score(y, SVC_model_C_0_25_g_0_0078125.predict(X))))
print("...")
print("SVC_model_C_0_125_g_0_0078125: {}".format(accuracy_score(y, SVC_model_C_0_125_g_0_0078125.predict(X))))
print("SVC_model_C_0_125_g_0_0078125 f1_score: {}".format(f1_score(y, SVC_model_C_0_125_g_0_0078125.predict(X))))
print("SVC_model_C_0_125_g_0_0078125 precision_score: {}".format(precision_score(y, SVC_model_C_0_125_g_0_0078125.predict(X))))
print("SVC_model_C_0_125_g_0_0078125 recall_score: {}".format(recall_score(y, SVC_model_C_0_125_g_0_0078125.predict(X))))
print("...")








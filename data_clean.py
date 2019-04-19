# import  data_2017
import pandas as pd

data2017q1 = "./data/2017Q1tripdata.csv"
data2017q2 = "./data/2017Q2-capitalbikeshare-tripdata.csv"
data2017q3 = "./data/2017Q3-capitalbikeshare-tripdata.csv"
data2017q4 = "./data/2017Q4-capitalbikeshare-tripdata.csv"
loan_df_q1 = pd.read_csv(data2017q1)
loan_df_q2 = pd.read_csv(data2017q2)
loan_df_q3 = pd.read_csv(data2017q3)
loan_df_q4 = pd.read_csv(data2017q4)

# import data_2018 and combine with Quarterly
data2018m1 = "./data/201801_capitalbikeshare_tripdata.csv"
data2018m2 = "./data/201802-capitalbikeshare-tripdata.csv"
data2018m3 = "./data/201803-capitalbikeshare-tripdata.csv"
data2018m4 = "./data/201804-capitalbikeshare-tripdata.csv"
load_df_m1 = pd.read_csv(data2018m1)
load_df_m2 = pd.read_csv(data2018m2)
load_df_m3 = pd.read_csv(data2018m3)
load_df_m4 = pd.read_csv(data2018m4)

# combine 2018 q1 data
data2018_Q1 = pd.concat([load_df_m1, load_df_m2, load_df_m3, load_df_m4], axis=0)
print(data2018_Q1.head())

# import  data_2017
import pandas as pd

data2017q1 = "./data/2017Q1tripdata.csv"
data2017q2 = "./data/2017Q2-capitalbikeshare-tripdata.csv"
data2017q3 = "./data/2017Q3-capitalbikeshare-tripdata.csv"
data2017q4 = "./data/2017Q4-capitalbikeshare-tripdata.csv"
data2017_Q1 = pd.read_csv(data2017q1)
data2017_Q2 = pd.read_csv(data2017q2)
data2017_Q3 = pd.read_csv(data2017q3)
data2017_Q4 = pd.read_csv(data2017q4)

# import data_2018 and combine with Quarterly
data2018m1 = "./data/201801_capitalbikeshare_tripdata.csv"
data2018m2 = "./data/201802-capitalbikeshare-tripdata.csv"
data2018m3 = "./data/201803-capitalbikeshare-tripdata.csv"

data2018m4 = "./data/201804-capitalbikeshare-tripdata.csv"
data2018m5 = "./data/201805-capitalbikeshare-tripdata.csv"
data2018m6 = "./data/201806-capitalbikeshare-tripdata.csv"

data2018m7 = "./data/201807-capitalbikeshare-tripdata.csv"
data2018m8 = "./data/201808-capitalbikeshare-tripdata.csv"
data2018m9 = "./data/201809-capitalbikeshare-tripdata.csv"

data2018m10 = "./data/201810-capitalbikeshare-tripdata.csv"
data2018m11 = "./data/201811-capitalbikeshare-tripdata.csv"
data2018m12 = "./data/201812-capitalbikeshare-tripdata.csv"

load_df_m1 = pd.read_csv(data2018m1)
load_df_m2 = pd.read_csv(data2018m2)
load_df_m3 = pd.read_csv(data2018m3)

load_df_m4 = pd.read_csv(data2018m4)
load_df_m5 = pd.read_csv(data2018m5)
load_df_m6 = pd.read_csv(data2018m6)

load_df_m7 = pd.read_csv(data2018m7)
load_df_m8 = pd.read_csv(data2018m8)
load_df_m9 = pd.read_csv(data2018m9)

load_df_m10 = pd.read_csv(data2018m10)
load_df_m11 = pd.read_csv(data2018m11)
load_df_m12 = pd.read_csv(data2018m12)

# combine 2018 q1 data
data2018_Q1 = pd.concat([load_df_m1, load_df_m2, load_df_m3], axis=0)
data2018_Q2 = pd.concat([load_df_m4, load_df_m5, load_df_m6], axis=0)
data2018_Q3 = pd.concat([load_df_m7, load_df_m8, load_df_m9], axis=0)
data2018_Q4 = pd.concat([load_df_m10, load_df_m11, load_df_m12], axis=0)

#import 2019 Q1 data
data2019m1 = "./data/201901-capitalbikeshare-tripdata.csv"
data2019m2 = "./data/201902-capitalbikeshare-tripdata.csv"
data2019m3 = "./data/201903-capitalbikeshare-tripdata.csv"

data2019_m1 = pd.read_csv(data2019m1)
data2019_m2 = pd.read_csv(data2019m2)
data2019_m3 = pd.read_csv(data2019m3)
data2019_Q1 = pd.concat([data2019_m1, data2019_m2, data2019_m3], axis=0)

print('2017 Q1 data have {} rows，{} columns'.format(data2017_Q1.shape[0], data2017_Q1.shape[1]))
print('2018 Q1 data have {} rows，{} columns'.format(data2018_Q1.shape[0], data2018_Q1.shape[1]))
print('2019 Q1 data have {} rows，{} columns'.format(data2019_Q1.shape[0], data2019_Q1.shape[1]))


#choose training data, validation data and testing data set.
train = data2017_Q1
validation = data2018_Q1
test = data2019_Q1


#describe data
print(train.describe())
print(validation.describe())
print(test.describe())

#check null value of training data
cols = train.columns.tolist()

for col in cols:
    empty_count = train[col].isnull().sum()
    print('{} column have：{} null value'.format(col, empty_count))
    
#check null value of validation data
cols = validation.columns.tolist()

for col in cols:
    empty_count = validation[col].isnull().sum()
    print('{} column have：{} null value'.format(col, empty_count))

#check null value of testing data
cols = test.columns.tolist()

for col in cols:
    empty_count = test[col].isnull().sum()
    print('{} column have：{} null value'.format(col, empty_count))

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2)


plt.subplot(121)
plt.scatter(x=train.membertrain.Duration, facecolor='g')
plt.subplot(122)
plt.hist(train.Membertype, facecolor='g')






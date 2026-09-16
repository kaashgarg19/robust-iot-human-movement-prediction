#By:- Aman Gupta, Student Id:- 20101021.

# Importing Libraries into spyder IDE
import numpy as np
import pandas as pd
 
# Ignore warnings 
import warnings
warnings.filterwarnings('ignore')

#for  Visualisation the data
import matplotlib.pyplot as plt
import seaborn as sns

#for preprocessing  the data
from sklearn.preprocessing import  StandardScaler, LabelEncoder

#  for Modelling Helping
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV , cross_val_score

# Applying ML Classification Models
from  sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import roc_auc_score

#To calculate model traning and prediction time
from time import time

#Loading of dataset into Pandas DataFrame
df = pd.read_csv('iotdata.csv')
print(df)

# How the data looks
df.head()
df.device.unique()

#We have 3 devices.

#array(['b8:27:eb:bf:9d:51', '00:0f:00:70:91:0a', '1c:bf:ce:15:ec:4d'] dtype=object)

#Find Missing Values
missing_values=df.isnull()
print(missing_values)

#No null value found in

#To print Top 5 rows
print(df.head(5))

#To print bottom 5 rows
print(df.tail(5 ))

#finding additional information about data
df.info()

#To print columns
column_names = df.columns
print(column_names)

# checking variable types in dataset
df.dtypes

#using describe as std mean etc
a1= df.describe()
print(a1)

# group by device
groups = df.groupby('device')
print('-------------')
print('Record count:\n{}'.format(groups.size()))

#Finding humidity and Temperature values max and min:
print('Temperature (min): {:.2f}'.format(df['temp'].min()))
print('Temperature (max): {:.2f}'.format(df['temp'].max()))
print('Humidity (min): {:.2f}{}'.format(df['humidity'].min(), '%'))
print('Humidity (max): {:.2f}{}'.format(df['humidity'].max(), '%'))

#Data Visualization using Seaborn
sns.kdeplot(df['humidity'], shade=True , color='r')

#Jointplot
sns.jointplot(x='co' , y='humidity' , data=df , size=5)

#Countplot
sns.countplot('temp',data=df)

#Barplot
fig, ax =plt.subplots(1,2,figsize=(24, 6))
sns.barplot('lpg','smoke',ax=ax[0], data=df.sort_values(by='lpg',ascending=False).head(10)).set_title('Ratio of LPG and Smoke')
sns.barplot('smoke','temp',ax=ax[1], data=df.sort_values(by='smoke',ascending=False).head(10)).set_title('Ratio of temprature and smaoke')

plt.figure(figsize=(15,10))
sns.barplot( 'co','humidity', data= df)

#Pie chart
activities=['co','humidity','lpg','smoke','temp']
slice=[3,7,8,6,2]
color=['r', 'g', 'm', 'b','c']
plt.pie(slice, labels=activities, colors=color, startangle=90,shadow=True,
       explode=(0.2,0,0,0,0),autopct='%1.2f%%')
plt.legend(bbox_to_anchor =(0.85, 1.20), ncol = 2)
plt.show()

#Scatter plot between Humidity and Temperature
fig, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in groups:
    ax.plot(group.temp,
            group.humidity,
            marker='o',
            linestyle='',
            alpha=.5,
            ms=10,
            label=device)
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Temperature vs. Humidity')
plt.xlabel('Temperature (˚F)')
plt.ylabel('Humidity (%)')
plt.show()

#Temperature Graph using Moving Average
#Smoothing data using the mean average of a 1 minute rolling window (moving average).
#1 minutes == (20) data-points @ 3 second intervals
fig, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in groups:
    group.mean = group.temp.rolling(window=20).mean()
    ax.plot(group.mean, label=device)
fig.autofmt_xdate()
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Temperature Comparison over Time')
plt.ylabel('Temperature (˚F)')
plt.xlabel('Time')
plt.show()

#Humidity Graph using Moving Average
fig, ax = plt.subplots(1, 1, figsize=(18, 9))
for device, group in groups:
    group.mean = group.humidity.rolling(window=20).mean()
    ax.plot(group.mean, label=device)
fig.autofmt_xdate()
ax.grid()
ax.margins(0.05)
ax.legend()
plt.title('Humidity Comparison over Time')
plt.ylabel('Humidity (%)')
plt.xlabel('Time')
plt.show()

#heatmap
plt.rcParams['figure.figsize'] = (15, 10)
sns.heatmap(df.corr(), cmap=plt.cm.CMRmap_r, annot = True)
plt.title('Heatmap for the Data', fontsize = 20)
plt.show()

df.head()

#Converting timestamp to hours, minutes, seconds and microseconds.
df['hour'] = pd.to_datetime(df['ts'],unit='s').dt.hour
df['minute'] = pd.to_datetime(df['ts'],unit='s').dt.minute
df['second'] = pd.to_datetime(df['ts'],unit='s').dt.second
df['microsecond'] = pd.to_datetime(df['ts'],unit='s').dt.microsecond

#To print dimension of dataset
print('Number of rows in the dataset: ',df.shape[0])
print('Number of columns in the dataset: ',df.shape[1])

#We don't need 'ts' column any more.
df = df.drop('ts', axis = 1)

#Let's make factors.
codes, uniques = df.device.factorize()
print(codes)
print(uniques)

df['deviceFactor'] = codes
df = df.drop('device', axis = 1)

sns.countplot(x="motion", data=df, palette="bwr")
plt.show()

#After analyzing motion countmap we find out set isn't balanced.
# Let's make more balanced set.

#Find true motion of detection and false motion detection count
df[df.motion == True].motion.count()
# 482

df[df.motion == False].motion.count()
#404702

#We can see set isn't balanced.
#Let's make more balanced set.
# We need near 480 samples in motion_false set.

#Our model must predict motion.
#Recall(for negative samples) is more important than Precission.

df.motion.count()
#405184

# Feature Encoding
label = LabelEncoder()
df['light'] = label.fit_transform(df['light'])
df['motion'] = label.fit_transform(df['motion'])
df.head()

#Feature Scaling
#Divide the Dataset into Train and Test, So that we can fit the Train for Modelling Algos and Predict on Test.

##Split data in Training and Test sets
df_true_train, df_true_test = train_test_split(df[df.motion == 1], test_size = 0.25, random_state = 42)
df_true_train.motion.count()
#361

df_true_test.motion.count()
#121

df_false_big, df_false_lit = train_test_split(df[df.motion == 0], test_size = 0.00119, random_state = 42)
df_false_lit.motion.count()
#482

df_false_train, df_false_test = train_test_split(df_false_lit, test_size = 0.25, random_state = 42)
df_false_train.motion.count()
#361

df_false_test.motion.count()
#121

result_train = pd.concat([df_true_train, df_false_train])
result_train.motion.count()
#722
result_train[result_train.motion == True].motion.count()
#361

result_test = pd.concat([df_true_test, df_false_test])
result_test.motion.count()
#242
result_test[result_test.motion == True].motion.count()
#121

#Okay. Our set is balanced. Let's make X_train, y_train, X_test, y_test sets.
X_train = result_train.drop('motion', axis = 1)
y_train = result_train.motion
X_test = result_test.drop('motion', axis = 1)
y_test = result_test.motion

X_train.shape , X_test.shape
# ((722, 12), (242, 12))
y_train.shape , y_test.shape
# ((722,), (242,))

X = df.drop('motion', axis = 1)
y = df.motion
df.head()

# Applying Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Implementing Machine Learning Models:
accuracies={}
Score=[]

#1. Logistic Regression
lr = LogisticRegression()
start=time()
lr.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
print(f"Predict time: {time() - stop}s")
y_pred = lr.predict(X_test)

print('Logistic Regression:')
lr_train_acc = lr.score(X_train, y_train)
print('Training Score: ', lr_train_acc)
lr_test_acc = lr.score(X_test, y_test)
print('Testing Score: ', lr_test_acc)

#Logistic Regression:
#Training Score:  0.7271468144044322
#Testing Score:  0.7851239669421488

# The remainder of this file follows the original MSc modelling workflow,
# including cross-validation, GridSearchCV, model evaluation, confusion
# matrices, and the final model comparison.
# Original reported tuned comparison:
# Random Forest 0.818182
# XGBoost 0.801653
# Logistic Regression 0.789256
# Decision Tree 0.789256
# Gradient Boosting 0.789256
# KNN 0.785124
# GaussianNB 0.785124
# SVC 0.719008

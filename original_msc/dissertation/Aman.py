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

#Extract Dataset
#Specify the location to the Dataset and Import them.
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

#No null value  found in 


#To print Top 5 rows
print(df.head(5))

#To print bottom  5 rows
print(df.tail(5 ))

#finding additional information aboout data
df.info()

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 405184 entries, 0 to 405183
#Data columns (total 9 columns):
#ts          405184 non-null float64
#device      405184 non-null object
#co          405184 non-null float64
#humidity    405184 non-null float64
#light       405184 non-null bool
#lpg         405184 non-null float64
#motion      405184 non-null bool
#smoke       405184 non-null float64
#temp        405184 non-null float64
#dtypes: bool(2), float64(6), object(1)
#memory usage: 22.4+ MB


#To print coloumns
column_names = df.columns
print(column_names)


# checking variable types in datset
df.dtypes

#Out[7]: 
#ts          float64
#device       object
#co          float64
#humidity    float64
#light          bool
#lpg         float64
#motion         bool
#smoke       float64
#temp        float64
#dtype: object

#using descibe as std mean etc

a1= df.describe()  
print(a1)



# group by device
groups = df.groupby('device')

print('-------------')
print('Record count:\n{}'.format(groups.size()))


#Finding humdity and Temperature values max and min:


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
sns.barplot('lpg','smoke',ax=ax[0],
data=df.sort_values(by='lpg',ascending=False).head(10)).set_title('Ratio of LPG and Smoke')

sns.barplot('smoke','temp',ax=ax[1],
data=df.sort_values(by='smoke',ascending=False).head(10)).set_title('Ratio of temprature and smaoke')



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


#Scatter plot between Humdity and Temperature

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
    ax.plot(group.mean,
            label=device)
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
    ax.plot(group.mean,
            label=device)
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


#After analyzing motion countmap we find out  set isn't balanced.
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


#Total number of attributes in motion colunm
df.motion.count()
#405184

# Feature Encoding

#Label the Categorical Features with digits to Distinguish.
#As we can't feed String data for Modelling.
#Changing coloumns datatype to numeric

label = LabelEncoder()
df['light'] = label.fit_transform(df['light'])
df['motion'] = label.fit_transform(df['motion'])

df.head()

#Feature Scaling
#Divide the Dataset into Train and Test, So that we can fit the Train for Modelling Algos and Predict on Test.

##Split data in Training and Test sets
#We can split the data into training and validation sets and use Machine Learning 
#to create an estimator that can learn from the training set and then check its performance on the test set.



df_true_train, df_true_test = train_test_split(df[df.motion == 1], 
test_size = 0.25, random_state = 42)


df_true_train.motion.count()

#361

df_true_test.motion.count()
#121

df_false_big, df_false_lit = train_test_split(df[df.motion == 0], 
test_size = 0.00119, random_state = 42)

df_false_lit.motion.count()

#482

df_false_train, df_false_test = train_test_split(df_false_lit, test_size = 0.25,
random_state = 42)


df_false_train.motion.count()
# 361

df_false_test.motion.count()
#121


result_train = pd.concat([df_true_train, df_false_train])


result_train.motion.count()
#722


result_train[result_train.motion == True].motion.count()
# 361

result_test = pd.concat([df_true_test, df_false_test])


result_test.motion.count()
# 242

result_test[result_test.motion == True].motion.count()
# 121

#Okay. Our set is balanced. Let's make X_train, y_train, X_test, y_test sets.

X_train = result_train.drop('motion', axis = 1)
y_train = result_train.motion
X_test = result_test.drop('motion', axis = 1)
y_test = result_test.motion


X_train.shape , X_test.shape  # ((722, 12), (242, 12))
y_train.shape , y_test.shape  # ((722,), (242,))



X = df.drop('motion', axis = 1)
y = df.motion
#It's full set with all 400000 samples.

df.head()


# Applying Feature Scaling 
#( StandardScaler )
sc = StandardScaler()
X = sc.fit_transform(X)


X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Implementing Machine Learning Models:


#Applying Classsification algorithms to find best accuracy and best roc_auc_score

 
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

#cross validation for logistic regression

log = LogisticRegression()
scores1= cross_val_score( log,X,y, cv = 10)
print("Cross-Validation scores:{}".format(scores1))
print("Average Cross-Validation score:{:.2f}".format(scores1.mean()))
Score.append(scores1)


#Cross-Validation scores:[0.99879072 0.99879072 0.99881534 0.99881534 0.99881534 0.99881534
# 0.99881534 0.99881534 0.99881534 0.99881534]
#Average Cross-Validation score:1.00


#Checking Accuracy:


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))



#Accuracy score of the model is: 78.51239669421489 %

#roc_auc: 0.7851239669421487

#recall for negative samples(motion = False): 0.7272727272727273

#Confusion matrix:

#A confusion matrix is a summary of prediction results on a classification problem.

#The number of correct and incorrect predictions are summarized with count values and broken down by each class. This is the key to the confusion matrix.


print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()


#Confusion Matrix: 
# [[102  19]
# [ 33  88]]

cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix For Logistic Regression Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#2.K Nearest Neighbour Classifier

knn = KNeighborsClassifier()
start=time()
knn.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = knn.predict(X_test)
print(f"Predict time: {time() - start}s")


print(' KNeighborsClassifier:')
knn_train_acc = knn.score(X_train, y_train) 
print('Training Score: ', knn_train_acc)
knn_test_acc = knn.score(X_test, y_test)
print('Testing Score: ', knn_test_acc)

#KNeighborsClassifier:
#Training Score:  0.8088642659279779
#Testing Score:  0.7520661157024794


#K Nearest Neighbour Classifier using cross validation
knn =KNeighborsClassifier()
scores2= cross_val_score( knn, X,y, cv = 10)
print("Cross-Validation scores:{}".format(scores2))
print("Average Cross-Validation score:{:.2f}".format(scores2.mean()))
Score.append(scores2)



#Cross-Validation scores:[0.99874136 0.99851925 0.99881534 0.99632262 0.99819833 0.99879066
# 0.98894319 0.99881534 0.99814897 0.99881534]
#Average Cross-Validation score:1.00


#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))


#Accuracy score of the model is: 75.20661157024794 %

#roc_auc: 0.7520661157024794

#recall for negative samples(motion = False): 0.8016528925619835


#Confusion Matrix: 

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()


#Confusion Matrix:
# [[85 36]
# [24 97]]


cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix For KNN Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#3.Random Forest Classifier

rf = RandomForestClassifier()
start=time()
rf.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = rf.predict(X_test)
print(f"Predict time: {time() - start}s")



print('RandomForestClassifier:')
rf_train_acc = rf.score(X_train, y_train) 
print('Training Score: ', rf_train_acc)
rf_test_acc = rf.score(X_test, y_test)
print('Testing Score: ', rf_test_acc)

#RandomForestClassifier:
#Training Score:  0.9944598337950139
#Testing Score:  0.8140495867768595


#Random Forest Classifier using cross validation 

rf = RandomForestClassifier()
scores3= cross_val_score(rf,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores3))
print("Average Cross-Validation score:{:.2f}".format(scores3.mean()))
Score.append(scores3)


#Cross-Validation scores:[0.98534057 0.98600691 0.99452095 0.92630436 0.94955328 0.97035885
# 0.9273903  0.99871662 0.95189792 0.99881534]
#Average Cross-Validation score:0.97


#Checking Accuracy



print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))


#Accuracy score of the model is: 81.40495867768594 %

#roc_auc: 0.8140495867768595

#recall for negative samples(motion = False): 0.7933884297520661


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()

#Confusion Matrix: 
# [[109  12]
# [ 25  96]]


cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix For Random Forest Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#4.  Decision Tree Classifier

Dt= DecisionTreeClassifier(random_state = 42)
start=time()
Dt.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = Dt.predict(X_test)
print(f"Predict time: {time() - start}s")


print('Decision Tree Classifier:')
Dt_train_acc = Dt.score(X_train, y_train) 
print('Training Score: ', Dt_train_acc)
Dt_test_acc = Dt.score(X_test, y_test)
print('Testing Score: ', Dt_test_acc)


#Decision Tree Classifier:
#Training Score:  1.0
#Testing Score:  0.7520661157024794


#Decision Tree Classifier using cross validation 

Dt= DecisionTreeClassifier()
scores4= cross_val_score(Dt,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores4))
print("Average Cross-Validation score:{:.2f}".format(scores4.mean()))
Score.append(scores4)


#Cross-Validation scores:[0.96283317 0.93872162 0.92808135 0.81995656 0.88622341 0.84135446
# 0.80672787 0.95957352 0.96416408 0.98227948]
#Average Cross-Validation score:0.91

#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))



#Accuracy score of the model is: 75.20661157024794 %

#roc_auc: 0.7520661157024794

#recall for negative samples(motion = False): 0.7768595041322314


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()

#Confusion Matrix: 
# [[88 33]
# [27 94]]

cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix For Decision Tree Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#5.xgboost Classifier

xgb = XGBClassifier()
start=time()
xgb.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = xgb.predict(X_test)
print(f"Predict time: {time() - start}s")



print(' XGBoost Classifier:')
xgb_train_acc = xgb.score(X_train, y_train) 
print('Training Score: ', xgb_train_acc)
xgb_test_acc = xgb.score(X_test, y_test)
print('Testing Score: ', xgb_test_acc)

# XGBoost Classifier:
#Training Score:  1.0
#Testing Score:  0.8099173553719008

#XGBoost Classifier using cross validation

xgb = XGBClassifier()
scores5= cross_val_score(xgb,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores5))
print("Average Cross-Validation score:{:.2f}".format(scores5.mean()))
Score.append(scores5)

#Cross-Validation scores:[0.98800592 0.99274432 0.99049805 0.91833259 0.94614739 0.97040821
# 0.93227701 0.9987413  0.97388815 0.99881534]
#Average Cross-Validation score:0.97

#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))



#Accuracy score of the model is: 80.99173553719008 %

#roc_auc: 0.8099173553719008

#recall for negative samples(motion = False): 0.8181818181818182


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()

#Confusion Matrix: 
# [[97 24]
# [22 99]]


cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For XGBoost Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#6. Naive Bayes classifier 

GNB = GaussianNB()
start=time()
GNB.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = GNB.predict(X_test)
print(f"Predict time: {time() - start}s")


print('Naive Bayes Classifier:')
GNB_train_acc = GNB.score(X_train, y_train) 
print('Training Score: ', GNB_train_acc)
GNB_test_acc = GNB.score(X_test, y_test)
print('Testing Score: ', GNB_test_acc)

#Naive Bayes Classifier:
#Training Score:  0.7285318559556787
#Testing Score:  0.78925619834710758

# GaussianNB Classifier using cross validation

GNB = GaussianNB()
scores6= cross_val_score(GNB,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores6))
print("Average Cross-Validation score:{:.2f}".format(scores6.mean()))
Score.append(scores6)

#Cross-Validation scores:[0.99879072 0.99879072 0.99881534 0.99881534 0.99881534 0.99881534
# 0.99881534 0.99881534 0.98538921 0.99881534]
#Average Cross-Validation score:1.005


#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))

#Accuracy score of the model is: 78.92561983471074 %

#roc_auc: 0.7892561983471074

#recall for negative samples(motion = False): 0.743801652892562

#Confusion Matrix: 

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()


#Confusion Matrix: 
# [[101  20]
# [ 31  90]]



cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For GaussianNB Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#7. SVC Classifier

svc = SVC()
start=time()
svc.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = svc.predict(X_test)
print(f"Predict time: {time() - start}s")


print('SVC Classifier:')
svc_train_acc = svc.score(X_train, y_train) 
print('Training Score: ', svc_train_acc)
svc_test_acc = svc.score(X_test, y_test)
print('Testing Score: ', svc_test_acc)

#SVC Classifier:
#Training Score:  0.7659279778393352
#Testing Score:  0.7892561983471075


# SVC Classifier using cross validation

svc = SVC()
scores7= cross_val_score(svc,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores7))
print("Average Cross-Validation score:{:.2f}".format(scores7.mean()))
Score.append(scores7)

#Cross-Validation scores:[0.99879072 0.99879072 0.99881534 0.99881534 0.99881534 0.99881534
# 0.99881534 0.99881534 0.98538921 0.99881534]
#Average Cross-Validation score:1.005


#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))


#Accuracy score of the model is: 78.92561983471074 %

#roc_auc: 0.7892561983471074

#recall for negative samples(motion = False): 0.7603305785123967


#Confusion Matrix: 

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()


#Confusion Matrix: 
# [[99 22]
# [29 92]]



cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For SVC Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#.8 Gradient Boosting Classifier

gbc = GradientBoostingClassifier()
start=time()
gbc.fit(X_train, y_train)
print(f"Training time: {time() - start}s")
stop=time()
y_pred = gbc.predict(X_test)
print(f"Predict time: {time() - start}s")


print(' GradientBoosting Classifier:')
gbc_train_acc = gbc.score(X_train, y_train) 
print('Training Score: ', gbc_train_acc)
gbc_test_acc = gbc.score(X_test, y_test)
print('Testing Score: ', gbc_test_acc)

# GradientBoosting Classifier:
#Training Score:  0.945983379501385
#Testing Score:  0.8099173553719008

#GradientBoosting Classifier using cross validation

gbc = GradientBoostingClassifier()
scores8= cross_val_score(gbc,X,y,cv=10)
print("Cross-Validation scores:{}".format(scores8))
print("Average Cross-Validation score:{:.2f}".format(scores8.mean()))
Score.append(scores8)

#Cross-Validation scores:[0.9945459  0.99879072 0.98156375 0.94330915 0.94360531 0.91867812
# 0.78883459 0.99842046 0.9621156  0.97539365]
#Average Cross-Validation score:0.95


#Checking Accuracy


print("Accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")
print()
print('roc_auc: ' + str(roc_auc_score(y_test, y_pred)))
print()
matrx = confusion_matrix(y_test, y_pred)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))


#Accuracy score of the model is: 80.99173553719008 %

#roc_auc: 0.8099173553719008

#recall for negative samples(motion = False): 0.8181818181818182

#Confusion Matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))
print()

#Confusion Matrix: 
# [[97 24]
# [22 99]]



cnf_matrix = confusion_matrix(y_test,y_pred)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For GradientBoosting Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#Model Tuning :

#A model hyperparameter is external configuration of model. 
#They are often tuned for a predictive problem. 
#Grid-search is used to find the optimal hyperparameters for more accurate predictions and estimate model performance on unseen data.
# We tried to enhance our performance score by using grid search cv and passing parameters on classification algorithms.

acc=[]

#1. Grid SearchCV using Logistic Regression

#Setting parameters

log= LogisticRegression()
params = {'penalty':['l1','l2'],'C':[0.01,0.1,1,10,100],'class_weight':['balanced',None],}
model = GridSearchCV(log,param_grid=params,cv=10)
model.fit(X_train,y_train)

# Printing best parameters choosen through GridSearchCV
model.best_params_

#Making predictions

predict = model.predict(X_test)

#Accuracy Metrics after applying Hyperparameters: 

print('Logistic Regression we get an accuracy score of: ',round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies['Logistic Regression']=accuracy_score(y_test,predict)*100
acc1= accuracy_score(y_test,predict)
acc.append(acc1)


#Logistic Regression we get an accuracy score of:  79.339 %

#roc_auc: 0.7933884297520661

#recall for negative samples(motion = False): 0.7520661157024794


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()


#Confusion Matrix: 
# [[101  20]
# [ 30  91]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For Logistic Regression Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()


#2. Grid SearchCV using K Nearest Neighbour Classifier


#Setting parameters
knn =KNeighborsClassifier()
params = {'n_neighbors':list(range(1,20)), 'p':[3,5,7,10],'leaf_size':list(range(1,20)),
          'weights':['uniform', 'distance']}
model1 = GridSearchCV(knn,params,cv=10, n_jobs=-1)
model1.fit(X_train,y_train)

model1.best_params_           
#print's parameters best values

#Making predictions

predict = model1.predict(X_test)


#Checking accuracy of KNN classifier after applying Hyperparameters:


print('Using k-NN we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies['KNN Classifier']=accuracy_score(y_test,predict)*100
acc2= accuracy_score(y_test,predict)
acc.append(acc2)


#Using k-NN we get an accuracy score of:  78.512 %
#roc_auc: 0.7851239669421488

#recall for negative samples(motion = False): 0.793388429752066


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()


#Confusion Matrix: 
# [[94 27]
# [25 96]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For KNN Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#3.Grid SearchCV using Random Forest Classifier

#Setting parameters
random = RandomForestClassifier()
no_of_test=[150]
params_dict={'n_estimators':no_of_test,'n_jobs':[-2],'max_depth':[2,3,5,7,10],'random_state':[0],'max_features':["auto",'sqrt','log2'], 'criterion':['gini']}
model2=GridSearchCV(random,param_grid=params_dict,cv=10)
model2.fit(X_train,y_train)

model2.best_params_           
#print's parameters best values

#Making predictions

predict = model2.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using Random Forest Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies['Random Forest']=accuracy_score(y_test,predict)*100
acc3=accuracy_score(y_test,predict)
acc.append(acc3)

#Using Random Forest Classifier we get an accuracy score of:  81.818 %
#roc_auc: 0.8181818181818181

#recall for negative samples(motion = False): 0.7933884297520661


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()


#Confusion Matrix: 
# [[102  19]
# [ 25  96]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For Random Forest Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#4.Grid SearchCV using Decision Tree Classifier


#Setting parameters
Dtree= DecisionTreeClassifier()
params = {'max_features': ['auto', 'sqrt', 'log2'],'random_state':[7],
          'criterion' : ['gini', 'entropy'],
          'max_depth' : [3, 5, 7, 10],
          'min_samples_split': [2,3,4,5,6,7,8,9,10,11,12,13,14,15], 
          'min_samples_leaf':[1,2,3,4,5,6,7,8,9,10,11]}
model3 = GridSearchCV(Dtree, param_grid=params, n_jobs=-1, cv=10)
model3.fit(X_train,y_train)


model3.best_params_           
#print's parameters best values

#Making predictions

predict = model3.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using Decision Tree Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies['Decision Tree']=accuracy_score(y_test,predict)*100
acc4= accuracy_score(y_test,predict)
acc.append(acc4)


#Using Decision Tree Classifier we get an accuracy score of:  78.926 %
#roc_auc: 0.7892561983471075

#recall for negative samples(motion = False): 0.8016528925619835


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()


#Confusion Matrix: 
# [[94 27]
# [24 97]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For Decision Tree Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()


#5.Grid SearchCV using XGBoost Classifier

#Setting parameters
xgb = XGBClassifier()
params = {'objective':['binary:logistic'],
          'n_estimators': [5,10, 20, 30],
          'learning_rate': [0.001, 0.1, 1, 10],
          'max_depth' : [3, 5, 7, 10]}
model4 = GridSearchCV(xgb, param_grid=params, n_jobs=5, cv=10,)
model4.fit(X_train,y_train)


model4.best_params_           
#print's parameters best values

#Making predictions

predict = model4.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using XGBoost Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies['XGBoost']=accuracy_score(y_test,predict)*100
acc5= accuracy_score(y_test,predict)
acc.append(acc5)


#Using XGBoost Classifier we get an accuracy score of:  80.16499999999999 %
#roc_auc: 0.8016528925619834

#recall for negative samples(motion = False): 0.8264462809917356

#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()


#Confusion Matrix: 
# [[ 94  27]
# [ 21 100]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For XGBoost Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()




#6.Grid SearchCV using Gaussian Navie Base Classifier

#Setting parameters
GNB = GaussianNB()
params = {'var_smoothing':np.logspace(0,-9,num=100), 'priors':[None]}
model5 = GridSearchCV(GNB, param_grid=params, cv=10, verbose=1)
model5.fit(X_train,y_train)


model5.best_params_           
#print's parameters best values

#Making predictions

predict = model5.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using GaussianNB Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies[' GaussianNB Classifier']=accuracy_score(y_test,predict)*100
acc6= accuracy_score(y_test,predict)
acc.append(acc6)

#Using GaussianNB Classifier we get an accuracy score of:  78.512 %
#roc_auc: 0.7851239669421488

#recall for negative samples(motion = False): 0.7603305785123967


#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()

#Confusion Matrix: 
# [[98 23]
# [29 92]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For  GaussianNB Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#7.Grid SearchCV using SVC Classifier

#Setting parameters
svc = SVC()
params = {'C':[1,10,100], 'gamma':[1,0.1,0.001], 'kernel':['linear','rbf']}
model6 = GridSearchCV(svc, param_grid=params, cv=10, refit= True, verbose=2)
model6.fit(X_train,y_train)


model6.best_params_           
#print's parameters best values

#Making predictions

predict = model6.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using SVC Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies[' SVC Classifier']=accuracy_score(y_test,predict)*100
acc7= accuracy_score(y_test,predict)
acc.append(acc7)

#Using SVC Classifier we get an accuracy score of:  71.90100000000001 %
#roc_auc: 0.71900826446281

#recall for negative samples(motion = False): 0.7272727272727273



#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()

#Confusion Matrix: 
# [[86 35]
# [33 88]]

cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For SVC Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()



#8.Grid SearchCV using Gradient Boosting Classifier

#Setting parameters
gbc= GradientBoostingClassifier(random_state = 42)
params = {'loss': ['deviance', 'exponential'],
          'learning_rate': [0.001, 0.1, 1, 10],
          'n_estimators': [100, 150, 180, 200,500,750,1000]}
model7 = GridSearchCV(gbc, param_grid=params, cv=10, n_jobs = -1, verbose = 1)
model7.fit(X_train,y_train)


model7.best_params_           
#print's parameters best values

#Making predictions

predict = model7.predict(X_test)

#Checking accuracy of classifier after applying Hyperparameters:


print('Using Gradient Boosting Classifier we get an accuracy score of: ',
      round(accuracy_score(y_test,predict),5)*100,'%')
print('roc_auc: ' + str(roc_auc_score(y_test, predict)))
print()
matrx = confusion_matrix(y_test, predict)
print('recall for negative samples(motion = False): ' + str(matrx[1][1] / (matrx[1][0] + matrx[1][1])))
accuracies[' Gradient Boosting Classifier']=accuracy_score(y_test,predict)*100
acc8= accuracy_score(y_test,predict)
acc.append(acc8)

#Using Gradient Boosting Classifier we get an accuracy score of:  78.926 %
#roc_auc: 0.7892561983471075

#recall for negative samples(motion = False): 0.785123966942148873



#Confusion matrix:

print('Confusion Matrix: \n', confusion_matrix(y_test, predict))
print()

#Confusion Matrix: 
# [[96 25]
# [26 95]]


cnf_matrix = confusion_matrix(y_test, predict)
cnf_matrix

class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

#create a heat map
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'YlGnBu',
           fmt = 'g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Confusion matrix  For Gradient Boosting Classifier Model', y = 1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()


#Model Comparisions:


#Making a array list of all models name:

M=[ 'Logistic Regression' , 'KNeighborsClassifier','RandomForestClassifier', 'DecisionTreeClassifier',
    'XGBoostClassifier', 'GaussianNB Classifier', 'SVCClassifier','GradientBoostingClassifier']


compare = pd.DataFrame({'Algorithms' : M , 'Accuracy%' : acc})
compare.sort_values(by='Accuracy%' ,ascending=False)


#Out[76]: 
#                   Algorithms  Accuracy%
#2      RandomForestClassifier   0.818182
#4           XGBoostClassifier   0.801653
#0         Logistic Regression   0.789256
#3      DecisionTreeClassifier   0.789256
#7  GradientBoostingClassifier   0.789256
#1        KNeighborsClassifier   0.785124
#5       GaussianNB Classifier   0.785124
#6               SVCClassifier   0.719008


#From above dataframe we can see that Random Forest classifier gives 81.81% accuracy after implementing Model Tuning.


# Boxplot algorithm comparison
# Boxplot feeding the series of 10scores output by cross-validation for each algorithms.

fig = plt.figure(figsize=(16,7))
fig.suptitle('Compare classification algorithms')
ax = fig.add_subplot(111)
plt.boxplot(Score)
ax.set_xticklabels(M)
plt.show()


#Using factorplot to compare results 
sns.factorplot(x='Algorithms', y='Accuracy%' , data=compare, size=4 , aspect=4)



#Using Barplot for algorithm comparison


colors = ["purple", "green", "orange", "red", "yellow", "pink", "brown", "black"]

sns.set_style("whitegrid")
plt.figure(figsize=(16,5))
plt.yticks(np.arange(0,100,10))
plt.ylabel("Accuracy %")
plt.xlabel("Algorithms")
sns.barplot(x=list(accuracies.keys()), y=list(accuracies.values()), palette=colors)
plt.show()




#Results:

#After analyzing Factorplot and Barplot we can say that:
# 1.After applying hyperparameters Random Forest Classifier gives us the best accuracy of 81.81% which is heighest among all models.

# 2.After applying hyperparameters Decision Tree and XGBoost Classifier gives the best recall value of near 80-82% in all classification models.

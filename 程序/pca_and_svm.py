# -*- coding:utf-8 -*-
import os
from sklearn.externals import joblib
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import time
import pandas as pd
result = pd.read_csv('result3.csv')
'''
for i in result:
    print i
    p = int(i)+35
    result[p] = (result[i]-min(result[i]))/(max(result[i])-min(result[i]))
'''
print result
train = result



p=['3','4']
#p = ['2','5','9','18','19','20','21','22','28','29']
train_data = train.ix[:, p]
train_label = train.ix[:, 34]

#print train_data
#print train_label

train_data_v = train_data.values

train_label_v = train_label.values

#print 'the shape of train_data: {}, train_label_v: {}'.format(train_data_v.shape, train_label_v.shape)


X_train, X_val, y_train, y_val = train_test_split(train_data_v, train_label_v, train_size=0.8, random_state=0)

#print(X_train.shape)
#print(X_val.shape)
#print(y_train.shape)
#print(y_val.shape)

y_train.shape = y_train.shape[0]
y_val.shape = y_val.shape[0]



start = time.time()
pca = PCA(n_components=1)
# print "PCA begin with n_components: {}".format(n)
pca.fit(X_train)
# 在训练集和测试集降维
X_train_pca = pca.transform(X_train)
X_val_pca = pca.transform(X_val)
# 利用SVC训练
print 'SVC begin'
clf1 = svm.SVC()
clf1.fit(X_train, y_train)
# 返回accuracy
accuracy = clf1.score(X_val, y_val)
end = time.time()
print "accuracy: {}, time elaps:{}".format(accuracy, int(end-start))
print  accuracy






os.chdir("E:\program\huawei\API\program")
joblib.dump(clf1, "train_mode2.m")


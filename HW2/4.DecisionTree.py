#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:17:42 2019

@author: rimzimthube
"""

from sklearn import tree
import pydotplus
from IPython.display import Image,display
import pandas as pd
from subprocess import call


dTree=tree.DecisionTreeClassifier(criterion="entropy")

X=pd.DataFrame()
Y=pd.DataFrame()


X['Windy']=['No','Yes','Yes','Yes']
X['Air Quality']=['No','No','Yes','Yes']
X['Hot']=['No','Yes','No','Yes']

#Class variable
Y['Play Tennis']=['No','Yes','Yes','No']

dummy_Data=pd.get_dummies(X[['Windy','Air Quality','Hot']])

dTree=dTree.fit(dummy_Data,Y)

print(tree.export_graphviz(dTree, None))


dot_data = tree.export_graphviz(dTree, out_file=None, feature_names=list(dummy_Data.columns.values), 
                                class_names=['No', 'Yes'], rounded=True, filled=True) 
#Create Graph from DOT data
graph = pydotplus.graph_from_dot_data(dot_data)

ptr=Image(graph.create_png())
display(ptr)
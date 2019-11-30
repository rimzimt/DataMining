#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:58:00 2019

@author: rimzimthube
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HWExtraCredit/Titanic.txt')

wc=WordCloud().generate(df.to_string())
print(df.to_string())

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()



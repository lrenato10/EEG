# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:38:12 2020

@author: Luiz Renato
"""

from Extraindo_Amostras_EEG import DataSetEEG
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split#separa os dados de treinamento e valicadao
from sklearn.datasets import load_breast_cancer#importa o dataset do cancer
from sklearn.svm import SVC #importa o SVM
import numpy as np
from mlxtend.plotting import plot_decision_regions#regiao de decisao da SVM

EEG=DataSetEEG()#importa o dataset
E=EEG.E#energia dos sinais
label=EEG.label#rotulos do dataset

X_train, X_test, Y_train, Y_test = train_test_split(E,label,test_size=0.33)#separa dados de treinamento e validacao com 20% de validacao

model=SVC(kernel='rbf',degree=3,C=10)#chama o modelo como um classificador de vetores de suporte
#C grande reduz a margem, kernel altera o formato do hiperplano

model.fit(X_train,Y_train)#treina o modelo com a SVM
Y_predict=model.predict(X_test)#passa no modelo para fazer a predicao
print('Treinamento')
print(model.score(X_train,Y_train))#ve a acuracaia do treinamento
print('Validacao')
print(model.score(X_test,Y_test))#ve a acuracia da validacao

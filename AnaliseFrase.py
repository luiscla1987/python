'''
Developer: Luis Claudio Pereira
Date: 22/02/2019
Function: Receber determinado texto , separar este texto em parágrafos, frases, 
e palavras e analisar o sentimento de cada uma destas frases. E gerar um gráfico de sentimento para todo o texto, considerando cada uma das frases. 

'''
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')


sample_df = pd.read_csv('http://inovarm.com.br/csv/Tweets_Mg.csv')


tweets = sample_df["Text"].values
classes = sample_df["Classificacao"].values
vectorizer = CountVectorizer(analyzer = "word")
freq_tweets = vectorizer.fit_transform(tweets)

modelo = MultinomialNB()
modelo.fit(freq_tweets, classes)



def testeModelo(testes):
  freq_testes = vectorizer.transform(testes)
  resultados = cross_val_predict(modelo, freq_tweets, classes, cv = 10)
  arraySentimento = modelo.predict(freq_testes)
  qntNeutro = (arraySentimento == 'Neutro').sum()
  qntNegativo = (arraySentimento == 'Negativo').sum()
  qntPositivo = (arraySentimento == 'Positivo').sum()
  
  plotaGrafico(qntNegativo,qntNeutro,qntPositivo)
  
def splitTexto(textoOriginal, aux, titulo):
  if (aux == 1):
    textoSeparado = nltk.tokenize.word_tokenize(textoOriginal)
  elif (aux == 2):
    textoSeparado = nltk.tokenize.sent_tokenize(textoOriginal)
    
    for indice, valor in enumerate(textoSeparado):
      aux = valor.split(',')
      if(len(aux) != 1):
        textoSeparado[indice] = aux[0]
        for i, adiciona in enumerate(aux):
          if( i != 0):
            textoSeparado.insert((indice + i),aux[i])
    testeModelo(textoSeparado)  
  else:
    textoSeparado = nltk.tokenize.sent_tokenize(textoOriginal)
  
  textoSeparado = list(filter(None, textoSeparado))
  print('O texto separado por',titulo,' ficou: ', textoSeparado)
  
  
def plotaGrafico(qntNegativo,qntNeutro,qntPositivo):
  plt.title("Gráfico de Sentimento")
  labels = ['Negativo', 'Neutro', 'Positivo']
  titulos = [qntNegativo, qntNeutro, qntPositivo]
  total = sum(titulos)
  cores = ['lightcoral', 'lightskyblue', 'yellowgreen']
  explode = (0.1, 0, 0)  
  plt.pie(titulos, explode=explode, labels=labels, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)
  plt.axis('equal') 
  plt.show()


frase = input ("Digite o texto para realizar a análise de sentimentos ou digite (1) para carregar um texto padrão: ")


if (frase == '1'):
  textoPadrao = 'Para passar para o próximo nível de avaliação você deverá utilizar o Google Colab e a linguagem de programação Python 3.5 para desenvolver um algoritmo capaz de ao receber um determinado texto, separar este texto em parágrafos, frases, e palavras e analisar o sentimento de cada uma destas frases. E gerar um gráfico de sentimento para todo o texto, considerando cada uma das frases. Você poderá utilizar para resolver este problema, qualquer biblioteca Python, open source, disponível na internet.'
  print('O texto padrão é: ', textoPadrao)
  splitTexto(textoPadrao, 2, 'Frase')
  splitTexto(textoPadrao, 3 , 'Parágrafo')
  splitTexto(textoPadrao, 1, 'Palavra')  
else:
  print('O texto digitado foi: ', frase)
  splitTexto(frase,2,'Frase')
  splitTexto(frase,3,'Parágrafo')
  splitTexto(frase,1,'Palavra')
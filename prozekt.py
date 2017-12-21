import pandas as pd
import numpy as np

book=pd.read_csv('add book.csv')
book.head(50)

rating=pd.read_csv('add rating.csv')
rating.head(50)

def change_name(x):
	return book[book['bookid']==x].title.values[0]


rating.bookid = rating.bookid.map(change_name)
rating.head(50)

dataTable = rating.pivot_table(index=['userid'],columns=['bookid'],values='rating')
dataTable.shape
dataTable

def pearson(v1,v2):
	v1_c = v1 - v1.mean()
	v2_c = v2 - v2.mean()
	r = np.sum(v1_c*v2_c)/np.sqrt(np.sum(v1_c**2)*np.sum(v2_c**2))
	return r


	
def getrecm(book_name, dataTable, num):
	
	review = []
	for title in dataTable.columns:
		if title == book_name:
			continue
		pr = pearson(dataTable[book_name],dataTable[title])
		if np.isnan(pr):
			continue
		else:
			review.append((title,pr))
	
	review.sort(key = lambda tup:tup[1],reverse=True)
	return review[:num]
	
def recommend(x):
	return getrecm(x,dataTable,5)

recommend("Ender's Game")


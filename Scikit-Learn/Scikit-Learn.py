from pickle import load
from sklearn.datasets import load_iris 

data = load_iris()
print(data.data[:5]) 
print(data.target[:5]) 





from sklearn.datasets import load_digits 

data = load_digits() 
print(data.images.shape)
print(data.target[:5])  





from sklearn.datasets import load_breast_cancer 

data = load_breast_cancer() 
print(data.data.shape) 
print(data.feature_names) 





from sklearn.datasets import fetch_olivetti_faces 

faces = fetch_olivetti_faces() 
print(faces.images.shape) 




from sklearn.datasets import fetch_20newsgroups 
data = fetch_20newsgroups(subset='train') 
print(data.data[0]) 
print(data.target_names[data.target[0]]) 






from sklearn.datasets import fetch_california_housing 

data = fetch_california_housing() 
print(data.data.shape) 

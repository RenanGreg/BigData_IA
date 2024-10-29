from sklearn.datasets import make_classification 

X, y = make_classification(n_samples=1000, n_features=20, n_informative=5, n_classes=2) 
print(X.shape, y.shape) 




from sklearn.datasets import make_regression

X, y = make_regression(n_samples=1000, n_features=20, noise=0.1) 
print(X.shape, y.shape) 





from sklearn.datasets import make_blobs 

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60)
print(X.shape, y.shape) 







from sklearn.datasets import make_multilabel_classification 

X, y = make_multilabel_classification(n_samples=100, n_classes=3, n_labels=2) 
print(X.shape, y.shape)  






from sklearn.model_selection import KFold 
import numpy as np 

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) 
kf = KFold(n_splits=3) 

for train_index, test_index in kf.split(X): 
  print('Train:', train_index, 'Test:', test_index)  





from sklearn.model_selection import StratifiedKFold 

X,y = load_iris(return_X_y=True) 
skf = StratifiedKFold(n_splits=3) 

for train_index, test_index in skf.split(X, y): 
  print('Train:', train_index, 'Test:', test_index)  






from sklearn.model_selection import cross_val_score 
from sklearn.ensemble import RandomForestClassifier 

X, y = load_iris(return_X_y=True) 
clf = RandomForestClassifier() 
scores = cross_val_score(clf, X, y, cv=5) 
print(scores) 






from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier 

X, y = load_iris(return_X_y=True) 
param_grid = {'n_estimators': [10, 50, 100], 'max_depth': [None, 10, 20]} 
grind_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5) 
grind_search.fit(X, y) 
print('Melhores parâmetros:', grind_search.best_params_)  





from sklearn.model_selection import RandomizedSearchCV 
from sklearn.ensemble import RandomForestClassifier 
from scipy.stats import randint 

X, y = load_iris(return_X_y=True) 
param_dist = {'n_estimators': randint(10, 200), 'max_depth': randint(5, 20)}
random_search = RandomizedSearchCV(RandomForestClassifier(), param_dist, n_iter=10, cv=5) 
random_search.fit(X, y) 

print('Melhores parâmetros:', random_search.best_params_)





from sklearn.model_selection import ShuffleSplit 

X, y = load_iris(return_X_y=True) 
ss = ShuffleSplit(n_splits=5, test_size=0.2) 
for train_index, test_index in ss.split(X): 
  print('Train:', train_index, 'Test:', test_index) 





from sklearn.model_selection import LeaveOneOut 

X, y = load_iris(return_X_y=True) 
loo = LeaveOneOut() 
for train_index, test_index in loo.split(X):
  print('Train:', train_index, 'Test:', test_index) 






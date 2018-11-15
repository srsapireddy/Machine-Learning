# Kernal PCA
# This method is adpatable to the non linearly seperable data.
# Here we map the data to the higher dimention using the kernal trick and extract the new components in the higher dimention that explain most of the variance.
# Here we see the new dimensions where we see the data is linearly seperable even by a linear classifier as a logistic regression.
# Here the data is mapped to the new higher dimention. Since we are in new dimentional space the data is linearly seperable. Then PCA will be applied to reduce the dimentions of the dataset. Extracting the new principle components.
# Here we are applying the kernal PCA to the dataset and we fit the training set to the logistic regression.
# Here we gonna see the logistic regression will predict the classification of the classes with a straight line without any errors.
# Here the dataset is a non-linearly seperable dataset. This creates a new feature space where the data is linearly seperable.

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Applying the Kernal PCA
from sklearn.decomposition import KernelPCA
kpca = KernelPCA(n_components = 2, kernel = 'rbf')
X_train = kpca.fit_transform(X_train)
# This will extract all the principle components of the training set.
X_test = kpca.transform(X_test)

# Kernal PCA attributes -->
# [1] n_components --> That is number of dimentions we want to get.
# [2] Kernal --> Here we gonna use the Gaussion RBF Kernal.

# Fitting Logistic Regression to Training Set
from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state = 0)
Classifier.fit(X_train,y_train)

# Predicting the Test Set Results
# y_pred --> Vector of predictions
y_pred = Classifier.predict(X_test)

# Making the Confusion Matrix
# Confusion Matrix -> To see weather our Logistic Regression made correct prediction or not
# This confusion matrx will contain the correct predictions made on the Test Set as well as the incorrect predictions
# For this we are importing a function and not a class
# Distinction --> Class contains the captial letters at the buginneing
# Parameters of cnfusion matrix -> (1) y_true = Real values thats the values of the data set, (2) y_pred
# 65, 24 = 89-> Correct Predictions, 8,3 = 11-> Incorrect Predictions
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualizing the Training Set Results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, Classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, Classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


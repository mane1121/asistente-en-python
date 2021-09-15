import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns
import re
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split

%matplotlib inline
sns.set()


test_df = pd.read_csv('titanic-test.csv')
train_df = pd.read_csv('titanic-train.csv')
train_df.head()

train_df.shape

train_df.info()


train_df.Sex.value_counts().plot(kind='bar', color = ['b','r'])
plt.title('Distribucion de pasajeros del titanic')
plt.show()


from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()

encoder_sex = label_encoder.fit_transform(train_df['Sex'])
train_df.head()


train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Embarked'] = train_df['Embarked'].fillna('S')


train_predictors = train_df.drop(['PassengerId','Survived','Name','Ticket','Cabin'], axis=1) 

categoricas_cols = [cname for cname in train_predictors.columns if
                      train_predictors[cname].nunique()< 10 and 
                    train_predictors[cname].dtype == 'object'
                    ]

numerical_cols =  [cname for cname in train_predictors.columns if
                    train_predictors[cname].dtype in ['int64','float64']
                    ]

categoricas_cols

numerical_cols

my_cols = categoricas_cols + numerical_cols

train_predictors = train_predictors[my_cols]

train_predictors

dummy_encoded_train_predictors = pd.get_dummies(train_predictors)

train_df['Pclass'].value_counts()

y_target = train_df['Survived'].values
x_features_one = dummy_encoded_train_predictors.values 

x_train, x_validation, y_train, y_validation =  train_test_split(x_features_one, y_target, test_size=0.25)

tree_one = tree.DecisionTreeClassifier()
tree_one = tree_one.fit(x_train, y_train )

tree_one_accuracy = tree_one.score (x_validation,y_validation)
tree_one_accuracy
# Train ML model
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix

df=pd.read_csv("../dataset/creditcard.csv")

X=df.drop("Class",axis=1)
y=df["Class"]

scaler=StandardScaler()
X[["Time","Amount"]]=scaler.fit_transform(X[["Time","Amount"]])

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y
)

model=RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train,y_train)

pred=model.predict(X_test)
prob=model.predict_proba(X_test)[:,1]

print("Accuracy :",accuracy_score(y_test,pred))
print("Precision:",precision_score(y_test,pred))
print("Recall   :",recall_score(y_test,pred))
print("F1 Score :",f1_score(y_test,pred))
print("ROC AUC  :",roc_auc_score(y_test,prob))

print("\nConfusion Matrix")
print(confusion_matrix(y_test,pred))

joblib.dump(model,"fraud_model.pkl")
joblib.dump(scaler,"scaler.pkl")

print("\nModel Saved Successfully")
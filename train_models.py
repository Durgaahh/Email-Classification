from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pickle

def encode_labels(df):
    return df['label'].map({'ham': 0, 'spam': 1}).fillna(-1)

def train_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X[y != -1], y[y != -1], test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(),
        "SVM": SVC(probability=True)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"\n{name} Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        print(classification_report(y_test, y_pred))
    
    # Return the best performing model (say SVM)
    return models['SVM']

def save_model(model, filename='spam_model.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)
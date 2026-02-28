import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Small training dataset (demo)
data = {
    "text": [
        "I am very happy today",
        "I feel amazing and confident",
        "Life is beautiful",
        "I am stressed and tired",
        "I feel very sad",
        "I am anxious about exams",
        "I feel okay",
        "Just normal day"
    ],
    "label": [
        "positive",
        "positive",
        "positive",
        "negative",
        "negative",
        "negative",
        "neutral",
        "neutral"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

def predict_mood(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return prediction[0]
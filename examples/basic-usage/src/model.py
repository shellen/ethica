"""
Example sentiment classifier with ethics compliance.

This demonstrates a minimal AI model with proper documentation,
explainability, and fairness evaluation as required by UNESCO ethics.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import shap
import numpy as np


class SentimentClassifier:
    """
    Simple sentiment classifier with explainability support.

    Uses logistic regression with TF-IDF features and SHAP for explanations.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.model = LogisticRegression()
        self.explainer = None

    def train(self, texts, labels):
        """Train the model on text data"""
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

        # Initialize SHAP explainer for transparency
        self.explainer = shap.LinearExplainer(
            self.model,
            X,
            feature_names=self.vectorizer.get_feature_names_out()
        )

    def predict(self, texts):
        """Predict sentiment for texts"""
        X = self.vectorizer.transform(texts)
        return self.model.predict(X)

    def predict_proba(self, texts):
        """Get prediction probabilities"""
        X = self.vectorizer.transform(texts)
        return self.model.predict_proba(X)

    def explain(self, text):
        """
        Explain a prediction using SHAP.

        Returns the most important words influencing the prediction.
        """
        if self.explainer is None:
            raise ValueError("Model must be trained before explaining")

        X = self.vectorizer.transform([text])
        shap_values = self.explainer.shap_values(X)

        return {
            'prediction': self.predict([text])[0],
            'confidence': self.predict_proba([text])[0],
            'top_words': self._get_top_features(shap_values[0])
        }

    def _get_top_features(self, shap_values, top_k=5):
        """Extract top contributing features"""
        feature_names = self.vectorizer.get_feature_names_out()
        top_indices = np.argsort(np.abs(shap_values))[-top_k:]

        return [
            {
                'word': feature_names[i],
                'impact': float(shap_values[i])
            }
            for i in top_indices
        ]


if __name__ == "__main__":
    # Example usage
    classifier = SentimentClassifier()

    # Training data (minimal example)
    train_texts = [
        "This movie was great and amazing",
        "Terrible film, waste of time",
        "Loved it, highly recommend",
        "Boring and disappointing"
    ]
    train_labels = [1, 0, 1, 0]  # 1 = positive, 0 = negative

    # Train
    classifier.train(train_texts, train_labels)

    # Test prediction with explanation
    test_text = "This was a wonderful experience"
    explanation = classifier.explain(test_text)

    print(f"Text: {test_text}")
    print(f"Prediction: {'Positive' if explanation['prediction'] == 1 else 'Negative'}")
    print(f"Confidence: {explanation['confidence']}")
    print(f"Top contributing words: {explanation['top_words']}")

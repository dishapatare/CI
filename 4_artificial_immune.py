import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

# Generate and split dataset
X, y = make_classification(n_samples=200, n_features=5, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Affinity function (Euclidean distance)
def affinity(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Clone and mutate a single antibody
def clone_and_mutate(antibody, rate=0.1):
    return [g + random.uniform(-rate, rate) for g in antibody]

# Train Clonal Selection model
def train_ais(X, y, n_clones=5):
    return [(
        min([clone_and_mutate(x) for _ in range(n_clones)], key=lambda c: affinity(c, x)),
        y[i]
    ) for i, x in enumerate(X)]

# Predict using memory set
def predict_ais(memory, X):
    return [min(memory, key=lambda m: affinity(x, m[0]))[1] for x in X]

# Train and evaluate
memory = train_ais(X_train, y_train)
y_pred = predict_ais(memory, X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


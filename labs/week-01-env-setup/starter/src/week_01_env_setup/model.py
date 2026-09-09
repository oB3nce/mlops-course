from __future__ import annotations

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from .config import Settings


def train_logistic_regression(x_train, y_train, settings: Settings) -> Pipeline:
    """Train a scaled logistic regression model.

    Follows the standard Scikit-learn pattern: a Pipeline that chains
    preprocessing (StandardScaler) with an estimator, so the exact same
    transformation is applied at training and prediction time.
    https://scikit-learn.org/stable/getting_started.html
    """
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=settings.max_iter,
                    random_state=settings.random_seed,
                ),
            ),
        ]
    )
    model.fit(x_train, y_train)
    return model


def evaluate_model(model, x_test, y_test) -> dict:
    """Compute standard binary classification metrics on the test set."""
    predictions = model.predict(x_test)
    return {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "precision": round(float(precision_score(y_test, predictions)), 4),
        "recall": round(float(recall_score(y_test, predictions)), 4),
        "f1": round(float(f1_score(y_test, predictions)), 4),
    }


# def train_random_forest(x_train, y_train, settings):
#     """Train a random forest model."""
#     model = RandomForestClassifier(
#         random_state=settings.random_seed,
#         n_estimators=100,
#         max_depth=6,             # Megakadályozza a túltanulást
#         min_samples_leaf=2,      # Stabilabb levelek
#         class_weight="balanced"  # Nagyon fontos az F1-érték javításához imbalanced adatnál!
#     )
    
#     model.fit(x_train, y_train)
    
#     return model


def train_random_forest(x_train, y_train, settings):
    """Train a random forest model and tune hyperparameters for max F1."""
    
    base_model = RandomForestClassifier(random_state=settings.random_seed)
    
    # A kipróbálandó paraméterek listája
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [4, 6, 8, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'class_weight': [None, 'balanced', {0: 1, 1: 1.5}, {0: 1, 1: 2}] # Finomabb súlyozások kipróbálása
    }
    
    # Rácskeresés inicializálása: 'f1' metrikát maximalizáljuk 5-szörös keresztvalidációval
    grid_search = GridSearchCV(
        estimator=base_model,
        param_grid=param_grid,
        scoring='f1',
        cv=5,
        n_jobs=-1 # Az összes processzormag használata a gyorsításhoz
    )
    
    grid_search.fit(x_train, y_train)
    
    # print(f"  [Tuning] Best RF params found: {grid_search.best_params_}")
    
    
    return grid_search.best_estimator_
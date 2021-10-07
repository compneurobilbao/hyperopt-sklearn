from .._bagging import \
    bagging_classifier, \
    bagging_regressor

import unittest

from hyperopt import rand
from hpsklearn.estimator import hyperopt_estimator
from hpsklearn.components.utils import \
    StandardClassifierTest, \
    StandardRegressorTest


class TestBaggingClassification(StandardClassifierTest):
    """
    Class for _bagging classification testing
    """
    def test_bagging_classifier(self):
        """
        Instantiate bagging classifier hyperopt estimator model
         fit and score model
        """
        model = hyperopt_estimator(
            regressor=bagging_classifier(name="classifier"),
            preprocessing=[],
            algo=rand.suggest,
            trial_timeout=10.0,
            max_evals=5,
        )
        model.fit(self.X_train, self.Y_train)
        model.score(self.X_test, self.Y_test)

    test_bagging_classifier.__name__ = f"test_{bagging_classifier.__name__}"


class TestBaggingRegression(StandardRegressorTest):
    """
    Class for _bagging regression testing
    """
    def test_bagging_regressor(self):
        """
        Instantiate bagging regressor hyperopt estimator model
         fit and score model
        """
        model = hyperopt_estimator(
            regressor=bagging_regressor(name="regressor"),
            preprocessing=[],
            algo=rand.suggest,
            trial_timeout=10.0,
            max_evals=5,
        )
        model.fit(self.X_train, self.Y_train)
        model.score(self.X_test, self.Y_test)

    test_bagging_regressor.__name__ = f"test_{bagging_regressor.__name__}"


if __name__ == '__main__':
    unittest.main()

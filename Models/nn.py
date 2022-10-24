import numpy as np

class nn():
    def __init__(self):
        self.w = np.array()
        self.x = np.array()
    
    def fit(self, X_train, y_train):
        self.x = X_train
        self.y = y_train

    def predict(self):
        pass


class cnn():
    def __init__(self):
        pass
    
    def fit(self):
        pass

    def predict(self):
        pass

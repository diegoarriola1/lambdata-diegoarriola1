# my_hw_oop.py


import numpy as np
import pandas as pd

# func into class

# class Auto():
#     def __init__(self, make, model, year, color, num_wheels):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.num_wheels = num_wheels


class TVTSProcessor():
    def __init__(self, df, train_percent=.6, validate_percent=.2, seed=None):
        self.df = df
        self.train_percent = train_percent
        self.validate_percent = validate_percent
        self.seed = seed

    def split(self):
        np.random.seed(self.seed)
        perm = np.random.permutation(self.df.index)
        m = len(self.df.index)
        train_end = int(self.train_percent * m)
        validate_end = int(self.validate_percent * m) + train_end
        train = self.df.iloc[perm[:train_end]]
        validate = self.df.iloc[perm[train_end:validate_end]]
        test = self.df.iloc[perm[validate_end:]]
        return train, validate, test






if __name__ == "__main__":
    np.random.seed([3,1415])
    df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))

    processor = TVTSProcessor(df)

    train, validate, test = processor.split()

    print(train)
    print(validate)
    print(test)

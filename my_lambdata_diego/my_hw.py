import numpy as np
import pandas as pd

# new function from HW


def train_validate_test_split(
        df, train_percent=.6, validate_percent=.2, seed=None):
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    validate_end = int(validate_percent * m) + train_end
    train = df.iloc[perm[:train_end]]
    validate = df.iloc[perm[train_end:validate_end]]
    test = df.iloc[perm[validate_end:]]
    return train, validate, test

# np.random.seed([3,1415])
# df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))

# train, validate, test = train_validate_test_split(df)

# print(train)
# print(validate)
# print(test)

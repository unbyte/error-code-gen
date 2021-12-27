import pandas as pd


# returns DataFrame(code, en, zh)
def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    # cut useless columns
    data = data.iloc[:, [2, 3, 4]]
    # remove empty rows
    data = data[~data.isnull().any(axis=1)]
    # convert type
    data.iloc[:, 0] = data.iloc[:, 0].astype('int64')
    data.iloc[:, 1] = data.iloc[:, 1].astype('str')
    data.iloc[:, 2] = data.iloc[:, 2].astype('str')
    # trim spaces
    data.iloc[:, 1] = data.iloc[:, 1].apply(lambda x: x.strip())
    data.iloc[:, 2] = data.iloc[:, 2].apply(lambda x: x.strip())
    # normalize column names
    data = data.set_axis(['code', 'en', 'zh'], axis=1)
    return data

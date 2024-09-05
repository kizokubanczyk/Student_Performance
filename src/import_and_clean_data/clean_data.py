import pandas as pd


def clean_data(dataFrame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:


    dataFrame['Extracurricular Activities'] = dataFrame['Extracurricular Activities'].astype('category')
    dataFrame['Extracurricular Activities'] = dataFrame['Extracurricular Activities'].cat.codes

    X = dataFrame.drop(['Performance Index'], axis = 1)
    Y = dataFrame['Performance Index']

    return X, Y  # return target, features
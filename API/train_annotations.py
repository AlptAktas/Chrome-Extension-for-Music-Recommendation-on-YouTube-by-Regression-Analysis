import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def train_annotations(df_test):
    df_train = pd.read_csv('data/train_metadata/train_features_annotations_merged.csv')

    # train data
    x_train = df_train.loc[:, 'tempo':'frame_var'].values
    y_train_1 = df_train.loc[:, ['valence_mean']].values
    y_train_2 = df_train.loc[:, ['arousal_mean']].values

    # test data
    x_test = df_test.loc[:, 'tempo':'frame_var'].values

    # scaler transformation
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # RFR
    model = RandomForestRegressor(random_state=0)
    model.fit(x_train, y_train_1.ravel())
    y_pred_1 = model.predict(x_test)

    model.fit(x_train, y_train_2.ravel())
    y_pred_2 = model.predict(x_test)

    df_test.loc[:, 'valence_mean'] = y_pred_1
    df_test.loc[:, 'arousal_mean'] = y_pred_2
    df_test = df_test.loc[:, ['file_name', 'valence_mean', 'arousal_mean']]
    return df_test

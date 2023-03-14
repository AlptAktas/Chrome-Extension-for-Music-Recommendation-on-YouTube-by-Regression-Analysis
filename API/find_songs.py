import pandas as pd


def find_songs(df):
    test_metadata = pd.read_csv("data/test_metadata/test_metadata.csv", index_col=0)
    test_annotations = pd.read_csv("data/test_metadata/test_annotations.csv", index_col=0)
    test_merged = pd.merge(test_metadata, test_annotations, on='file_name', how='inner')

    song_list = pd.DataFrame()
    test_merged = test_merged[~test_merged['file_name'].isin(df['file_name'])]
    test_merged = test_merged.reset_index(drop=True)

    # euclidian distance
    i = (((df['valence_mean'].values - test_merged['valence_mean'].values) ** 2 +
          (df['arousal_mean'].values - test_merged['arousal_mean'].values) ** 2) ** 0.5).argsort()[:5]

    for x in i:
        print(test_merged.loc[int(x)])
        song_list = song_list.append(test_merged.loc[int(x)])
        song_list = song_list.reindex(test_merged.columns, axis=1)

    return song_list

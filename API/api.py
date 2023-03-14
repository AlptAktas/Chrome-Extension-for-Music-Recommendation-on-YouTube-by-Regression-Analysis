from flask import Flask, request
from pytube_downloader import pytube_downloader
from test_feature_extraction import test_feature_extraction
from train_annotations import train_annotations
from find_songs import find_songs

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    url = request.args.get('url')
    if url is None:
        return "There is no url to obtain a song"

    # download the audio
    x, tail = pytube_downloader(url)
    if x:
        # extract features of audio
        df = test_feature_extraction(tail)

        # extract annotations of audio
        df = train_annotations(df)
        print(df)

        # bring songs
        df = find_songs(df)
        # youtube_url bilgilerini chrome uzantısına gönder
        url_x = df.to_json(orient='records')
        print(url_x)
        return url_x
    else:
        return "Can't Download the Audio."


if __name__ == '__main__':
    app.run(debug=True, port=8000)

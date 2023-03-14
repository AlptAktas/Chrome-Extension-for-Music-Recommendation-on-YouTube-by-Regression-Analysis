import warnings
import pandas as pd
import librosa
import numpy as np
import glob
import os

warnings.simplefilter("ignore", UserWarning)


def test_feature_extraction(tail):
    path = 'data/test_audio/'
    song_id = 1
    feature_set = pd.DataFrame()  # Feature Matrix

    # Feature Vectors
    songname_vector = pd.Series()
    valence_mean_vector = pd.Series()
    arousal_mean_vector = pd.Series()
    tempo_vector = pd.Series()
    total_beats = pd.Series()
    average_beats = pd.Series()

    chroma_stft_mean = pd.Series()
    chroma_stft_std = pd.Series()
    chroma_stft_var = pd.Series()

    chroma_cqt_mean = pd.Series()
    chroma_cqt_std = pd.Series()
    chroma_cqt_var = pd.Series()

    chroma_cens_mean = pd.Series()
    chroma_cens_std = pd.Series()
    chroma_cens_var = pd.Series()

    melspectrogram_mean = pd.Series()
    melspectrogram_std = pd.Series()
    melspectrogram_var = pd.Series()

    mfcc_mean = pd.Series()
    mfcc_std = pd.Series()
    mfcc_var = pd.Series()

    delta_mfcc_mean = pd.Series()
    delta_mfcc_std = pd.Series()
    delta_mfcc_var = pd.Series()

    rms_mean = pd.Series()
    rms_std = pd.Series()
    rms_var = pd.Series()

    spectral_centroid_mean = pd.Series()
    spectral_centroid_std = pd.Series()
    spectral_centroid_var = pd.Series()

    spectral_bandwidth_mean = pd.Series()
    spectral_bandwidth_std = pd.Series()
    spectral_bandwidth_var = pd.Series()

    spectral_contrast_mean = pd.Series()
    spectral_contrast_std = pd.Series()
    spectral_contrast_var = pd.Series()

    spectral_flatness_mean = pd.Series()
    spectral_flatness_std = pd.Series()
    spectral_flatness_var = pd.Series()

    spectral_rolloff_mean = pd.Series()
    spectral_rolloff_std = pd.Series()
    spectral_rolloff_var = pd.Series()

    poly_features_mean = pd.Series()
    poly_features_std = pd.Series()
    poly_features_var = pd.Series()

    tonnetz_mean = pd.Series()
    tonnetz_std = pd.Series()
    tonnetz_var = pd.Series()

    zero_crossing_rate_mean = pd.Series()
    zero_crossing_rate_std = pd.Series()
    zero_crossing_rate_var = pd.Series()

    frame_mean = pd.Series()
    frame_std = pd.Series()
    frame_var = pd.Series()

    harmonic_mean = pd.Series()
    harmonic_std = pd.Series()
    harmonic_var = pd.Series()

    percussive_mean = pd.Series()
    percussive_std = pd.Series()
    percussive_var = pd.Series()

    # Importing Audio File
    song_name = path + tail
    y, sampling_rate = librosa.load(song_name, duration=60)  # y = audio time series
    S = np.abs(librosa.stft(y))

    # Extracting Features

    # Spectral Features
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sampling_rate)
    chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sampling_rate)
    chroma_cens = librosa.feature.chroma_cens(y=y, sr=sampling_rate)
    melspectrogram = librosa.feature.melspectrogram(S=S)
    mfcc = librosa.feature.mfcc(S=S)
    delta_mfcc = librosa.feature.delta(mfcc)
    rms = librosa.feature.rms(S=S)
    spectral_centroid = librosa.feature.spectral_centroid(S=S)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(S=S)
    spectral_contrast = librosa.feature.spectral_contrast(S=S)
    spectral_flatness = librosa.feature.spectral_flatness(S=S)
    spectral_rolloff = librosa.feature.spectral_rolloff(S=S)
    poly_features = librosa.feature.poly_features(S=S)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sampling_rate)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)

    # Rhythm Features
    tempo, beats = librosa.beat.beat_track(y=y, sr=sampling_rate)  # BPM

    # Onset Detection
    onset_frames = librosa.onset.onset_detect(y=y, sr=sampling_rate)
    frames_to_time = librosa.frames_to_time(onset_frames[:20], sr=sampling_rate)

    # Effects
    harmonic = librosa.effects.harmonic(y)
    percussive = librosa.effects.percussive(y)

    # Transforming Features
    songname_vector.at[song_id] = tail  # song name
    tempo_vector.at[song_id] = tempo  # tempo
    total_beats.at[song_id] = sum(beats)  # beats
    average_beats.at[song_id] = np.average(beats)

    chroma_stft_mean.at[song_id] = np.mean(chroma_stft)  # chroma stft
    chroma_stft_std.at[song_id] = np.std(chroma_stft)
    chroma_stft_var.at[song_id] = np.var(chroma_stft)

    chroma_cqt_mean.at[song_id] = np.mean(chroma_cqt)  # chroma cqt
    chroma_cqt_std.at[song_id] = np.std(chroma_cqt)
    chroma_cqt_var.at[song_id] = np.var(chroma_cqt)

    chroma_cens_mean.at[song_id] = np.mean(chroma_cens)  # chroma cens
    chroma_cens_std.at[song_id] = np.std(chroma_cens)
    chroma_cens_var.at[song_id] = np.var(chroma_cens)

    melspectrogram_mean.at[song_id] = np.mean(melspectrogram)  # melspectrogram
    melspectrogram_std.at[song_id] = np.std(melspectrogram)
    melspectrogram_var.at[song_id] = np.var(melspectrogram)

    mfcc_mean.at[song_id] = np.mean(mfcc)  # mfcc
    mfcc_std.at[song_id] = np.std(mfcc)
    mfcc_var.at[song_id] = np.var(mfcc)

    delta_mfcc_mean.at[song_id] = np.mean(delta_mfcc)  # mfcc delta
    delta_mfcc_std.at[song_id] = np.std(delta_mfcc)
    delta_mfcc_var.at[song_id] = np.var(delta_mfcc)

    rms_mean.at[song_id] = np.mean(rms)  # rms
    rms_std.at[song_id] = np.std(rms)
    rms_var.at[song_id] = np.var(rms)

    spectral_centroid_mean.at[song_id] = np.mean(spectral_centroid)  # spectral_centroid
    spectral_centroid_std.at[song_id] = np.std(spectral_centroid)
    spectral_centroid_var.at[song_id] = np.var(spectral_centroid)

    spectral_bandwidth_mean.at[song_id] = np.mean(spectral_bandwidth)  # spectral bandwidth
    spectral_bandwidth_std.at[song_id] = np.std(spectral_bandwidth)
    spectral_bandwidth_var.at[song_id] = np.var(spectral_bandwidth)

    spectral_contrast_mean.at[song_id] = np.mean(spectral_contrast)  # spectral_contrast
    spectral_contrast_std.at[song_id] = np.std(spectral_contrast)
    spectral_contrast_var.at[song_id] = np.var(spectral_contrast)

    spectral_flatness_mean.at[song_id] = np.mean(spectral_flatness)  # spectral_flatness
    spectral_flatness_std.at[song_id] = np.std(spectral_flatness)
    spectral_flatness_var.at[song_id] = np.var(spectral_flatness)

    spectral_rolloff_mean.at[song_id] = np.mean(spectral_rolloff)  # spectral_rolloff
    spectral_rolloff_std.at[song_id] = np.std(spectral_rolloff)
    spectral_rolloff_var.at[song_id] = np.var(spectral_rolloff)

    poly_features_mean.at[song_id] = np.mean(poly_features)  # poly_features
    poly_features_std.at[song_id] = np.std(poly_features)
    poly_features_var.at[song_id] = np.var(poly_features)

    tonnetz_mean.at[song_id] = np.mean(tonnetz)  # tonnetz
    tonnetz_std.at[song_id] = np.std(tonnetz)
    tonnetz_var.at[song_id] = np.var(tonnetz)

    zero_crossing_rate_mean.at[song_id] = np.mean(zero_crossing_rate)  # zero_crossing_rate
    zero_crossing_rate_std.at[song_id] = np.std(zero_crossing_rate)
    zero_crossing_rate_var.at[song_id] = np.var(zero_crossing_rate)

    frame_mean.at[song_id] = np.mean(frames_to_time)  # frames
    frame_std.at[song_id] = np.std(frames_to_time)
    frame_var.at[song_id] = np.var(frames_to_time)

    harmonic_mean.at[song_id] = np.mean(harmonic)  # harmonic
    harmonic_std.at[song_id] = np.std(harmonic)
    harmonic_var.at[song_id] = np.var(harmonic)

    percussive_mean.at[song_id] = np.mean(percussive)  # percussive
    percussive_std.at[song_id] = np.std(percussive)
    percussive_var.at[song_id] = np.var(percussive)

    # Concatenating Features into one csv and json format
    feature_set['file_name'] = songname_vector  # song name
    feature_set['valence_mean'] = valence_mean_vector
    feature_set['arousal_mean'] = arousal_mean_vector
    feature_set['tempo'] = tempo_vector  # tempo
    feature_set['total_beats'] = total_beats  # beats
    feature_set['average_beats'] = average_beats

    feature_set['chroma_stft_mean'] = chroma_stft_mean  # chroma stft
    feature_set['chroma_stft_std'] = chroma_stft_std
    feature_set['chroma_stft_var'] = chroma_stft_var

    feature_set['chroma_cqt_mean'] = chroma_cqt_mean  # chroma cqt
    feature_set['chroma_cqt_std'] = chroma_cqt_std
    feature_set['chroma_cqt_var'] = chroma_cqt_var

    feature_set['chroma_cens_mean'] = chroma_cens_mean  # chroma cens
    feature_set['chroma_cens_std'] = chroma_cens_std
    feature_set['chroma_cens_var'] = chroma_cens_var

    feature_set['melspectrogram_mean'] = melspectrogram_mean  # melspectrogram
    feature_set['melspectrogram_std'] = melspectrogram_std
    feature_set['melspectrogram_var'] = melspectrogram_var

    feature_set['mfcc_mean'] = mfcc_mean  # mfcc
    feature_set['mfcc_std'] = mfcc_std
    feature_set['mfcc_var'] = mfcc_var

    feature_set['delta_mfcc_mean'] = delta_mfcc_mean  # mfcc delta
    feature_set['delta_mfcc_std'] = delta_mfcc_std
    feature_set['delta_mfcc_var'] = delta_mfcc_var

    feature_set['rms_mean'] = rms_mean  # rms
    feature_set['rms_std'] = rms_std
    feature_set['rms_var'] = rms_var

    feature_set['spectral_centroid_mean'] = spectral_centroid_mean  # spectral_centroid
    feature_set['spectral_centroid_std'] = spectral_centroid_std
    feature_set['spectral_centroid_var'] = spectral_centroid_var

    feature_set['spectral_bandwidth_mean'] = spectral_bandwidth_mean  # spectral_bandwidth
    feature_set['spectral_bandwidth_std'] = spectral_bandwidth_std
    feature_set['spectral_bandwidth_var'] = spectral_bandwidth_var

    feature_set['spectral_contrast_mean'] = spectral_contrast_mean  # spectral_contrast
    feature_set['spectral_contrast_std'] = spectral_contrast_std
    feature_set['spectral_contrast_var'] = spectral_contrast_var

    feature_set['spectral_rolloff_mean'] = spectral_rolloff_mean  # spectral_rolloff
    feature_set['spectral_rolloff_std'] = spectral_rolloff_std
    feature_set['spectral_rolloff_var'] = spectral_rolloff_var

    feature_set['poly_features_mean'] = poly_features_mean  # poly_features
    feature_set['poly_features_std'] = poly_features_std
    feature_set['poly_features_var'] = poly_features_var

    feature_set['tonnetz_mean'] = tonnetz_mean  # tonnetz
    feature_set['tonnetz_std'] = tonnetz_std
    feature_set['tonnetz_var'] = tonnetz_var

    feature_set['zero_crossing_rate_mean'] = zero_crossing_rate_mean  # zero_crossing_rate
    feature_set['zero_crossing_rate_std'] = zero_crossing_rate_std
    feature_set['zero_crossing_rate_var'] = zero_crossing_rate_var

    feature_set['harmonic_mean'] = harmonic_mean  # harmonic
    feature_set['harmonic_std'] = harmonic_std
    feature_set['harmonic_var'] = harmonic_var

    feature_set['percussive_mean'] = percussive_mean  # percussive
    feature_set['percussive_std'] = percussive_std
    feature_set['percussive_var'] = percussive_var

    feature_set['frame_mean'] = frame_mean  # frames
    feature_set['frame_std'] = frame_std
    feature_set['frame_var'] = frame_var

    file_path = glob.glob('data/test_audio/*.mp3')
    for f in file_path:
        os.remove(f)
    return feature_set

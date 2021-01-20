from music21 import features
from music21 import converter
import argparse
import os
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("-S", "--songs", help="path to songs for which you want to extract features")


initial_tempo = [] # more features can be added as desired

column_names = ["condition", "initial_tempo", "note_duration", "melodic_interval", "motion_direction", "strongest_pitch", "pitches_classes", "importance_bass", "importance_middle", "importance_height"]

df = []

datasets = ["christmas", "mixed", "dutch"]

for dataset in datasets:
    condition = dataset
    for song in os.listdir('../dataset_sample/'+dataset):
        splitted = os.path.splitext(song)
        extension = splitted[len(splitted)-1]
        if extension != ".midi" and extension != ".abc":
            continue

        song_path = os.path.join('../dataset_sample/'+dataset, song)

        try:
            s = converter.parse(song_path)
        except:
            print("Could not convert " + song)
            continue

        try:
            fe = features.jSymbolic.InitialTempoFeature(s)
            f = fe.extract()
            initial_tempo = f.vector[0]

            fe = features.jSymbolic.AverageNoteDurationFeature(s)
            f = fe.extract()
            note_duration = f.vector[0]

            fe = features.jSymbolic.AverageMelodicIntervalFeature(s)
            f = fe.extract()
            melodic_interval = f.vector[0]

            fe = features.jSymbolic.DirectionOfMotionFeature(s)
            f = fe.extract()
            motion_direction = f.vector[0]

            fe = features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature(s)
            f = fe.extract()
            strongest_pitch = f.vector[0]

            fe = features.jSymbolic.PitchClassDistributionFeature(s)
            f = fe.extract()
            pitches_classes = f.vector

            fe = features.jSymbolic.ImportanceOfBassRegisterFeature(s)
            f = fe.extract()
            importance_bass = f.vector[0]

            fe = features.jSymbolic.ImportanceOfMiddleRegisterFeature(s)
            f = fe.extract()
            importance_middle = f.vector[0]

            fe = features.jSymbolic.ImportanceOfHighRegisterFeature(s)
            f = fe.extract()
            importance_height = f.vector[0]

            df.append([condition, initial_tempo, note_duration, melodic_interval, motion_direction, strongest_pitch, pitches_classes, importance_bass, importance_middle, importance_height])

        except:
            print("Feature could not be extracted for " + song)

print(df)
dfcsv = pd.DataFrame(df, columns = column_names)
dfcsv.to_csv('features.csv')
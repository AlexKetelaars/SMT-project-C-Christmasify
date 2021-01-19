from music21 import features
from music21 import converter
import argparse
import os
import matplotlib.pyplot as plt
import statistics
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("-S", "--songs", help="path to songs for which you want to extract features")
args = parser.parse_args()

if not args.songs:
    print("Please input the path to the songs you want to extract features for.")
    print("Usage: -S path/to/songs")
    exit()


initial_tempo = [] # more features can be added as desired

column_names = ["condition", "initial_tempo", "note_duration", "melodic_interval", "motion_direction", "strongest_pitch"]

condition = "dutch"
df = []

for song in os.listdir(args.songs):
    splitted = os.path.splitext(song)
    extension = splitted[len(splitted)-1]
    if extension != ".midi" and extension != ".abc":
        continue

    song_path = os.path.join(args.songs, song)

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

        df.append([condition, initial_tempo, note_duration, melodic_interval, motion_direction, strongest_pitch])

    except:
        print("Initial Tempo could not be extracted for " + song)

dfcsv = pd.DataFrame(df, columns = column_names)
dfcsv.to_csv('features.csv')
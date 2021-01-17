from music21 import features
from music21 import converter
import argparse
import os
import matplotlib.pyplot as plt
import statistics


parser = argparse.ArgumentParser()
parser.add_argument("-S", "--songs", help="path to songs for which you want to extract features")
args = parser.parse_args()

if not args.songs:
    print("Please input the path to the songs you want to extract features for.")
    print("Usage: -S path/to/songs")
    exit()


initial_tempo = [] # more features can be added as desired

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
        print("Initial Tempo for " + song + ": " + str(f.vector[0]))
        initial_tempo.append(f.vector[0])
    except:
        print("Initial Tempo could not be extracted for " + song)


print("\nFinal statistics for Initial Tempo")
print("Mean: " + str(statistics.mean(initial_tempo)))
print("Standard deviation: " + str(statistics.stdev(initial_tempo)))
print("Minimum value: " + str(min(initial_tempo)))
print("Maximum value: " + str(max(initial_tempo)) + "\n")

plt.hist(initial_tempo, bins = 20, color = 'blue', edgecolor = 'black')
plt.title("Initial Tempo feature distribution")
plt.xlabel("Initial Tempo")
plt.ylabel("Frequency")
plt.show()
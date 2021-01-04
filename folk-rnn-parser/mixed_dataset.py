import random

token = 'T:'

dutch_songs = []
current_chunk = []
for line in open("../parsed-datasets/dataset_dutch.txt"):
    if line.startswith(token) and current_chunk:
        # if line starts with token and the current chunk is not empty
        dutch_songs.append(current_chunk[:])  # add not empty chunk to chunks
        current_chunk = []  # make current chunk blank
    # just append a line to the current chunk on each iteration
    current_chunk.append(line)
dutch_songs.append(current_chunk)  # append the last chunk outside the loop

christmas_songs = []
current_chunk = []
for line in open("../parsed-datasets/dataset_christmas.txt"):
    if line.startswith(token) and current_chunk:
        # if line starts with token and the current chunk is not empty
        christmas_songs.append(current_chunk[:])  # add not empty chunk to chunks
        current_chunk = []  # make current chunk blank
    # just append a line to the current chunk on each iteration
    current_chunk.append(line)
christmas_songs.append(current_chunk)  # append the last chunk outside the loop

dutch_songs_half = random.sample(dutch_songs, 1844)
christmas_songs_half = random.sample(christmas_songs, 1844)

print(len(christmas_songs))
print(len(dutch_songs))
print(len(christmas_songs_half))
print(len(dutch_songs_half))

mixed = dutch_songs_half
mixed.extend(christmas_songs_half)
random.shuffle(mixed)

print(len(mixed))

f = open("../parsed-datasets/dataset_mixed.txt", 'w')
i = 0
for ele in dutch_songs_half:
    i=i+1
    for line in ele:
        f.write(line)
    f.write('\n')

print(i)

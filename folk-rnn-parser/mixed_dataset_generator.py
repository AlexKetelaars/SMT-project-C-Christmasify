import random

## IMPORTANT! Datasets must be of the same length, probably christmas is smaller. lengths should also be dividable by 2 for the mixed!
if __name__ == "__main__":
    token = 'L:'

    dutch_songs = []
    current_chunk = []
    for line in open("../datasets_parsed/fixed_parsed_dutch.txt"):
        if line.startswith(token) and current_chunk:
            # if line starts with token and the current chunk is not empty
            dutch_songs.append(current_chunk[:])  # add not empty chunk to chunks
            current_chunk = []  # make current chunk blank
        # just append a line to the current chunk on each iteration
        current_chunk.append(line)
    dutch_songs.append(current_chunk)  # append the last chunk outside the loop

    christmas_songs = []
    current_chunk = []
    for line in open("../datasets_parsed/fixed_parsed_christmas.txt"):
        if line.startswith(token) and current_chunk:
            # if line starts with token and the current chunk is not empty
            christmas_songs.append(current_chunk[:])  # add not empty chunk to chunks
            current_chunk = []  # make current chunk blank
        # just append a line to the current chunk on each iteration
        current_chunk.append(line)
    christmas_songs.append(current_chunk)  # append the last chunk outside the loop

    # print input dataset sizes
    print('Input dutch songs: ', len(dutch_songs))
    print('Input dutch songs: ', len(christmas_songs))

    # since datasets_original have different lengths, consider the smaller
    n_song = min(len(dutch_songs), len(christmas_songs))

    # if n_song is not even, reduce by one. otherwise mixed dataset cannot be 50-50%
    if n_song % 2 != 0:
        n_song -= 1

    print("Min dataset size: ", n_song)

    # trim randomly input datasets_original, to have same min size
    if len(dutch_songs) > n_song:
        dutch_songs = random.sample(dutch_songs, n_song)
    if len(christmas_songs) > n_song:
        dutch_songs = random.sample(dutch_songs, n_song)

    # check new dataset sizes
    print('New size dutch songs: ', len(dutch_songs))
    print('New size dutch songs: ', len(christmas_songs))

    n_song_half = int(n_song / 2)

    dutch_songs_half = random.sample(dutch_songs, n_song_half)
    christmas_songs_half = random.sample(christmas_songs, n_song_half)

    # start mixed model adding the dutch ones
    mixed_songs = dutch_songs_half
    # add the christmas ones
    mixed_songs.extend(christmas_songs_half)
    # randomize order
    random.shuffle(mixed_songs)

    print("Mixed dataset length: ", len(mixed_songs))

    if len(mixed_songs) == len(dutch_songs) & len(mixed_songs) == len(christmas_songs):
        print('Everything correct!')

    # write all datasets_original to file

    f = open("../datasets_parsed/rnn_dataset_mixed.txt", 'w')
    i = 0
    for ele in mixed_songs:
        i = i + 1
        for line in ele:
            f.write(line)
    print('Written to file', i,'songs mixed dataset')

    f = open("../datasets_parsed/rnn_dataset_dutch.txt", 'w')
    i = 0
    for ele in dutch_songs:
        i = i + 1
        for line in ele:
            f.write(line)
    print('Written to file', i,'songs dutch dataset')

    f = open("../datasets_parsed/rnn_dataset_christmas.txt", 'w')
    i = 0
    for ele in christmas_songs:
        i = i + 1
        for line in ele:
            f.write(line)
    print('Written to file', i,'songs christmas dataset')

    print('IMPORTANT: remember to manually delete the last newline(s)!')
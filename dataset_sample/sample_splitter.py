dataset_type= 'mixed'

filename = "dataset_"+dataset_type+".txt"

with open(filename) as f:
    content = f.readlines()

    i = 0
    ind_song = ''
    for line in content:
        if line != '\n':
            ind_song += line
        else:
            i += 1
            with open("individuals_"+dataset_type+"/"+dataset_type+"_" + str(i) + ".abc", "w") as text_file:
                text_file.write(ind_song)
            ind_song = ''

    print("Number of songs split:", i)

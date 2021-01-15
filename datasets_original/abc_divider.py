for k in range(1, 20):
    filename = "datasets_original/abc_dutch_folk/allnlb"+str(k)+"000.abc"

    with open(filename) as f:
        content = f.readlines()


    i=0
    ind_song = ''
    for line in content:

        if (line != '\n'):
            ind_song+=line
        else:
            i+=1
            with open("datasets_original/abc_dutch/song"+str(k)+"_"+str(i)+".abc", "w") as text_file:
                text_file.write(ind_song)
            ind_song = ''
    print(i)
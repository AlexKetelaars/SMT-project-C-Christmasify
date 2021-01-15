import re


def post_rnn_parser_parser():
    return


if __name__ == "__main__":

    # l = "[ C, A, ] | [ D, A, ]"

    # l = re.sub(r"([\[]) +([A-Ga-g0-9/,]) +([\]])", r"\1\3", l)
    # print(l)
    count = 0
    filename = "../parsed-datasets/original_parsed_dutch.txt"
    s = ""
    bool_K = False
    with open(str(filename), "r") as f:
        for l in f.readlines():

            if bool_K:
                # Removing L k and M features inside the body of the song
                l = re.sub(r"\[L:(.+?)\]", "", l)
                l = re.sub(r"\[K:(.+?)\]", "", l)
                l = re.sub(r"\[M:(.+?)\]", "", l)

                # Duration (A 2)
                l = re.sub(r"([A-Za-z]) +([0-9])", r"\1\2", l)

                # Duration (A / or A /2)
                l = re.sub(r"([A-Za-z]) +([/])", r"\1\2", l)

                # Duration (/ /)
                l = re.sub(r"([/]) +([/])", r"\1\2", l)

                # Duration (, /)
                l = re.sub(r"([,]) +([/])", r"\1\2", l)

                # Octave (A ,)
                l = re.sub(r"([A-Za-z]) +([,])", r"\1\2", l)

                # Octave (2 , or A/3 ,)
                l = re.sub(r"([0-9]) +([,])", r"\1\2", l)

                # byMarco (, 2)
                l = re.sub(r"([,]) +([0-9])", r"\1\2", l)

                # Octave (, ,)
                l = re.sub(r"([,]) +([,])", r"\1\2", l)

                # delete all white spaces inside of [] to make it an individual note
                l = re.sub(r'\[.*?\]', lambda x: ''.join(x.group(0).split()), l)

                # remove all :| and |:
                l = l.replace(":|", "|")
                if l.startswith('|: '):
                    l = l[3:]
                l = l.replace("|: ", "|")


                # discard tracks with empty segments | |
                regexp = re.compile(r"([|]) +([|])")
                if regexp.search(l):
                    count+=1
                    print (l)
                    continue

                bool_K = False

            if l[:2] == "T:":
                continue
            if l[:3] == "[L:" or l[:3] == "[M:" or l[:3] == "[K:":
                s += l[1:-2] + l[-1:]
                if l[:3] == "[K:":
                    bool_K = True
                continue
            s += l

    with open("final_" + str(filename), "w") as f:
        f.write(s)

    print(count)
# -*- coding: utf-8 -*-


def save_to_file(vids_dict, filename):
    """
    Saves comments from a dictionary to a file given a dictionary and
    filename
    """
    f = open(filename, 'w')
    for video in vids_dict:
        f.write(video + ' Video ID' + "\n")
        for comments in vids_dict.values():
            for string in comments:
                if type(string) is str:
                    f.write(string + '\n')
    f.close()


def load_from_file(filename):
    """
    Loads comments into a dictionary from file given "filename"
    """
    vids_dict = {}

    f = open(filename, 'r')

    video_id = None

    for line in f:
        if line.endswith('Video ID'):
            video_id = line[0:11]
        else:
            comment_list = [line for line in f]

        vids_dict[video_id] = comment_list
    f.close()

    return vids_dict

if __name__ == "__main__":
    print "Hello"

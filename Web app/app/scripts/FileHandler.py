# -*- coding: utf-8 -*-


def save_to_file(vids_dict, filename):
    """
    Saves comments from a dictionary to a file given a dictionary and
    filename
    """
    f = open(filename, 'w')
    for video in vids_dict:
        f.write(video + ' Video ID')
        for comment in vids_dict.values:
            if type(comment) is str:
                f.write(comment + '\n')
    f.close()


def load_from_file(filename):
    """
    Loads comments into a dictionary from file given "filename"
    """
    vids_dict = {}

    f = open(filename, 'r')

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

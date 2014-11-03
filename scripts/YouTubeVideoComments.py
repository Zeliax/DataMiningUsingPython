# -*- coding: utf-8 -*-
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import gdata.youtube.service
import config

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = config.DEVELOPER_KEY
YOUTUBE_API_SERVICE_NAME = config.YOUTUBE_API_SERVICE_NAME
YOUTUBE_API_VERSION = config.YOUTUBE_API_VERSION

USERNAME = config.EMAIL
PASSWORD = config.PASSWORD


def fetch_video_list(options):
    """
    Function using YouTube API V3 to fetch videos from YouTube and returning a
    list of video names including video id
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))

    return videos


def format_video_lists(search, results):
    """
    Based on two input parameters, this function uses another function to
    to fetch a list of youtube videos and their matching IDs. It also sorts out
    the list from
    """
    argparser.add_argument("--q", help="Search term", default=search)
    argparser.add_argument("--max-results", help="Max results",
                           default=results)
    args = argparser.parse_args()

    try:
        video_list = fetch_video_list(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    vid_ids_list = []
    vid_name_list = []

    for v in video_list:
        vid_ids_list.append(v.split('(')[-1][:-1])
        paran_count = v.count("(")
        #If a paranthesis exists in title get the last occurance of the
        #paranthesis
        if paran_count > 1:
            vid = v.split("(")
            vid_name = "(".join(vid[:paran_count])
            vid_name_list.append(vid_name)
        else:
            vid_name_list.append(v.split(' (')[:1][-1])

    return vid_ids_list, vid_name_list


def fetch_video_comments(video_ids_list):
    """
    Based on a list of video ids this function returns a dictionary with a list
    of comments in which the key is the video id.
    """
    comments = {}

    print "Downloading comments"
    for i, _ in enumerate(vid_ids_list):
        print "---------Downloading Comments for--------"
        print "Video ID:", vid_ids_list[i]
        print "Video Name:", vid_name_list[i].encode("utf-8"), "\n"

        comment_list = [comment.content.text for comment in
                        yts.GetYouTubeVideoCommentFeed
                        (video_id=vid_ids_list[i]).entry]
        comments[vid_ids_list[i]] = comment_list
    print "Done"

    return comments


def save_comments_to_file(comment_list):
    """
    Saves comments to a file
    """
    f = open('testfile.txt', 'w')
    for comment in comment_list:
        f.writelines(comment.replace("\n", " ") + "\n")
    f.close()


if __name__ == "__main__":
    yts = gdata.youtube.service.YouTubeService()

    search_word = "Dog"
    results = 1

    vid_ids_list, vid_name_list = format_video_lists(search_word, results)
    comments = fetch_video_comments(vid_ids_list)

    video_comments = comments.values()[0]
    save_comments_to_file(video_comments)

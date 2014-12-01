# -*- coding: utf-8 -*-
from apiclient.discovery import build
from apiclient.errors import HttpError
# from oauth2client import tools
from gdata.youtube import service

import config
import pafy
import argparse

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = config.DEVELOPER_KEY
YOUTUBE_API_SERVICE_NAME = config.YOUTUBE_API_SERVICE_NAME
YOUTUBE_API_VERSION = config.YOUTUBE_API_VERSION
YTS = service.YouTubeService()


def youtube_search(options):
    """Performs a YouTube search using Google API V3 and formats list to
    desired output.

    Function using YouTube API V3 to fetch videos from YouTube and returning a
    list of video ids and a list video names by splitting the list returned
    returned from the api call.
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
  # matching videos, channels, and playlists
    for search_result in search_response.get("items", []):
        # If result matches a video, append it to the video list
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))

    #Splitting and formatting the video list:
    video_ids_list = []
    video_names_list = []

    for video in videos:
        video_ids_list.append(video.split('(')[-1][:-1])
        paran_count = video.count("(")
        #If a paranthesis exists in title get the last occurance of the
        #paranthesis
        if paran_count > 1:
            video = video.split("(")
            video_name = "(".join(video[:paran_count])
            video_names_list.append(video_name)
        else:
            video_names_list.append(video.split(' (')[:1][-1])

    return video_ids_list, video_names_list


# def split_video_list(search, result_nr=1):
#     """Splits internal list into a more desired format.

#     Based on two input parameters, this function uses another function to
#     to fetch a list of youtube videos and their matching IDs. It also formats
#     the list and splits it into two, which is returns.
#     """
#     argparser = argparse.ArgumentParser(add_help=False)
#     argparser.add_argument("--q", help="Search term", default=search)
#     argparser.add_argument("--max-results", help="Max results",
#                            default=result_nr)
#     args = argparser.parse_args()

#     try:
#         video_list = youtube_search(args)
#     except HttpError, e:
#         print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

#     vid_ids_list = []
#     vid_name_list = []

#     for v in video_list:
#         vid_ids_list.append(v.split('(')[-1][:-1])
#         paran_count = v.count("(")
#         #If a paranthesis exists in title get the last occurance of the
#         #paranthesis
#         if paran_count > 1:
#             vid = v.split("(")
#             vid_name = "(".join(vid[:paran_count])
#             vid_name_list.append(vid_name)
#         else:
#             vid_name_list.append(v.split(' (')[:1][-1])

#     return vid_ids_list, vid_name_list


def comments_generator(client, video_id):
    """Uses gdata api to download comments given a video id."""
    urlpattern = ('http://gdata.youtube.com/feeds/api/videos/' + video_id +
                  '/comments?orderby=published&start-index=%d&max-results=25')
    index = 1
    url = urlpattern % index
    comment_feed = client.GetYouTubeVideoCommentFeed(uri=url)
    while comment_feed is not None:
        for comment in comment_feed.entry:
            yield comment
        next_link = comment_feed.GetNextLink()
        if next_link is None:
            comment_feed = None
        else:
            try:
                comment_feed = client.GetYouTubeVideoCommentFeed(
                    next_link.href)
            except Exception, e:
                print e
                break


def get_video_name(name_list):
    """Given a list of strings, returns a list utf-8 encoded strings."""
    name_list = [name.encode('utf-8') for name in name_list]
    return name_list


def get_video_link(id_list):
    """Given a list of IDs, returns a list of links."""
    link_list = ['https://www.youtube.com/watch?v=' + str(ids) for ids
                 in id_list]
    return link_list


def get_video_rating(url):
    """Downloads likes and dislikes in a list based on video url."""
    video = pafy.new(url)
    return [video.likes, video.dislikes]


def main_func(search_word, nr_of_results):
    """
    Function that collects all other functions and performs YouTube search,
    and returns a dictionary with comments for all the videos found.
    """

    argparser = argparse.ArgumentParser(add_help=False)
    argparser.add_argument("--q", help="Search term", default=search_word)
    argparser.add_argument("--max-results", help="Max results",
                           default=nr_of_results)
    args = argparser.parse_args()

    try:
        video_ids_list, video_names_list = youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    names = get_video_name(video_names_list)
    links = get_video_link(video_ids_list)

    comment_list = []
    for video_id in video_ids_list:
        comment_list.append([comment.content.text for comment in
                             comments_generator(YTS, video_id)
                             if comment.content.text is not None])

    return comment_list, names, links


def main():
    """Used for manual testing of functions."""
    searchList = ['dolphin', 'dog']
    # search_dict = {}

    search_word = searchList[0]
    nr_of_results = 1

    url = "https://www.youtube.com/watch?v=OoOHkJYeFDg"

    get_video_rating(url)

    # Dictionary containing all the videos and their corresponding comments
    comments_list, names_list, links_list = main_func(
        search_word, nr_of_results)

if __name__ == "__main__":
    main()

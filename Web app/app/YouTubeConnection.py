# -*- coding: utf-8 -*-
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from gdata.youtube import service

import config

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = config.DEVELOPER_KEY
YOUTUBE_API_SERVICE_NAME = config.YOUTUBE_API_SERVICE_NAME
YOUTUBE_API_VERSION = config.YOUTUBE_API_VERSION
YTS = service.YouTubeService()


def YouTube_V3_Search(options):
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


def split_video_list(search, result_nr):
    """
    Based on two input parameters, this function uses another function to
    to fetch a list of youtube videos and their matching IDs. It also sorts out
    the list from
    """
    argparser.add_argument("--q", help="Search term", default=search)
    argparser.add_argument("--max-results", help="Max results",
                           default=result_nr)
    args = argparser.parse_args()

    try:
        video_list = YouTube_V3_Search(args)
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


def comments_generator(client, video_id):
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
    """
    Function that returns a list with names of the videos (used in the
    sentinemt analysis)
    """
    name_list = [name.encode('utf-8') for name in name_list]

    return name_list


def get_video_link(link_list):
    """
    Function that returns a link to the videos (direct shortcut to go to video)
    """
    link_list = ['https://www.youtube.com/watch?v=' + str(link) for link
                 in link_list]

    return link_list


def main_func(search_word, nr_of_results):
    """
    Function that collects all other functions and performs YouTube search,
    and returns a dictionary with comments for all the videos found.
    """
    #Move to another function...
    vid_ids_list, vid_name_list = split_video_list(
        search_word, nr_of_results)

    names = get_video_name(vid_name_list)
    links = get_video_link(vid_ids_list)

    # vid_id_dict = {}
    for video_id in vid_ids_list:
        comment_list = [comment.content.text.decode('utf-8') for comment in
                        comments_generator(YTS, video_id)
                        if comment.content.text is not None]

    return comment_list, names, links


if __name__ == "__main__":
    search_list = ['dolphin', 'dog']
    # search_dict = {}

    search_word = search_list[0]
    nr_of_results = 1

    #Dictionary containing all the videos and their corresponding comments
    comments_list, names_list, links_list = main_func(
        search_word, nr_of_results)

    #Save comments to a file
    # f = open('testfile.txt', 'w')
    # for comment in comments_list:
    #     f.write(comment + '\n')
    # f.close()

    #Used to print all the video names line for line
    # for name in names_list:
    #     print name

    #Used to print all the links line for line
    # for link in links_list:
    #     print link

    #Used to print the comments "line for line" in comment dict
    # for comments in comments_dict.itervalues():
    #     for string in comments:
    #         print string

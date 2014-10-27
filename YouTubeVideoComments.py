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

yts = gdata.youtube.service.YouTubeService()


def youtube_search(options):
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


def get_vid_lists(search, results):
    argparser.add_argument("--q", help="Search term", default=search)
    argparser.add_argument("--max-results", help="Max results",
                           default=results)
    args = argparser.parse_args()

    try:
        video_list = youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    vid_id_list = []
    vid_name_list = []

    for v in video_list:
        vid_id_list.append(v.split('(')[-1][:-1])
        paran_count = v.count("(")
        #If a paranthesis exists in title get the last occurance of the
        #paranthesis
        if paran_count > 1:
            vid = v.split("(")
            vid_name = "(".join(vid[:paran_count])
            vid_name_list.append(vid_name)
        else:
            vid_name_list.append(v.split(' (')[:1][-1])

    return vid_id_list, vid_name_list


if __name__ == "__main__":
    search_word = "Dog"
    results = 1
    vid_id_list, vid_name_list = get_vid_lists(search_word, results)

    comments = {}

    print "Downloading comments"
    for i, _ in enumerate(vid_id_list):
        # print "---------Downloading Comments for--------"
        # print "Video ID:", vid_id_list[i]
        # print "Video Name:", vid_name_list[i].encode("utf-8"), "\n"11
        comment_feed = yts.GetYouTubeVideoCommentFeed(video_id=vid_id_list[i])
        while comment_feed is not None:
            for comment in comment_feed.entry:
                yield comment
            next_link = comment_feed.GetNextLink()
            if next_link is None:
                comment_feed = None
            else:
                comment_feed = yts.GetYouTubeVideoCommentFeed(next_link.href)
        # comment_list = [comment.content.text for comment in comment_feed
        # comments[vid_id_list[i]] = comment_list
    print "Done"

    video_comments = comments.values()[0]
    print len(comments.values()[0])

    for comment in video_comments:
        print comment

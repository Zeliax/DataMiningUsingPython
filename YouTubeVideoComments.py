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


def get_vid_lists(search):
    argparser.add_argument("--q", help="Search term", default=search)
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()

    try:
        video_list = youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    vid_id_list = []
    vid_name_list = []

    for v in video_list:
        vid_id_list.append(v.split('(')[-1][:-1])
        #If a paranthesis exists in title get the last occurance of the
        #paranthesis
        if v.count("(") > 1:
            vid_name_list.append(v.rsplit(" (", -1)[:1][-1])
        else:
            vid_name_list.append(v.split(' (')[:1][-1])

    return vid_id_list, vid_name_list


if __name__ == "__main__":
    search_word = "Dog"
    vid_id_list, vid_name_list = get_vid_lists(search_word)

    urlpattern = ('http://gdata.youtube.com/feeds/api/'
                  'videos/YoB8t0B4jx4/comments?start-index=%d&max-results=20')
    index = 1
    url = urlpattern % index
    comments = []

    for i in range(len(vid_id_list)):
        print "\n---------New video starting--------"
        print vid_id_list[i], vid_name_list[i]
        for comment in yts.GetYouTubeVideoCommentFeed(video_id=
                                                      vid_id_list[i]).entry:
            print comment.content.text

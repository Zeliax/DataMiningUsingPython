# -*- coding: utf-8 -*-
"""Used to download different data from YouTube."""
from apiclient.discovery import build
from apiclient.errors import HttpError
from gdata.youtube import service

import argparse
import pafy

import config


class YouTubeConnection(object):

    """Module with functions used to interact with YouTube."""

    def __init__(self, developer_key, youtube_api_version,
                 youtube_api_service_name):
        """Initialize the class with config parameters and YouTubeService."""
        self.yts = service.YouTubeService()
        self.developer_key = config.DEVELOPER_KEY
        self.youtube_api_version = config.YOUTUBE_API_VERSION
        self.youtube_api_service_name = config.YOUTUBE_API_SERVICE_NAME

    def youtube_search(self, arguments):
        """Perform a YouTube search and formats list to desired output.

        Function using YouTube API V3 to fetch videos from YouTube and
        returning a list of video ids and a list video names by splitting the
        list returned returned from the api call.
        """
        youtube = build(self.youtube_api_service_name,
                        self.youtube_api_version,
                        developerKey=self.developer_key)

        # Call the search.list method to retrieve results matching the
        # specified query term.
        search_response = youtube.search().list(
            q=arguments.q,
            part="id,snippet",
            maxResults=arguments.max_results
        ).execute()

        videos = []

      # Add each result to the appropriate list, and then display the lists of
      # matching videos, channels, and playlists
        for search_result in search_response.get("items", []):
            # If result matches a video, append it to the video list
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                           search_result["id"]["videoId"]))

        #Splitting and formatting the ''videos'' list:
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

    def comments_generator(self, video_id):
        """Using gdata api to download comments given a video id."""
        urlpattern = ('http://gdata.youtube.com/feeds/api/videos/' + video_id +
                      '/comments?orderby=published&start-index=%d&'
                      'max-results=35')
        index = 1
        url = urlpattern % index
        comment_feed = self.yts.GetYouTubeVideoCommentFeed(uri=url)
        while comment_feed is not None:
            for comment in comment_feed.entry:
                yield comment
            next_link = comment_feed.GetNextLink()
            if next_link is None:
                comment_feed = None
            else:
                try:
                    comment_feed = self.yts.GetYouTubeVideoCommentFeed(
                        next_link.href)
                except Exception, error_:
                    print error_
                    break

    def get_video_names(self, names_list):
        """Given a list of strings, returns a list utf-8 encoded strings."""
        names_list = [name.encode('utf-8') for name in names_list]
        return names_list

    def get_video_links(self, ids_list):
        """Given a list of IDs, returns a list of links."""
        links_list = ['https://www.youtube.com/watch?v=' + str(ids) for ids
                      in ids_list]
        return links_list

    def get_embedded_links(self, ids_list):
        """Given a list of IDs, returns a list of links with embeeded tag."""
        embedded_list = ['https://www.youtube.com/embed/' + str(ids) for ids in
                         ids_list]
        return embedded_list

    def get_video_rating(self, url_list):
        """Download likes and dislikes to a list based on video url."""
        rating_list = []
        for url in url_list:
            video = pafy.new(url)
            rating_list.append([video.likes, video.dislikes])
        return rating_list

    def main_func(self, search_word, nr_of_results):
        """Perform a youtube_search and returns different lists.

        Return:
        comment_list -> list with comments
        names -> list with video names
        links -> list with links for videos
        embedded -> list with links for embedded videos
        """
        argparser = argparse.ArgumentParser(add_help=False)
        argparser.add_argument("--q", help="Search term", default=search_word)
        argparser.add_argument("--max-results", help="Max results",
                               default=nr_of_results)
        args = argparser.parse_args()

        try:
            video_ids_list, video_names_list = self.youtube_search(args)
        except HttpError, error_:
            print "An HTTP error %d occurred:\n%s" % (error_.resp.status,
                                                      error_.content)

        names = self.get_video_names(video_names_list)
        links = self.get_video_links(video_ids_list)
        embedded = self.get_embedded_links(video_ids_list)

        comment_list = []
        for video_id in video_ids_list:
            comment_list.append([comment.content.text for comment in
                                 self.comments_generator(video_id)
                                 if comment.content.text is not None])

        return comment_list, names, links, embedded

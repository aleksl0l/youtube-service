import datetime
from typing import Union

import googleapiclient.discovery
from django.conf import settings


class YouTubeService:
    def __init__(self):
        self.service = googleapiclient.discovery.build("youtube", "v3", developerKey=settings.YOUTUBE_KEY)

    def fetch_videos(
            self,
            key_word: str,
            published_after: Union[datetime.datetime, None] = None,
            next_page_token: Union[str, None] = None
    ) -> dict:
        request = self.service.search().list(
            part="snippet",
            maxResults=50,
            q=key_word,
            pageToken=next_page_token,
            type="video",
            order="date",
            publishedAfter=published_after.isoformat() if published_after else None,
        )
        response = request.execute()
        return response


youtube_service = YouTubeService()


def map_raw_to_video(raw_item: dict) -> dict:
    return {
        "video_id": raw_item.get("id").get("videoId"),
        "title": raw_item.get("snippet").get("title"),
        "published_at": raw_item.get("snippet").get("publishedAt"),
    }

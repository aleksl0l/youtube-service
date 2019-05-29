from celery import shared_task
from django.utils import timezone

from core.models import Word, Video
from core.utils import youtube_service, map_raw_to_video


@shared_task
def create_videos(word_id: int) -> None:
    word = Word.objects.get(id=word_id)
    raw_response = youtube_service.fetch_videos(word.key_word, word.last_search)
    create_videos_from_response.delay(word_id, raw_response)

    next_page_token = raw_response.get("nextPageToken")
    while next_page_token:
        raw_response = youtube_service.fetch_videos(word.key_word, word.last_search, next_page_token)
        create_videos_from_response.delay(word_id, raw_response)
        next_page_token = raw_response.get("nextPageToken")
    word.last_search = timezone.now()
    word.save(update_fields=["last_search"])


@shared_task
def create_videos_from_response(word_id: int, raw_response: dict) -> None:
    items = raw_response.get("items")
    videos = []
    for item in items:
        video, created = Video.objects.get_or_create(**map_raw_to_video(item))
        videos.append(video)
    Word.objects.get(id=word_id).videos.add(*videos)


@shared_task(name="create_all_videos")
def create_all_videos() -> None:
    words = Word.objects.all()
    for word in words:
        create_videos.delay(word.id)

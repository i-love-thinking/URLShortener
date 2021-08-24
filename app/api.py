import uuid
from ninja import NinjaAPI, Schema
from .models import MappingUrl
import logging

api = NinjaAPI()


class Item(Schema):
    originUrl: str


class shortenedUrl(Schema):
    shortenedUrl: str


@api.post("/create_shorten_url")
def create(request, item: Item):
    logging.warning(item)
    result, created = MappingUrl.objects.get_or_create(originUrl=item.originUrl)
    if created:
        while True:
            shortenString = str(uuid.uuid1())[:8]
            check = MappingUrl.objects.filter(shortenString=shortenString)
            if len(check) == 0:
                result.shortenString = shortenString
                result.save()
                break
    return {'shortenedUrl': result.shortenString}

import os
import random

import io

from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.db import transaction
from faker import Factory
import requests

from web.models import Post

NUM_POSTS = 64


class Command(BaseCommand):
    help = "Setup test articles for the demo website"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Factory.create("en_AU")
        Post.objects.all().delete()
        for i in range(NUM_POSTS):
            print("Creating post", i)
            f = download_image(i)
            image = ImageFile(f, name=f"img-{i}.jpeg")
            Post.objects.create(title=fake.sentence(), image=image)


def download_image(idx):
    print(f"Downloading image {idx} from thispersondoesnotexist...")
    url = "https://thispersondoesnotexist.com/image"
    r = requests.get(url, stream=True)
    r.raise_for_status()
    return io.BytesIO(r.content)

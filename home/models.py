from django.db import models
from core.models import BaseModel

class AboutUs(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_url = models.CharField(max_length=250)
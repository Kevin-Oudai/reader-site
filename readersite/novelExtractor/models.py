from django.db import models

# Create your models here.
class Novel(models.Model):
    titleName = models.CharField(max_length=300)

class Chapters(models.Model):
    chapterName = models.ForeignKey(Novel, on_delete=models.CASCADE)
    url = models.URLField()
    nextUrl = models.URLField()
    prevUrl = models.URLField()
    content = models.TextField()
    
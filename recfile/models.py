from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime


# Create your models here.
class Recfile(models.Model):
    class Meta:
        db_table = "recfile"

    prog_title = models.CharField("番組タイトル", max_length=255)
    prog_channel = models.CharField("放送局", max_length=30)
    prog_id = models.CharField("Radiko番組ID", max_length=100)
    prog_ft = models.DateTimeField("放送開始日時")
    prog_to = models.DateTimeField("放送終了日時")
    prog_dur = models.IntegerField("放送時間")
    prog_url = models.CharField("番組URL", max_length=255)
    prog_desc = models.TextField("description")
    prog_info = models.TextField("information")
    prog_pfm = models.CharField("パーソナリティ", max_length=100)
    prog_img = models.CharField("画像URL", max_length=255)
    prog_hastag = models.CharField("Twitterハッシュタグ", max_length=255)
    prog_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['m4a'])])

    def __str__(self):
        return self.prog_title

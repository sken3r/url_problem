from django.db import models


class ShortURL(models.Model):
    main_url = models.URLField(db_index=True)
    short_id = models.CharField(max_length=30, primary_key=True)


class TraceOperation(models.Model):
    view_path = models.CharField(max_length=200, primary_key=True)
    hit_count = models.IntegerField(default=1)

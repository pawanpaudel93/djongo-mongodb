from djongo import models

class Tutorial(models.Model):
    title = models.CharField("Title", max_length=70, null=False)
    description = models.CharField("Description", max_length=200, null=False)
    published = models.BooleanField("Published", default=False)
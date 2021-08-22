from django.db import models
from django.db.models.fields.files import ImageField
import os
# Create your models here.
class DemoImage(models.Model):
    dimg = ImageField(upload_to='demoImages/')

    def __unicode__(self):
        return os.path.basename(self.dimg.name)

    def filename(self):
        return os.path.basename(self.dimg.name)

    def __str__(self):
        return self.filename()
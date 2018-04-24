from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class donnee_pharmacie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nom = models.URLField(max_length=100, blank=False, default='nothing')
    url_map = models.CharField(max_length=100, blank=True, default='')
    telephone = models.CharField(max_length=15)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    class Meta:
        ordering = ('created',)

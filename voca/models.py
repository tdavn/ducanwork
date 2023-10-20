from django.db import models
from django.urls import reverse

# Create your models here.
class Voca(models.Model):
    word_entry = models.CharField(max_length=250)
    word_def = models.TextField()
    illustration = models.ImageField(null=True, blank=True, upload_to='images/voca/')
    examples = models.TextField()
    thesaurus = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word_entry
    
    def get_absolute_url(self):
        return reverse('voca:word_detail', kwargs={'pk':self.pk})
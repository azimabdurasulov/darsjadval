from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 

class Article(models.Model):
    title = models.CharField(max_length=150,
    help_text="Yangilik sarlavhasini kiriting")
    summary = models.CharField(max_length=200, blank=True, 
    help_text="qisqa matn kiriting")
    body = RichTextField(help_text="Yangilik to`liq matnini kiriting")
    photo = models.ImageField(upload_to='images/', blank=True, 
    help_text="Rasmni yuklang")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

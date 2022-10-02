from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 
#kechkilar
class Birinchi(models.Model):
    title = models.CharField(max_length=150, help_text="nomini kiriting")
    photo = models.ImageField(upload_to='images/', blank=True, help_text="jadval rasmini yuklang")
    body = RichTextField(help_text="matn kiriting", blank=True,)    
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
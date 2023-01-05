from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone #added 

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})

class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date']

    title = models.CharField(max_length=200) #character field
    author = models.ForeignKey(
        get_user_model(), 
        on_delete = models.CASCADE #if user deleted, delete the post as well
    )
    pub_date = models.DateTimeField(default=timezone.now) #Timezone now means it automatically selected current date and time based on timezone
    content = models.TextField() #unrestricted text
    image_url = models.URLField(blank=True)#add image
    category = models.CharField(max_length=200, default='others')

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    story = models.ForeignKey(NewsStory, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(), related_name='comments', on_delete = models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
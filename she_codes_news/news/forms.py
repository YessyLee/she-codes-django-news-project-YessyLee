from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment, Category

#Add choices for categories
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

# class StoryForm(ModelForm):
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = [
            'title', 
            'category',
            'pub_date', 
            'image_url',
            'content'
            ]
        widgets = {
            'pub_date': forms.DateTimeInput(
                format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control', 'style': 'width: 200px;'})
            }

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']

class StoryUpdateForm(ModelForm):
    
    class Meta:
        model = NewsStory
        fields = ['title','image_url','content']
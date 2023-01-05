
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import NewsStory
from .forms import StoryForm, CommentForm, StoryUpdateForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all() #return all of the items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:3]
        context['all_stories'] = NewsStory.objects.all().order_by('pub_date')[:3]
        return context
    
def SearchStoryView(request): #search story by its category
    if request.method == 'POST':
        searched = request.POST['searched']
        stories = NewsStory.objects.filter(category__contains=searched) 
        
        return render(request, 'news/searchStory.html', {'searched':searched, 'stories':stories})
    
    else:
        return render(request, 'news/searchStory.html', {})

def CategoryView(request, cats):
    category_story = NewsStory.objects.filter(category=cats)
    return render(request, 'news/categories.html', {'cats': cats, 
'category_story':category_story})

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["form_action"] = reverse_lazy("news:addComment", kwargs={"pk": self.kwargs.get('pk')})
        return context
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateStoryView(generic.UpdateView):
    form_class = StoryUpdateForm
    model = NewsStory
    context_object_name = 'StoryUpdateForm'
    template_name = 'news/UpdateStory.html'
    # success_url = reverse_lazy('news:newsStory')

    def get_success_url(self) -> str:
        pk = self.kwargs.get('pk')
        return reverse_lazy('news:story', kwargs={'pk':pk})
    
class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/DeleteStory.html'
    success_url = reverse_lazy('news:index')
 
class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/createComment.html"
    # success_url = reverse_lazy('news:newsStory')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        pk = self.kwargs.get('pk')
        return reverse_lazy('news:story', kwargs={'pk':pk})
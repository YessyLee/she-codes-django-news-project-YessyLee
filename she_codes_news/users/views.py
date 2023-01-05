from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm, EditUserProfileForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:editProfile')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        f=super().form_valid(form)
        user = self.object
        login(self.request, user)
        return f

class EditUserProfileView(UpdateView):
    form_class = EditUserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/editProfile.html'
    
    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:profile', kwargs={"pk":self.request.user.id})

    def get_object(self):
        return self.request.user

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfileHome.html'


class AuthorsView(ListView):
    model = CustomUser
    template_name = 'users/viewAuthors.html'

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = CustomUser.objects.all()
        return context



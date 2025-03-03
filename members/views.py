from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from members.forms import ProfileUpdateForm
from .models import Profile
from mySEblog.models import Post


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    user_posts = Post.objects.filter(author=profile.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'profile': profile,
        'user_posts': user_posts,
        'form': form,
    }
    return render(request, 'profile.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage
# Create your views here.

#Add registration view for user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('chat_home')  # Redirect to chat home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/home.html', {'users': users})

@login_required
def chat_room(request, username):
    other_user = User.objects.get(username=username)
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user, receiver=other_user)) | (Q(sender=other_user, receiver=request.user))
    ).order_by('timestamp')    
    
    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'messages': messages
    })
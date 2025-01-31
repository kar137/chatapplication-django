from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import ChatMessage
from django.http import JsonResponse
import json
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
    users = User.objects.exclude(id=request.user.id)
    other_user = User.objects.get(username=username)
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user, receiver=other_user)) | (Q(sender=other_user, receiver=request.user))
    ).order_by('timestamp')    
    
    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'messages': messages,
        'users': users,
    })

@login_required
@require_POST
def send_message(request):
    data = json.loads(request.body)
    receiver_username = data.get('receiver')
    message_text = data.get('message')

    try:
        receiver = User.objects.get(username=receiver_username)
        message = ChatMessage.objects.create(
            sender=request.user,
            receiver=receiver,
            message=message_text
        )
        return JsonResponse({
            'status': 'success', 
            'message_id': message.id
        })
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error', 
            'message': 'Receiver not found'
        }, status=400)


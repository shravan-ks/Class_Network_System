import profile

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.
from chat.models import Chat, classroom


def home(request):
    chats = Chat.objects.all()
    ctx = {
        'home': 'active',
        'chat': chats
    }
    if request.user.is_authenticated:
        return render(request, 'chat.html', ctx)
    else:
        return render(request, 'core/index.html', None)


def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(user=request.user, message=msg)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg, 'user': chat_message.user.username})
    else:
        return HttpResponse('Request must be POST.')


def messages(request):
    chat = Chat.objects.all()
    return render(request, 'messages.html', {'chat': chat})


class IndexView(generic.ListView):
    context_object_name = 'classes'
    template_name = 'chatroom.html'

    def get_queryset(self):
        return classroom.objects.all()

from django.shortcuts import redirect, render
from django.http import HttpResponse
#from .forms import HelloForm
from .forms import FriendForm, FindForm
from django.views.generic import ListView, DetailView
from .models import Friend
from django.db.models import QuerySet
from django.db.models import Q

# Create your views here.

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += f'<td> {k} = {item[k]} </td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Index',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params={
        'title':'Create',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Create',
        'form':FriendForm(instance=obj),
        'id':num,
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title':'Create',
        'obj':friend,
        'id':num,
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        value = find.split()
        data = Friend.objects.filter(age__gte = value[0], age__lte = value[1])
        #data = Friend.objects.filter(Q(name__contains = find) | Q(mail__contains = find))
        #data = Friend.objects.filter(name__in = list)
        #data = Friend.objects.filter(name__icontains = find)
        message = f'検索結果：{data.count()}件'
    else:
        message = ''
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': message,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)
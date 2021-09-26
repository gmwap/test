from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView
from .models import Friend
from django.db.models import QuerySet

# Create your views here.

class HelloView(TemplateView):
    def __init__(self) :
        self.params = {
        'title':'Hello/index',
        'message':'Indexページ',
        'data':[],
        'form':HelloForm(),
    }

    def get(self, request):
        data = Friend.objects.all()
        self.params['data']=data
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        num = request.POST.get('id')
        item = Friend.objects.get(id=num)
        self.params['data'] = [item]
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)


def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += f'<td> {str(k)} = {str(item[k])} </td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        'message': 'all friends.',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/next',
        'message':'nextページ',
        'form':HelloForm(),
    }
    return render(request, 'hello/index.html', params)


def form(request):
    name = request.POST.get('name')
    params = {
        'title':name,
        'message':"post",
    }
    return render(request, 'hello/index.html', params)



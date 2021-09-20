from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView

# Create your views here.

class HelloView(TemplateView):
    def __init__(self) :
        self.params = {
        'title':'Hello/index',
        'message':'Indexページ',
        'form':HelloForm(),
    }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        age = request.POST.get('age')
        self.params['message']=f'名前：{name}<br> メール:{mail}<br> 年齢:{age}'
        self.params['form']=HelloForm(request.POST)
    
        return render(request, 'hello/index.html', self.params)



def index(request):
    params = {
        'title':'Hello/index',
        'message':'Indexページ',
        'form':HelloForm(),
    }
    
    if(request.method == 'POST'):
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        age = request.POST.get('age')
        params['message']=f'名前：{name}<br> メール:{mail}<br> 年齢:{age}'
        params['form']=HelloForm(request.POST)
    
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



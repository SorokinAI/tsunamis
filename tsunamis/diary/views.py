from django.shortcuts import render
from .models import Swimmer, Mark
from .forms import LoginForm
# Create your views here.


def signin(request):
    form = LoginForm()
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            pass
        else:
            error = 'Такого пловца нет'

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'diary/signin.html', data)

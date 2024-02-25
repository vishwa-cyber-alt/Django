

from django.shortcuts import render
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'display_form_data.html', {'name': name, 'email': email})
    else:
        form = MyForm()
    return render(request, 'my_form.html', {'form': form})

from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/new_list/')
    return render(request, 'list.html')


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/new_list/')

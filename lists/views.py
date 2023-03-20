from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/new_list/')
    items = Item.objects.all()
    return render(request, 'home.html', context={'items': items})


def view_list(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/new_list/')
    return render(request, 'list.html')

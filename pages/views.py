from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from pages.models import posts
from pages.forms import Post

def HomePageView(request):
    posts_list = posts.objects.all()
    data = { 'errors': [], 'successful': [], 'posts_list': posts_list, 'what_order': '', 'order_by': 'id' }
    
    if request.method == "POST":
        if 'what_order' in request.POST and 'order_by' in request.POST:
            data['what_order'] = request.POST.get('what_order')
            data['order_by'] = request.POST.get('order_by')
        data['posts_list'] = posts.objects.order_by(data['what_order'] + data['order_by'])
        if 'content' in request.POST:
            form = Post(request.POST)
            if form.is_valid():
                form.save()
                data['successful'].append('Элемент успешно добавлен в таблицу')
            else:
                data['errors'].append('Текст меньше пяти символов')
    return render(request, 'home.html', data)

def delete(request, id):
    post = get_object_or_404(posts, id=id).delete()
    return HttpResponseRedirect(reverse('home'))

def edit(request, id):
    post = get_object_or_404(posts, pk=id)
    data = { 'errors': [], 'successful': [], 'post': post, 'id': id }
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            data['post'] = form.editPost(id)
            if data['post'].content != post.content:
                data['successful'].append('Элемент успешно изменен')
            else:
                data['errors'].append('Ошибка сохранения: элемент уже сохранен')
        else:
            data['errors'].append('Ошибка сохранения: текст меньше пяти символов')
    return render(request, 'edit.html', data)

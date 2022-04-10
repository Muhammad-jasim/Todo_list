from django.http import HttpResponse
from django.shortcuts import redirect, render

from todolist_app.models import TodoList
from todolist_app.forms import TodoListForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        t = TodoListForm(request.POST)
        if t.is_valid():
            t.save()
            t_view = TodoList.objects.all()
            return redirect(home)
    else:
        t = TodoListForm()
        t_view = TodoList.objects.all()
        t_count = TodoList.objects.all().count()+1
        return render(request,'todolist.html',{'todo':t,'view':t_view,'order':t_count})

def drag(request,id):
    request.session['drag_id']=id
    return redirect(home)   

def drop(request,id):
    request.session['drop_id']=id
    return redirect('swap')

# drag and drop
def swap(request):
    drag = request.session['drag_id']
    drop = request.session['drop_id']
    drag_obj = TodoList.objects.get(item_id=drag)
    drop_obj = TodoList.objects.get(item_id=drop)
    
    a = drag_obj.item
    b = drop_obj.item

    drag_obj.item = b
    drop_obj.item = a
    drag_obj.save()
    drop_obj.save()
    return redirect('home')

# edit and update
def edit(request,id):
    t = TodoList.objects.get(item_id=id)
    t_view = TodoList.objects.filter(item_id=id)
    return render(request,'todolist_edit.html',{'edit':t,'view':t_view})

def update(request,id):
    item = request.POST['item']
    t = TodoList.objects.get(item_id=id)
    t.item = item
    t.save()
    return redirect('home')

# to delete item
def delete(request,id):
    t = TodoList.objects.get(item_id=id)
    t.delete()
    return redirect('home')
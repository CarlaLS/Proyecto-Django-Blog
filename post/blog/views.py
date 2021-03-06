
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, ActualizarForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    posts=Post.objects.all()
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado= True)
    paginator = Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page) 

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.autor= request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostForm   

    form=PostForm()

    if queryset:
        posts= Post.objects.filter(
           Q(titulo__icontains=queryset) |
           Q(subtitulo__icontains=queryset) 
           
        ).distinct()   
    contexto={
        'posts': posts,
        
    }
      
    return render(request, 'blog/index.html', contexto)



@login_required
def about(request):
    return  render(request, 'blog/about.html')
    
@login_required

def crear_post(request):

  posts=Post.objects.all()
  

  if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.autor= request.user
            instance.save()
            return redirect('blog-index')
  else:
        form = PostForm   

  form=PostForm()
  contexto={
        
        'form': form
    }
  
  return render(request, 'blog/crear_post.html', contexto)


   
@login_required
def detalle_post(request, pk):
    post= Post.objects.get(id=pk)
   


    if request.method == 'POST':
        c_form = ComentarioForm(request.POST)
        if c_form.is_valid():
           instance= c_form.save(commit =False)
           instance.usuario = request.user
           instance.post = post 
           instance.save()
           return redirect('detalle_post', pk=post.id)
    else:
        c_form = ComentarioForm()    

    



    contexto={
       'post': post,
       'c_form':c_form,
    }
    return render(request, 'blog/detalle_post.html', contexto) 
       

@login_required
def editar_post(request, pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        form = ActualizarForm(request.POST, instance=post)
        if form. is_valid():
            form.save()
            return redirect('detalle_post', pk=post.id)
    else:
        form = ActualizarForm(instance=post)    

    contexto={
         'post': post,
         'form': form,
    }
    return render(request, 'blog/editar_post.html', contexto)  

@login_required
def borrar_post(request, pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')

    contexto= {
        'post': post
    }
    return render (request, 'blog/borrar_post.html', contexto)

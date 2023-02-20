from django.shortcuts import render,redirect
import datetime
from kobita.models import *
from django.contrib import messages

def view_page(request,pk):

    post = Post.objects.all().get(id=pk)
    comment = Comment.objects.all().filter(post_comment_id=post.id).order_by('-id')
    my_date = datetime.datetime.now()
   
    post.view += 1
    post.save()

    if request.method=='POST':
        comment_take = Comment(request.POST)

        name = request.POST['name']
        body = request.POST['body']
        date = datetime.datetime.now()
        post_id = request.POST['post_id']

        object = Comment(name=name,body=body,post_comment_id=post_id,created_at=date)
        object.save()
        messages.success(request,"Comment Successfull")
        return redirect('/post/'+str(post_id)+'/')
    else:
        comment_take = Comment()


    context ={
        'post':post,
        'comment':comment,
        'my_date': my_date
    }
    return render(request,'view.html',context)


def IP(request):
    get_ip = request.META.get("HTTP_X_FORWARDED_FOR")

    if get_ip is not None:
        ip = get_ip.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def home(request):

    my_date = datetime.datetime.now()
    myip = IP(request)
    data = Post.objects.all().order_by('-view')[:3]
    data2 = Post.objects.all().order_by('-id')[:100]
    if request.method=='POST':
        data3 = subscription(request.POST)
        mail = request.POST["email"]
        ip = request.POST["ip"]
        object = subscription(email=mail,ip=ip)
        already_has = subscription.objects.all().filter(email=mail).exists()
        if already_has:
            messages.warning(request,"Sorry, already subscribed")
        else:
            object.save()
            messages.success(request,"Subscription Done")
            return redirect('Home')
    else:
        data3 = subscription()

    context = {
        'my_date':my_date,
        'data':data,
        'data2':data2,
        'myip':myip
    }
    return render(request,'index.html',context)
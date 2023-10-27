from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import reset_password_token
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    webdevelopment=Category.objects.get(name="Web Development")
    onlinemarketing=Category.objects.get(name="Online Marketing")
    videoediting=Category.objects.get(name="Video Editing")
    graphicdesign=Category.objects.get(name="Graphic Design")
    webdevelopmentcourse=Course.objects.filter(category=webdevelopment).count()
    onlinemarketingcourse=Course.objects.filter(category=onlinemarketing).count()
    videoeditingcourse=Course.objects.filter(category=videoediting).count()
    graphicdesigncourse=Course.objects.filter(category=graphicdesign).count()

    
    context={
        'webdevelopment':webdevelopment,
        'onlinemarketing':onlinemarketing,
        'videoediting':videoediting,
        'graphicdesign':graphicdesign,
        'webdevelopmentcourse':webdevelopmentcourse,
        'onlinemarketingcourse':onlinemarketingcourse,
        'videoeditingcourse':videoeditingcourse,
        'graphicdesigncourse':graphicdesigncourse
    }
    return render(request, 'index.html', context)

def error_404(request, exception):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        contactinfo=Contact.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
            message=message,
        )
        contactinfo.save()
        messages.success(request, "Thank you for sending message")
    return render(request, 'contact.html')

def courses(request):
    webdevelopment=Category.objects.get(name="Web Development")
    onlinemarketing=Category.objects.get(name="Online Marketing")
    videoediting=Category.objects.get(name="Video Editing")
    graphicdesign=Category.objects.get(name="Graphic Design")
    webdevelopmentcourse=Course.objects.filter(category=webdevelopment).count()
    onlinemarketingcourse=Course.objects.filter(category=onlinemarketing).count()
    videoeditingcourse=Course.objects.filter(category=videoediting).count()
    graphicdesigncourse=Course.objects.filter(category=graphicdesign).count()

    
    context={
        'webdevelopment':webdevelopment,
        'onlinemarketing':onlinemarketing,
        'videoediting':videoediting,
        'graphicdesign':graphicdesign,
        'webdevelopmentcourse':webdevelopmentcourse,
        'onlinemarketingcourse':onlinemarketingcourse,
        'videoeditingcourse':videoeditingcourse,
        'graphicdesigncourse':graphicdesigncourse
    }
    return render(request, 'courses.html', context)

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def course_detail(request, name):
    category=Category.objects.get(name=name)
    courses=Course.objects.filter(category=category)
    context={
        'courses':courses,
        'category':category.name
    }
    return render(request, "course-detail.html", context)

def videos(request, pk):
    if request.user.is_anonymous:
        a="no"
        course=Course.objects.get(pk=pk)
        lecture=Lecture.objects.filter(course=course)
    else:
        a="no"
        course=Course.objects.get(pk=pk)
        lecture=Lecture.objects.filter(course=course)
        mycourses=MyCourses.objects.filter(user=request.user)
        for i in mycourses:
            if i.name == course.name:
                a="yes"
    context = {
        'lectures':lecture,
        'course':course,
        'a':a
    }
    return render(request, "videos.html", context)

def billinginfo(request,pk):
    course=Course.objects.get(pk=pk)
    if request.user.is_anonymous:
        mycourse=None
    else:
        try:
            mycourse=MyCourses.objects.get(name=course.name, user=request.user)
        except MyCourses.DoesNotExist:
            mycourse=None
        
    context={
        'course':course,
        'mycourse':mycourse
    }
    return render(request, "billingifo.html", context)

def mycourses(request):   
    my_courses=MyCourses.objects.filter(user=request.user)
    context={
        'mycourses':my_courses
    }
    
    return render(request, 'mycourses.html', context)

def enroll(request,pk):
    course=Course.objects.get(pk=pk)
    mycourse=MyCourses.objects.create(
        user=request.user,
        name=course.name,
        category=course.category,
        image=course.image,
        courseid=pk,
    )
    mycourse.save()
    return redirect('mycourses')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'account do not exists please register to login')
    return render(request, 'login.html')

def registration_page(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.warning(request, "username alredy exists try new username!!")
            return redirect('registration')

        if User.objects.filter(email=email):
            messages.warning(request, "email alredy exists please try the another email!!")
            return redirect('registration')

        if password1 == password2:
            User.objects.create_user(
                username=username,
                first_name = fullname,
                email=email,
                password=password1
            )
            return redirect('login')
        else:
            messages.warning(request, "password doesn't match")
            return redirect('registration')
    return render(request, 'registration.html')


def logout_user(request):
    logout(request)
    messages.success(request, f' you are logout !!')
    return redirect('login')

def change_password(request, pk):
    if request.method == 'POST':
        newpassword1=request.POST["newpassword1"]
        newpassword2=request.POST["newpassword2"]
        user = User.objects.get(pk=pk)
        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request, "your password has been change now you can login!!")
            return redirect('login')
        else:
            messages.warning(request, "password doesn't match")
    context={
        'id':pk
    }
    return render(request, "change_password.html", context)

def reset_password(request):
    if request.method == 'POST':
        email=request.POST['email']
        
        if User.objects.filter(email=email):
            user=User.objects.get(email=email)
            subject = 'Reset Password link'
            message =render_to_string('forget_password_email.html', {  
                'user': user,  
                'domain': get_current_site(request).domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':reset_password_token.make_token(user),  
            })  
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email ]
            send_mail( subject, message, email_from, recipient_list )
            
            messages.success(request,"please check the email to change the password!!")
            return redirect('login')
        else:
            messages.warning(request, "This email is not register please register at first!!")
    return render(request, 'forgetyourpassword.html')



def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and reset_password_token.check_token(user, token): 
        return redirect("change_password", pk=user.id) 
    else:
        messages.warning(request,"invalid link")
        return redirect("reset_password")

from django.shortcuts import render
from django.template import RequestContext
from .models import userdata, maidata, review, message
from .forms import Orderform, Maidform, Reviewform, Messageform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

@login_required
def user(request):
    emails = userdata.objects.order_by('date_added')
    user = request.user.email
    template = 'ordermaid.html'
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phoneno = form.cleaned_data['phone_number']
            type1 = form.cleaned_data['worktype']
            subject = 'IDEALTECH: NEW REQUEST'
            message = """
            Hi there, We have a new request!
            Here are the details!
            %s
            %s
            %s %s
            """ % (name, address, phoneno, type1)
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True,)
            confirm_message = "Thank you for your order!"
            context = {'confirm_message':confirm_message}
            template = 'thankyou.html'
            return render(request,template,context)
    else:
        if not emails:
            form = Orderform(initial={'email':user, 'city':'Pune', 'zipcode':'411019'})
            context = {'form':form}
            return render(request,template,context)
        else:
            for email1 in emails:
                if user == email1.email:
                    form = Orderform(initial={'name':email1.name,'email': user, 'phone_number': email1.phone_number, 'address': email1.address, 'city': 'Pune', 'zipcode': '411019'})
                    context = {'form':form}
                    return render(request,template,context)
                    break
                else:
                    form = Orderform(initial={'email':user, 'city':'Pune', 'zipcode':'411019'})
                    context = {'form':form}
                    return render(request,template,context)

@login_required
def maidstat(request):
    orders = userdata.objects.order_by('-date_added')
    context = {'orders': orders}
    template = 'maidstat.html'
    return render(request,template,context)
@login_required
def yourorders(request):
    orders = review.objects.order_by('-date_added')
    context = {'orders': orders}
    template = 'yourorders.html'
    return render(request,template,context)

def maiddata(request):
    template = 'maidlogin.html'
    if request.method != 'POST':
        form = Maidform()
        context = {'form':form}
        return render(request,template,context)
    else:
        form = Maidform(request.POST)
        if form.is_valid():
            form.save()
            template = 'home.html'
            context = {}
            return render(request,template,context)

def maid(request):
    maids = maidata.objects.order_by('-date_added')
    context = {'maids': maids}
    template = 'maiddata.html'
    return render(request,template,context)
@login_required
def reviewmaid(request):
    codes = maidata.objects.order_by('-date_added')
    if request.method != 'POST':
        template = 'review.html'
        form = Reviewform(initial={'email':request.user.email})
        context = {'form':form}
        return render(request,template,context)
    else:
        form = Reviewform(request.POST)
        if form.is_valid():
            data = form.cleaned_data['code']
            for i in range(0, len(codes)):
                if codes[i].maidid == data:
                    form.save()
                    name = form.cleaned_data['name']
                    review = form.cleaned_data['review']
                    code1 = codes[i].maidid
                    subject = 'IDEALTECH: NEW REVIEW'
                    message = """
                    Hi there, Someone just added a review!
                    Here are the details!
                    Name: %s
                    Review Message: %s
                    Maid ID: %s
                    """ % (name, review, code1)
                    emailFrom = form.cleaned_data['email']
                    emailTo = [settings.EMAIL_HOST_USER]
                    send_mail(subject, message, emailFrom, emailTo, fail_silently=True,)
                    template = 'home.html'
                    context = {}
                    return render(request,template,context)
                else:
                    message = 'Seems like the Maid ID you entered is incorrect! Please cross-check with your maid.'
                    context = {'message':message}
                    template = 'review.html'
                    return render(request,template,context)
@login_required
def message(request):
    template = 'message.html'
    if request.method != 'POST':
        form = Messageform(initial={'email':request.user.email})
        context = {'form':form}
        return render(request,template,context)
    else:
        form = Messageform(request.POST)
        if form.is_valid():
            form.save()
            template = 'thankyou.html'
            message1 = "Thank you for your time. We have got your message, we will get back to you asap!"
            context = {'message1':message1}
            return render(request,template,context)

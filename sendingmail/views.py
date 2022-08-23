from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from bulkmail.settings import EMAIL_HOST_USER
from django.contrib import messages

def EmailSend(request):
    if request.method=='POST':
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        html=request.POST.get('html')
        msg=EmailMultiAlternatives(f'{subject}',f'{content}',EMAIL_HOST_USER,[f'{email}'])
        msg.attach_alternative(html,"text/html")
        msg.send()
        messages.success(request,'Sucess')
        return render(request,'htmlpages/check.html')
    return render(request,'htmlpages/sendmail.html')
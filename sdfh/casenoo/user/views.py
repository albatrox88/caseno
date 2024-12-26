from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.conf import settings
from .models import UserVerification
from django.contrib.auth import get_user_model
  
#################### index####################################### 
def index(request):
    return render(request, 'user/index.html', {'title':'Juwa tash'})
  
########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
################ login forms################################################### 
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Render email template
            html_message = render_to_string('user/Email.html', {'username': username})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = email

            # Send email
            send_mail(
                'Thank you for registering',
                plain_message,
                from_email,
                [to],
                html_message=html_message,
            )

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def delete_account_request(request):
    if request.method == 'POST':
        verification_code = get_random_string(length=6)
        UserVerification.objects.create(user=request.user, code=verification_code)
        send_mail(
            'Delete Account Verification Code',
            f'Your verification code is {verification_code}',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
        )
        return redirect('verify_delete_account')
    return render(request, 'user/delete_account_request.html')

# View to handle verification code and delete the account
@login_required
def verify_delete_account(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        verification = UserVerification.objects.filter(user=request.user, code=code).first()
        if verification:
            user = request.user
            user.delete()
            return redirect('account_deleted')
    return render(request, 'user/verify_delete_account.html')

# View to show account deleted confirmation
def account_deleted(request):
    return render(request, 'user/account_deleted.html')
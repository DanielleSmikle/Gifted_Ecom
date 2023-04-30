from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import RegistrationForm
from django.shortcuts import redirect
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import UserBase
from .forms import RegistrationForm


@login_required
def dashboard(request):
    return render(request, 
                  'account/user/dashboard.html')

def account_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email_address = registerForm.cleaned_data['email_address']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # email_address setup
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email_address.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_address(subject=subject, message=message)
            return HttpResponse('registered successfully and activiation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form':registerForm })

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
  
    

    


    

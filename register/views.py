from django.shortcuts import render, HttpResponse
from register.form import Registration_form, login_form
from register.models import Register
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.


def index(request):
    return HttpResponse('Welcome')


def success_message(request):
    return render(request, 'html/Message Card/success.html')


def failed_message(request):
    return render(request, 'html/Message Card/failed.html')


def user_detail(request, user_slug):
    try:
        print(user_slug)
        find_slug = Register.objects.get(slug=user_slug)
        print(find_slug.first_name)
        return render(request, 'html/profile/profile.html', {
            'found': True,
            'user_detail': find_slug,
        })
    except:
        return render(request, 'html/profile/profile.html', {
            'found': False,
        })


def login_user(request):
    slug_name = "m"
    print(request.method)
    if(request.method == 'POST'):
        form = login_form(request.POST)
        if(form.is_valid()):
            try:
                u_name = form.cleaned_data.get('user_name')
                u_password = form.cleaned_data.get('password')
                user = Register.objects.get(user_name=u_name)
                if(user.user_name == u_name and user.password == u_password):
                    return redirect('profile', user_slug=user.slug)
                else:
                    return render(request, 'html/login.html', {
                        'try': True,
                        'form': form,
                    })
            except:
                return render(request, 'html/login.html', {
                    'try': True,
                    'form': form,
                })
    else:
        form = login_form()
        return render(request, 'html/login.html', {
            'try': False,
            'form': form,
        })


def Register_user(request):
    print('okk')
    print(request.method)
    if(request.method == 'POST'):
        forms = Registration_form(request.POST)
        print(forms.is_valid())
        if(forms.is_valid()):
            try:
                u_name = forms.cleaned_data.get('user_name')
                f_name = forms.cleaned_data.get('first_name')
                l_name = forms.cleaned_data.get('last_name')
                mail = forms.cleaned_data.get('email')
                passwd = forms.cleaned_data.get('password')
                user = Register.objects.create(
                    first_name=f_name, user_name=u_name, last_name=l_name, email=mail, password=passwd)
                user.save()
                return redirect('success_message')
            except:
                return redirect('failed_message')
    else:
        forms = Registration_form
    return render(request, 'html/registration.html', {
        'form': forms,
    })

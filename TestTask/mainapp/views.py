from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from .serv import change_user_info
from django.contrib.auth.views import LoginView


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user_cat = UserProfile.objects.get(user_id=request.user.pk)

        context = {'cat': user_cat.cat_user_id}
        return render(request, 'mainapp/index.html', context)
    return render(request, 'mainapp/index.html')


def register_user(request):
    user_form = RegisterUserFrom()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = RegisterUserFrom(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user_id = user.id
            profile_form.save()
            return redirect(reverse_lazy('login'))
    context = {'user_form': user_form, 'profile_form': profile_form, 'title': 'Регистрация'}
    return render(request, 'mainapp/registration.html', context)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect('index')


def profile_employer(request):
    user_info = User.objects.get(pk=request.user.pk)
    user_profile = UserProfile.objects.get(user_id=request.user.pk)
    change_user_form = ChangeUserInfoForm()
    change_profile_form = ChangeUserProfileForm()
    change_user_info(request)
    context = {'user_info': user_info, 'user_profile': user_profile, 'title': 'Профиль',
               'change_user_form': change_user_form, 'change_profile_form': change_profile_form}
    return render(request, 'mainapp/profile_employer.html', context)


def profile_worker(request):
    user_info = User.objects.get(pk=request.user.pk)
    user_profile = UserProfile.objects.get(user_id=request.user.pk)
    user_exp = Experience.objects.filter(user_id=request.user.pk)
    change_user_form = ChangeUserInfoForm()
    change_profile_form = ChangeUserProfileForm()
    change_user_info(request)
    context = {'user_info': user_info, 'user_profile': user_profile, 'title': 'Профиль', 'user_exp': user_exp,
               'change_user_form': change_user_form, 'change_profile_form': change_profile_form, }
    return render(request, 'mainapp/profile_worker.html', context)


def exp_add(request):
    user_exp_form = ExperienceForm()
    if request.method == 'POST':
        user_exp_form = ExperienceForm(request.POST, )
        if user_exp_form.is_valid():
            user = request.user.pk
            exp = user_exp_form.save(commit=False)
            exp.user_id = user
            user_exp_form.save()
    context = {'user_exp_form': user_exp_form, 'title': 'Опыт работы'}
    return render(request, 'mainapp/exp_add.html', context)


def delete_exp(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        Experience.objects.filter(id=record_id).delete()
    return redirect('profile_worker')

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserOurRegistration
from .forms import ProfileImage
from .forms import UserUpdateForm


# Create your views here.
def register(request):
    if request.method == "POST":  # если была нажата кнопка отправки формы
        form = UserOurRegistration(request.POST)
        if form.is_valid():  # если форма была заполненна и удовлетворяет условиям
            form.save()  # сохранение пользователя
            username = form.cleaned_data.get("username")
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('auth')
    else:  # когда просто перешли на страницу регистрации
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация'})


@login_required  # декоратор для проверки авторизованности пользователя, если пользователь не авторизован переходить на страницу не будет
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'title': 'Личный кабинет',
        'img_profile': img_profile,
        'update_user': update_user,
    }
    return render(request, 'users/profile.html', data)

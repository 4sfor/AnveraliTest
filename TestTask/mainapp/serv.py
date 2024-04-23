from .forms import *
from .models import *


def change_user_info(request):
    user_instance = User.objects.get(pk=request.user.pk)
    profile_instance = UserProfile.objects.get(user_id=request.user.pk)
    if request.method == 'POST':
        user_form = ChangeUserInfoForm(request.POST, instance=user_instance)
        profile_form = ChangeUserProfileForm(request.POST, request.FILES, instance=profile_instance)

        if user_form.is_valid() and profile_form.is_valid():
            user_fields = {key: value for key, value in user_form.cleaned_data.items() if value}

            if user_fields:
                User.objects.filter(pk=request.user.pk).update(**user_fields)
            profile_form.save()



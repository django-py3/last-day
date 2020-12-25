from .models import RegularUser

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegularUserCreationForm(UserCreationForm):
    """
    Наш интерфейс взаимодействия с нашей CustomUser моделью
    Создание юзера
    """
    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = UserCreationForm.Meta.fields + ('age','phone_number','postal_code','sex',) 
        # При создании пользователя еще хотим указывать и возраст

class RegularUserChangeForm(UserChangeForm):
    """
    Наш интерфейс взаимодействия с нашей CustomUser моделью
    Редактирование юзера
    """
    class Meta(UserChangeForm.Meta):
        model = RegularUser
        fields = UserChangeForm.Meta.fields 
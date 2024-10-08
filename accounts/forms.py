from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from crispy_tailwind.layout import Submit

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class BlueSubmit(Submit):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('css_class', 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer')
        super().__init__(*args, **kwargs)


class RedSubmit(Submit):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('css_class', 'bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded cursor-pointer')
        super().__init__(*args, **kwargs)


class PurpleSubmit(Submit):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('css_class', 'bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded cursor-pointer')
        super().__init__(*args, **kwargs)


class SignupForm(UserCreationForm):
    helper = FormHelper()
    helper.attrs = {"novalidate": True}        # form 태그에 추가할 속성
    helper.layout = Layout(
        "username",
        Row(
            Field("password1", wrapper_class="w-1/2"),
            Field("password2", wrapper_class="w-1/2"),
            css_class="flex flex-row gap-2"
        )
    )
    helper.add_input(
        PurpleSubmit("submit", "회원가입"),
    )

    class Meta(UserCreationForm.Meta):
        model = User


class LoginForm(AuthenticationForm):
    helper = FormHelper()
    helper.attrs = {"novalidate": True}        # form 태그에 추가할 속성

    # 원하는 Row/Column 배치로 레이아웃을 구성 지원
    helper.layout = Layout(
        Row("username", "password", css_class="flex flex-row gap-2")
    )

    helper.add_input(
        PurpleSubmit("submit", "로그인"),
    )

from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.forms import LoginForm


class LoginView(DjangoLoginView):
    form_class = LoginForm  # 로그인 폼 필드 커스텀할려면 !!!
    template_name = "_crispy_form.html"

    # 로그인 후에 이동할 주소에 대한 allowed host list
    # 같은 호스트라면 등록할 필요는 없습니다.
    success_url_allowed_hosts = ["localhost:3000"]
    # 아래와 같이 새 settings 설정 사용을 권장
    # success_url_allowed_hosts = settings.FRONT_HOST


login = LoginView.as_view()


class LogoutView(DjangoLogoutView):
    next_page = "accounts:login"
    success_url_allowed_hosts = ["localhost:3000"]
    # 아래와 같이 새 settings 설정 사용을 권장
    # success_url_allowed_hosts = settings.FRONT_HOST

logout = LogoutView.as_view()


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

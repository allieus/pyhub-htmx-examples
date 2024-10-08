from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from crispy_tailwind.layout import Submit

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator


class DemoForm(forms.Form):
    author = forms.CharField(label="작성자")
    instagram_username = forms.CharField(label="인스타그램 아이디")
    title = forms.CharField(label="제목")
    summary = forms.CharField(
        label="요약",
        help_text="본문에 대한 요약을 최소 20자, 최대 200자 내로 입력해주세요.",
        validators=[MinLengthValidator(20), MaxLengthValidator(200)],
    )
    content = forms.CharField(widget=forms.Textarea, label="내용")
    content_en = forms.CharField(widget=forms.Textarea, label="내용(영문)")

    # 폼에 파일/이미지 필드가 있다면, enctype="multipart/form-data"가 자동 추가됩니다.
    helper = FormHelper()
    helper.attrs = {"novalidate": True}        # form 태그에 추가할 속성

    # 원하는 Row/Column 배치로 레이아웃을 구성 지원
    helper.layout = Layout(
        "title",  # crispy-bootstrap5 지원, 커스텀 필드
        "summary",
        "content",
        "content_en",
        # 1행 2열 레이아웃
        Row(
            # 기본 위젯 렌더링 + 추가 속성 지정 + 래핑 클래스 지정
            Field("author", autocomplete="off", wrapper_class="w-1/2"),
            # Bootstrap 지원 필드 + 래핑 클래스 지정
            PrependedText("instagram_username", "@", wrapper_class="w-1/2"),
            css_class="flex flex-row gap-4",
        ),
    )

    helper.add_input(Submit("submit", "제출"))  # submit 버튼 추가

    def clean(self):
        summary = self.cleaned_data.get("summary")
        content = self.cleaned_data.get("content")

        if content and not summary:
            raise forms.ValidationError("본문에 대한 요약을 입력해주세요.")

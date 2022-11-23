from django import forms
from django.forms import ModelForm, Textarea
from .models import Feedback
from services.models import ServiceDetail, ServicePage
from yard.models import Service


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, required=False)
    email = forms.EmailField(label='Емейл', max_length=50, required=False)
    phone = forms.CharField(label='Телефон', max_length=50, required=True)
    massage = forms.CharField(label='Сообщение', max_length=500, widget=forms.Textarea, required=False)


# class AboutForm(ModelForm):
#
#     class Meta:
#         model = About
#         fields = '__all__'
#         widgets = {
#             'text': Textarea(attrs={'cols': 160,
#                                     'rows': 20})
#         }


class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class ServicePageForm(ModelForm):

    class Meta:
        model = ServicePage
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
            'bottom_text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class ServiceDetailForm(ModelForm):

    class Meta:
        model = ServiceDetail
        fields = '__all__'
        widgets = {
            'text_1': Textarea(attrs={'cols': 160,
                                    'rows': 20}),
            'text_2': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


# class GalleryPageForm(ModelForm):
#
#     class Meta:
#         model = GalleryPage
#         fields = '__all__'
#         widgets = {
#             'bottom_text': Textarea(attrs={'cols': 160,
#                                     'rows': 20}),
#         }
#
#
# class ProjectPageForm(ModelForm):
#
#     class Meta:
#         model = ProjectPage
#         fields = '__all__'
#         widgets = {
#             'bottom_text': Textarea(attrs={'cols': 160,
#                                     'rows': 20}),
#         }
#
#
# class ProjectDetailForm(ModelForm):
#
#     class Meta:
#         model = ProjectDetail
#         fields = '__all__'
#         widgets = {
#             'article_text': Textarea(attrs={'cols': 160,
#                                     'rows': 20}),
#         }
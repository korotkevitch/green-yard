from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Service, Testimonial, Project, Sphere, Feedback
from services.models import ServiceDetail
from .forms import UserForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


class IndexView(ListView):
    context_object_name = 'index'
    template_name = 'index.html'
    queryset = Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['testimonial_list'] = Testimonial.objects.all()
        context['project_list'] = Project.objects.all()
        context['sphere_list'] = Sphere.objects.all()
        context['all_services'] = ServiceDetail.objects.all()
        return context


####### Данные из формы отправляются на емейл и в БД (админку) ########

def feedback(request):
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    massage = request.POST.get('massage', '')
    if name and phone and massage:
        try:
            send_mail('Сообщение с сайта green-yard.by',
                      str('Имя:' + ' ' + name + '\n' + 'Телефон:' + ' ' + phone + '\n' + '\n' + 'Сообщение:' + ' ' + massage),
                      'no-reply@green-yard.by',
                      ['info@iko-studio.com'])

            f = Feedback(name=name, phone=phone, massage=massage)  # Данные сохраняются в БД (админке)
            f.save()

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'thanks.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'thanks.html')

####### Данные из формы сохраняются только в БД (админке) ########
# def feedback(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             massage = form.cleaned_data['massage']
#
#             f = Feedback(name=name, email=email, phone=phone, massage=massage)
#
#             f.save()
#         return render(request, 'thanks.html')
#
#     else:
#         form = UserForm()
#     return render(request, 'thanks.html', {'form': form,})


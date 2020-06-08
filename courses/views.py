import time

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import DetailView
from cloudipsp import Api
from cloudipsp import Checkout

from .models import Course
from .models import Lesson
from .forms import CourseForm


# Create your views here.
class HomePage(ListView):
    """Class for displaying Course data base in the html page.

    model - data base that used in the class. (Course)

    template_name - name of html template that would be refer to the class.

    context_object_name - name that would be used for get a fields from the database.

    ordering - sorting by field for displaying database's items. By id there.
    """
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Add extra parameter "title" with database.
        """
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница сайта'
        return context


class CourseDetailPage(DetailView):
    """Class for detail displaying every item from Course data base in the html page.

    model - data base that used in the class. (Course)

    template_name - name of html template that would be refer to the class.

    """
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Adds extra parameters "title" and "lessons" from Lesson database,
        that connect with defined course with Course database.

        Lessons would be sorted by their numbers. (Sends as a list)

        Lesson.objects.filter(course=context['title'])
            course - field in Lesson table
            context['title'] - with what we compare
        """
        context = super(CourseDetailPage, self).get_context_data(**kwargs)
        context['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        context['lessons'] = Lesson.objects.filter(course=context['title']).order_by('number')
        return context


class LessonDetailPage(DetailView):
    """Class for detail displaying every item from Lesson database through Course database in the html page.

    model - data base that used in the class. (Course)

    template_name - name of html template that would be refer to the class.

    """
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Adds extra parameters "title", "description" and "video_url" from Lesson database,
        that connect with defined course with Course database.

        From "video_url" we take only video's id.
        """
        context = super(LessonDetailPage, self).get_context_data(**kwargs)

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        context['title'] = lesson[0]['title']
        context['description'] = lesson[0]['description']
        context['video'] = lesson[0]['video_url'].split("=")[1]
        return context


def create_course(request):
    """
    Function for display CourseForm Course table, and create new item in Course table,
    if data would be sent and form valid.
    """
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            course = form.cleaned_data.get('title')
            messages.success(request, f"Курс {course} был успешно добавлен")
            return redirect('home')
        else:
            messages.error(request, "Ошибка добавления курса")
    else:
        form = CourseForm()
    data = {
        'title': 'Новый курс',
        'form': form,
     }
    return render(request, 'courses/course-form.html', data)


def tarrifs_page(request):
    """For tarrifs.html page. Connect to FONDY."""
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": 150000,
        "order_desc": "Покупка подписки на сайте",
        "order_id": str(time.time())
    }
    url = checkout.url(data).get('checkout_url')
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы на сайте', 'url': url})

import requests
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from apps.main.models import FormWholesalerForm, OurBlog, AboutUs

from constance import config

from apps.products.models import Category, Product

import operator

from core.sms_service import sms_to_phone


class BlogPage(ListView):
    template_name = 'blog/blog_list.html'
    model = OurBlog
    context_object_name = 'blogs'
    paginate_by = 2


class HomePage(ListView):
    """Рендер главной страницы сайта"""

    template_name = 'home/index.html'
    model = OurBlog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = dict(Category.objects.all().values_list('id', 'name'))
        context['config'] = config
        context['B1_CAT_NAME'] = categories[config.B1_CAT_ID] if config.B1_CAT_ID in categories else 'Test'
        context['B2_CAT_NAME'] = categories[config.B2_CAT_ID] if config.B2_CAT_ID in categories else 'Test'
        context['B3_CAT_NAME'] = categories[config.B3_CAT_ID] if config.B3_CAT_ID in categories else 'Test'
        context['B4_CAT_NAME'] = categories[config.B4_CAT_ID] if config.B4_CAT_ID in categories else 'Test'
        context['B5_CAT_NAME'] = categories[config.B5_CAT_ID] if config.B5_CAT_ID in categories else 'Test'
        context['B6_CAT_NAME'] = categories[config.B6_CAT_ID] if config.B6_CAT_ID in categories else 'Test'
        context['popular_products'] = Product.objects.filter(is_popular=True)
        return context


class BlogDetail(DetailView):
    """ страница блога """
    template_name = 'blog/blog_detail.html'
    model = OurBlog
    context_object_name = 'blog'
    pk_url_kwarg = 'id'

class AboutUsDetail(DetailView):
    template_name = 'about_us/about_us_detail.html'
    model = AboutUs
    context_object_name = 'about_us'

    def get_object(self, queryset=None):
        return AboutUs.objects.first()


def wholesaler_page(request):
    if request.method == "POST":
        form = FormWholesalerForm(
            request.POST, request.FILES
        )
        if form.is_valid():
            form.save()
        messages.error(request, 'Ваш запрос был отправлен , в скором времени с вами свяжется наш менеджер .',
                       extra_tags='success')
        sms_to_phone(message='')

    else:
        form = FormWholesalerForm()

    return render(request, 'wholesaler/index.html', {'form': form})


#
# def get_eskiz_token():
#     headers = {}
#     files = {}
#     url = 'https://notify.eskiz.uz/api/auth/login'
#     payload = {'email': 'custompcgaming1@gmail.com',
#                'password': '5kxq5WOjtQp4PGf53IbO1QejyuQD8fUJ5LtLM1qF'}
#     response = requests.request("POST", url, headers=headers, data=payload, files=files)
#     print(response)
#     print(response.json())
#
#
# get_eskiz_token()


def handler404(request, exception):
    context = {}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response

# def handler500(request):
#     context = {}
#     response = render(request, "pages/errors/500.html", context=context)
#     response.status_code = 500
#     return response

from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
import requests
from django.urls import reverse
import re  # Importing re module


class OurBlog(models.Model):
    """ Модель страницы нашего блога """

    img = models.ImageField("Изображение", upload_to='images/blog/', blank=False, null=False)
    title = models.CharField("тема", max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, db_index=True)
    short_description = models.TextField("Краткое описание", blank=False, null=False)
    full_description = models.TextField("Полное описание", blank=False, null=False)
    created_at = models.DateTimeField('Дата и время создания публикации', auto_now=True)
    seo_keyword = models.CharField(max_length=255)

    class Meta:
        db_table = 'our_blog'
        verbose_name = 'создать блог'
        verbose_name_plural = 'создавать блоги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})


class FormWholesaler(models.Model):
    """Таблица формы заполнения оптовикам"""

    class BusinessType(models.TextChoices):
        """Тип бизнеса"""

        myself = ('Для себя', 'Для себя')
        sale = ('Продажа', 'Продажа')
        other = ('Другое', 'Другое')

    name = models.CharField('Имя', max_length=30)
    phone = models.CharField('Номер телефона', max_length=15, blank=True)
    email = models.EmailField('Email', max_length=30, blank=True)
    company_name = models.CharField('Название компании', max_length=50, blank=True)
    social_network = models.CharField('Вебсайт/Instagram', max_length=50, blank=True)
    city = models.CharField('Город', max_length=50, blank=True)
    document = models.FileField('Сертификат/Диплом', upload_to='files/documents',
                                help_text='Документ для ускорения модерации', blank=True)
    business_type = models.CharField('Тип бизнеса', choices=BusinessType.choices, default=BusinessType.other,
                                     max_length=50)
    comment = models.TextField('Комментарий/Вопросы', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'forms_wholesalers'
        verbose_name = 'Заявка от оптовика'
        verbose_name_plural = 'Заявки от оптовиков'

    def __str__(self):
        return self.name


class FormWholesalerForm(forms.ModelForm):
    class Meta:
        model = FormWholesaler
        fields = '__all__'


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class AboutUs(SingletonModel):
    title = models.CharField(max_length=60)
    description = RichTextUploadingField('Описание')
    keyword = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/aboutus/')
    seo_keyword = models.CharField(max_length=255)

    class Meta:
        db_table = 'about_us'
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


def phone_number_validation(number):
    if re.fullmatch('998[0-9]{2}[0-9]{7}', number):
        return number
    else:
        raise ValidationError("Введенный номер телефона недействителен. Пожалуйста, введите номер телефона без +")


class Settings(SingletonModel):
    token = models.TextField(blank=True, null=True)
    admin_phone = models.CharField("Введите номер без +", max_length=12, null=True,
                                   validators=[phone_number_validation, ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'
        db_table = 'settings'

#
# def get_currency_from_api():
#     url = "https://api.apilayer.com/currency_data/convert?to=UZS&from=USD&amount=1"
#     headers = {
#         "apikey": "QaUnY2d2pSmIAvjRtbEl4eQNjiebDbLq"
#     }
#     response = requests.request("GET", url, headers=headers, data={})
#     resp = response.json()
#     print(resp)
#     return resp.get('result', 0)
#
# #
# # print(get_currency_from_api())
# # print(datetime.datetime.now())

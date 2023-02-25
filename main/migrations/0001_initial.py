# Generated by Django 4.1.7 on 2023-02-21 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Дайте название изображению чтобы легче его найти')),
                ('image', models.ImageField(blank=True, null=True, upload_to='shared/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Общие изображения',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IndexPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_bg', models.ImageField(blank=True, upload_to='index', verbose_name='Фоновое изображение')),
                ('hours_text', models.CharField(max_length=22, verbose_name='Часы работы')),
                ('out_text', models.CharField(max_length=22, verbose_name='Выезд на дом')),
                ('recommend_p1', models.TextField(verbose_name='Параграф 1-й')),
                ('recommend_p2', models.TextField(verbose_name='Параграф 2-й')),
                ('contact_bg', models.ImageField(blank=True, upload_to='index', verbose_name='Фоновое изображение контактов')),
                ('inst_name', models.CharField(blank=True, max_length=30, verbose_name='Название Инстаграма')),
                ('inst_url', models.URLField(blank=True, verbose_name='Ссылка на Инстаграм')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('whatsapp', models.CharField(blank=True, max_length=20, verbose_name='Телефон Whatsapp')),
                ('hire_phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон отдела кадров')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Найстройку главной страницы',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='PartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partners/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServiceGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Группа для услуг',
                'verbose_name_plural': 'Группы для услуг',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимальная длина 12 символов', max_length=30, verbose_name='Заголовок вакансии')),
                ('text', models.TextField(max_length=60, verbose_name='Краткое описание')),
                ('wage', models.SmallIntegerField(default=0, verbose_name='Зарплата')),
                ('details', models.TextField(blank=True, max_length=300, verbose_name='Подробное описание')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.SmallIntegerField(verbose_name='Стоимость')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.servicegroupmodel', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': 'Услуги',
                'ordering': ['group'],
            },
        ),
        migrations.CreateModel(
            name='SaleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Максимальная длина 12 символов', max_length=12, verbose_name='Заголовок акции')),
                ('text', models.TextField(max_length=60, verbose_name='Краткое описание')),
                ('details', models.TextField(blank=True, max_length=300, verbose_name='Подробное описание')),
                ('date_end', models.DateField(blank=True, verbose_name='Дата окончания')),
                ('delete_when_end', models.BooleanField(default=False, verbose_name='Удалить по окончанию')),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='main.imagesmodel', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
                'ordering': ['id'],
            },
        ),
    ]

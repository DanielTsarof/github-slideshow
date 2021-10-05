from django.db import models

# Create your models here.

# Атрибуты модели представляют соответсвующие поля в БД

class News(models.Model):     # Класс модели наследуется от класса models
    # описываем атрибуты
    # id - не создаем, т.к. это первичный ключ, он будет создан автоматически, если не указан
    '''
    id - INT
    title - Varchar
    content - Text
    updated_at - Datetime
    created at - Datetime
    photo - image
    is_published - Boolean
    '''

    title = models.CharField(max_length=150)
    content = models.TextField(blank = True)    # blank - говорит о том, что данное поле является не обязательным к заполнению
    created_at = models.DateTimeField(auto_now_add= True)   # Время создания
    updated_at = models.DateTimeField(auto_now= True)       # Время последнего обновления
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    is_published = models.BooleanField(default = True)
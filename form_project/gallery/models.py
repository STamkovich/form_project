from django.db import models


class Gallery(models.Model):
    image = models.FileField(upload_to='my_data')  # в image хранится только сcылка на файл а upload_to папка для файлов


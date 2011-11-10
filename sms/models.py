# -*- coding: utf-8 -*-
from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=100, verbose_name='Утасны дугаар')

    class Meta:
        verbose_name = 'Утасны дугаар'
        verbose_name_plural = 'Утасны дугаарууд'

class Message(models.Model):
    send_number = models.ForeignKey(PhoneNumber, verbose_name='Илгээх дугаар')
    content  = models.TextField(max_length=160, verbose_name='Агуулга')

    class Meta:
        verbose_name = 'Мессеж'
        verbose_name_plural = 'Мессежнүүд'

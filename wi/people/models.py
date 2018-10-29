#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    TEACHER_CHOICES = (
            ('junior', 'Junior'),
            ('senior', 'Senior'))

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50, choices=TEACHER_CHOICES)
    email = models.EmailField(max_length=100)
    entry_date = models.DateField(default=timezone.now)
    active_user = models.BooleanField()
    def __str__(self):
        return self.name + self.surname

class Student(models.Model):
    STUDENT_CHOICES = (
        ('BACHILLER', (
            ('primero', 'Primero'),
            ('segundo', 'Segundo')
        )),
        ('ESO', (
            ('tercero', 'Tercero'),
            ('cuarto', 'Cuarto')
        )))

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50, choices=STUDENT_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    entry_date = models.DateField(default=timezone.now)
    active_user = models.BooleanField()
    def __str__(self):
        return self.name + self.surname

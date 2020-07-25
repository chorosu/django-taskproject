from django.db import models

# Create your models here.

PRIORITY = (('danger','veryhigh'),('warning','high'),('info','normal'),('success','low'))

class TodoModel(models.Model):
    title = models.CharField(verbose_name = 'タスク名', max_length=100)
    memo = models.TextField(verbose_name = 'メモ', blank=True)
    priority = models.CharField(
        verbose_name = '優先度',
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField(verbose_name = '期限')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
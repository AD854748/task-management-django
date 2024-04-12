# models.py
from django.db import models

class StoryModel(models.Model):
    STATUS_CHOICES = [
        ('TO_DO', 'TO_DO'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('HOLD', 'HOLD'),
         ('QA', 'QA'),
          ('PO_REVIEW', 'PO_REVIEW'),
          ('COMPLETED', 'COMPLETED'),
    ]
    PRIORITY_CHOICES = [
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_updated_on = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    assigned_to=  models.CharField(max_length=100)
    assignee=  models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=PRIORITY_CHOICES)
    
 

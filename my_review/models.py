# reviews/models.py
from django.db import models

class Review(models.Model):
    OCCUPATION_CHOICES = [
        ('IT', 'IT'),
        ('Education', 'Education'),
        ('HR', 'HR'),
        ('Connection', 'Connection'),
        ('Other', 'Others'),
    ]
    
    REASON_CHOICES = [
        ('Employment', 'Employment'),
        ('Product Purchase', 'Product Purchase'),
        ('Service Inquiry', 'Service Inquiry'),
        ('Other', 'Other'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    comment = models.TextField()
    rating = models.IntegerField()
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_opt_in = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=False)
    reply = models.TextField(blank=True, null=True, default="Thanks for the feedback.")

    def __str__(self):
        return self.name

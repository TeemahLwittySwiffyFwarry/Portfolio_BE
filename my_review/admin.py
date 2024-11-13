# reviews/admin.py
from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation','comment', 'is_approve')
    list_editable = ('is_approve',)

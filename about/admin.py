from django.contrib import admin
from .models import about
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(about)
class aboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
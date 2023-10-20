from django.contrib import admin
from .models import Voca

# Register your models here.
@admin.register(Voca)
class VocaAdmin(admin.ModelAdmin):
    list_display = ('word_entry', 'word_def', 'illustration', 'examples', 'thesaurus')
    list_filter = ('word_entry', 'created')
    search_fields = ('word_entry',)
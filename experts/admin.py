from django.contrib import admin

from experts.models import Category, ExpertProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(ExpertProfile)

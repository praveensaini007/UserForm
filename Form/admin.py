from django.contrib import admin

from Form.models import FormInfo


class FormInfoModel(admin.ModelAdmin):
    list_display = ('Name', 'Dob', 'Email', 'Mobile')


# Register your models here.
admin.site.register(FormInfo, FormInfoModel)

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Work, WorkFile, WorkShot
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WorkAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Work
        fields = '__all__'


class WorkShotInline(admin.TabularInline):
    model = WorkShot
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Дополнительные изображения"


class WorkFileInline(admin.TabularInline):
    model = WorkFile
    extra = 0


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    """Архитектура"""
    prepopulated_fields = {"url": ("title",)}
    view_on_site = False
    list_display = ("title","url", "draft")
    search_fields = ("title",)
    inlines = [WorkShotInline, WorkFileInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = WorkAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_photo.url} width="550">')

    get_image.short_description = "Превью выбранного изображения"
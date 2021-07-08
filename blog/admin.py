from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, BlogFile, BlogShot, Reviews
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = '__all__'


admin.site.register(Reviews)


class BlogShotInline(admin.TabularInline):
    model = BlogShot
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Дополнительные изображения"

class BlogFileInline(admin.TabularInline):
    model = BlogFile
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Блог"""
    prepopulated_fields = {"url": ("title",)}
    view_on_site = False
    list_display = ("title","url", "draft")
    list_filter = ("date",)
    search_fields = ("title",)
    inlines = [BlogShotInline, BlogFileInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = BlogAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="550">')

    get_image.short_description = "Превью выбранного изображения"
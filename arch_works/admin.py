from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Architecture, Architector, Style, ArchitectureShots
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ArchAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Architecture
        fields = '__all__'


class ArchitectorAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Architector
        fields = '__all__'

    def clean(self):
        # BC  Years
        if self.cleaned_data['date_of_birth'] < 0 and self.cleaned_data['date_of_death'] < 0:
            if self.cleaned_data['date_of_birth'] < self.cleaned_data['date_of_death']:
                return self.cleaned_data
        
        # AD Years
        if self.cleaned_data['date_of_death'] == 0 or self.cleaned_data['date_of_birth'] < self.cleaned_data['date_of_death']:
            return self.cleaned_data
        raise forms.ValidationError('Ошибка введенных значение полей ("Дата рождения" и "Дата смерти"). Перепроверьте их и попробуйте еще раз.')

class StyleAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Style
        fields = '__all__'


@admin.register(Architector)
class ArchitectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    view_on_site = False
    model = Architector
    list_display = ("name", "url", "draft")
    list_filter = ("country",)
    search_fields = ("name",)
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = ArchitectorAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="550"')

    get_image.short_description = "Превью выбранного изображения"



@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    view_on_site = False
    model = Style
    list_display = ("name", "url", "draft")
    search_fields = ("title",)
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = StyleAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="550"')

    get_image.short_description = "Превью выбранного изображения"


class ArchitectureShotsInline(admin.TabularInline):
    model = ArchitectureShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Дополнительные изображения"


@admin.register(Architecture)
class ArchitectureAdmin(admin.ModelAdmin):
    """Архитектура"""
    prepopulated_fields = {"url": ("title",)}
    view_on_site = False
    list_display = ("title","url", "draft")
    list_filter = ("styles","architectors")
    search_fields = ("title", "styles__name")
    form = ArchAdminForm
    inlines = [ArchitectureShotsInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_photo.url} width="550">')

    get_image.short_description = "Превью выбранного изображения"












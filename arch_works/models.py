from django.db import models
from django.urls import reverse
from .custom_validators import validate_resolution_photo



class Architecture(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    main_photo = models.ImageField("Главное фото", upload_to="architecture/", validators=[validate_resolution_photo])
    year = models.SmallIntegerField("Дата появления", default=2021)
    country = models.CharField("Страна", max_length=30)
    architectors = models.ManyToManyField("Architector", verbose_name="архитекторы", related_name="architectors")
    styles = models.ManyToManyField("Style", verbose_name="стили")
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-pk"]
        verbose_name = "Архитектурный шедевр"
        verbose_name_plural = "Архитектурные шедевры"


    def get_absolute_url(self):
        return reverse("arch_detail", kwargs={"url":self.url})




class ArchitectureShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="architecture_shots/")
    architecture = models.ForeignKey(Architecture, verbose_name="архитектура", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр"
        verbose_name_plural = "Кадры"


class Architector(models.Model):
    """Архитекторы"""
    name = models.CharField("Имя", max_length=100)
    country = models.CharField("Страна", max_length=200)
    date_of_birth = models.SmallIntegerField("Дата рождения", default=0, help_text="*Для значений годов до н.е, используйте отрицательные числа.")
    date_of_death = models.SmallIntegerField("Дата смерти", default=0, help_text="*Если этой даты нет, просто оставьте значение 0.<br/> Для значений годов до н.е, используйте отрицательные числа.")
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="architectors/", validators=[validate_resolution_photo])
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Архитектор"
        verbose_name_plural = "Архитекторы"

    def get_absolute_url(self):
        return reverse("architector_detail", kwargs={"url":self.url})

class Style(models.Model):
    """Стили"""
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="architecture_styles_images/", validators=[validate_resolution_photo])
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Cтиль"
        verbose_name_plural = "Cтили"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"url":self.url})






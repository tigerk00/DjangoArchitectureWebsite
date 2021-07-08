from django.db import models


class Work(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    main_photo = models.ImageField("Главное фото", upload_to="work/", default="default.jpg")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-pk"]
        verbose_name = "Моя работа"
        verbose_name_plural = "Мои работы"


class WorkShot(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="work_shots/")
    work = models.ForeignKey(Work, verbose_name="работа", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class WorkFile(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to="work_files/")
    work = models.ForeignKey(Work, verbose_name="работа", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

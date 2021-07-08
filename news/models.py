from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    poster = models.ImageField("Изображение", upload_to="news/", blank=True, default="default.jpg")
    description = models.TextField()
    date = models.DateTimeField()
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField(max_length=130, unique=True)
    source = models.CharField("Первоисточник", max_length=300, default="Мы первоисточники")
    important = models.BooleanField("Важно", default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость мира архитектуры"
        verbose_name_plural = "Новости мира архитектуры"


class NewsShot(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="news_shots/")
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class NewsFile(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to="news_files/")
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"




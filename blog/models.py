from django.db import models

class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    poster = models.ImageField("Изображение", upload_to="blog/", blank=True, default="default.jpg")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField(max_length=130, unique=True)


    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class BlogShot(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="blog_shots/")
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class BlogFile(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Файл", upload_to="blog_files/")
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    blog = models.ForeignKey(Blog, verbose_name="Блог", on_delete=models.CASCADE)
    allowed = models.BooleanField("Допущен", default=False)

    def __str__(self):
        return f"{self.name} - {self.blog}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

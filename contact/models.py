from django.db import models

class ContactInfo(models.Model):
    address = models.CharField("Адрес", max_length=200)
    phone_number = models.CharField("Номер телефона", max_length=50)
    email_address = models.EmailField("Електронная почта")
    facebook_link = models.CharField("Facebook", max_length=200, blank=True)
    instagram_link = models.CharField("Instagram", max_length=200, blank=True)
    telegram_link = models.CharField("Telegram", max_length=200, blank=True)
    twitter_link = models.CharField("Twitter", max_length=200, blank=True)
    youtube_link = models.CharField("YouTube", max_length=200, blank=True)
    website = models.CharField("Вебсайт", max_length=200, blank=True)
    iframe_map = models.CharField("Карта", max_length=500, blank=True, help_text="""1.Зайдите в https://www.google.com/maps/ и выберите точное место вашей компании <br/> 
                                                                                    2.Нажмите на кнопку 'поделиться'. <br/>
                                                                                    3.Выберите подпункт 'встраивание карт' и нажмите на кнопку 'копировать HTML'. <br/>
                                                                                    4.Вставьте это значение в даное поле. """)
    class Meta:
        verbose_name = "Блок Контактов"
        verbose_name_plural = "Блоки Контактов"

    def __str__(self):
        return "Контакты"

class ContactEmail(models.Model):
    name = models.CharField("Имя/никнейм", max_length=200)
    email = models.EmailField("Е-mail",)
    message = models.TextField("Сообщение",)

    class Meta:
        verbose_name = "Сообщение от пользователя"
        verbose_name_plural = "Сообщения от пользователей"

    def __str__(self):
        return f"Сообщение от: {self.name}"


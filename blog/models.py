from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Текст')
    image = models.ImageField('Картинка', upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title[:50]}"

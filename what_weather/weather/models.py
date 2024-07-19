from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city} запрос от {self.user.username}, {self.timestamp}'

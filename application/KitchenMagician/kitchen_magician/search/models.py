
from django.db import models
class SearchKeyword(models.Model):
    # CASCADE, once the user is deleted, the recipe will be deleted automatically
    keyword = models.CharField(max_length=100, verbose_name='Keyword')
    count = models.IntegerField(default=1)

    class Meta():
        db_table = 'search_keyword'

    def __str__(self):
        return f'{self.keyword} {self.count}'

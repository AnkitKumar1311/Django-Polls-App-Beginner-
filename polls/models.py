from django.db import models
from datetime import datetime as dt
from django.utils import timezone
import datetime

#   Question Model
class Question(models.Model) : 
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = dt.now())
    is_published = models.BooleanField(default=True)

    def __str__(self) : 
        return self.question_text

    def was_published_recently(self) : 
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


#   Choices Model
class Choice(models.Model) : 
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) : 
        return self.choice_text

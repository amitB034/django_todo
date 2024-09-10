from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUserのうちカスタマイズするものだけを以下に指定する
    # メールアドレスはデフォルトでnullはOK、他ユーザーとの重複もOKになっているためカスタマイズする
    # yunique=Trueにすると重複できないし、nullにもできなくなる。
    email = models.EmailField('メールアドレス', default=None)

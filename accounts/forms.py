from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# UserCreationFormはDjangoが元々用意している新規登録用のフォーム
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    # このsaveはformのsave。フォームを投稿した時にこのsaveが呼ばれる
    def save(self):
        # commit=Falseだと、DBに保存されない
        user = super().save()  #まずはデフォルトのsaveを呼び出して、email以外のユーザー名やパスワードをセットする。commit=FalseにしておくとDBにはまだ書き込まれない
        user.save()   # このsaveはmodelのsave。これでデータベースに書き込める
        return user
    

class LoginFrom(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password1",)
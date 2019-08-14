from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能に
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserCreationForm
        fields = ("username", "password1", "password2",)

    class LoginForm(AuthenticationForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #htmlの表示を変更可能にする
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['class'] = 'form-control'
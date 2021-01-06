from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # элемент <input> с атрибутом type="password", поэтому
    # браузер будет работать с ним как с полем пароля

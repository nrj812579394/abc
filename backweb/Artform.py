from django import forms


class AddArtForm(forms.Form):
    # required=True表示必填项
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'min_length': '文章标题不能少于2个字符',
                                'required': '文章标题不能为空'
                                })
    desc = forms.CharField(min_length=3, required=True,
                           error_messages={
                                'min_length': '文章简述不能少于3个字符',
                                'required': '文章简述不能为空'
                                })
    content = forms.CharField(required=True,
                              error_messages={
                                'required': '文章内容不能为空'
                                })
    icon = forms.ImageField(required=True,
                            error_messages={
                                'required': '你需要加入一张图片哦'
                            })


class Register(forms.Form):
    username = forms.CharField(min_length=2, required=True,
                               error_messages={
                                   'min_length': '账号长度不能小于两位！',
                                   'required': '账号不能为空'
                                    })
    password = forms.CharField(min_length=2, required=True,
                               error_messages={
                                   'min_length': '密码长度不能少于两位！',
                                   'required': '密码不能为空'
                                    })
    password2 = forms.CharField(min_length=2, required=True,
                                error_messages={
                                   'min_length': '密码长度不能少于两位！',
                                   'required': '密码不能为空'
                                    })


class EditArt(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'min_length': '文章标题不能少于2个字符',
                                'required': '文章标题不能为空'
                                })
    desc = forms.CharField(min_length=3, required=True,
                           error_messages={
                                'min_length': '文章简述不能少于3个字符',
                                'required': '文章简述不能为空'
                                })
    content = forms.CharField(required=True,
                              error_messages={
                                'required': '文章内容不能为空'
                                })
    icon = forms.ImageField(required=False)
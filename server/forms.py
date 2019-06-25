# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:43
# @Author  : Langu
# @Email   : xblinux06@gmail.com
from django import forms
from .models import ServerInfo

class ServerForm(forms.ModelForm):
    class Meta:
        model = ServerInfo
        fields = (
            'server_name',
            'ip',
            'cpu',
            'mem',
            'disk',
            'net',
            'os_version',
            's_type',
            's_status',
            'mark'
        )
        widgets = {
            'server_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.Select(attrs={'class': 'form-control'}),
            'disk': forms.TextInput(attrs={'class': 'form-control'}),
            'mem': forms.TextInput(attrs={'class': 'form-control'}),
            'net': forms.TextInput(attrs={'class': 'form-control'}),
            'os_version': forms.TextInput(attrs={'class': 'form-control'}),
            'mark': forms.TextInput(attrs={'class': 'form-control'}),
            's_status': forms.Select(attrs={'class': 'form-control'}),
            's_type': forms.Select(attrs={'class': 'form-control'}),
        }


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Account(models.Model):
    email = models.EmailField(verbose_name=u"账号")
    key = models.CharField(max_length=256, verbose_name="Auth_Key", null=True, blank=True)
    access_key = models.CharField(max_length=256, verbose_name="Access Key", null=True, blank=True)
    secret_key = models.CharField(max_length=256, verbose_name="Secret Key", null=True, blank=True)
    product_list = (
        ('cloudflare', 'cloudflare'),
        ('qiniu', 'qiniu')
    )
    product = models.CharField(max_length=30, choices=product_list, verbose_name=u"厂商")

    def __str__(self):
        return "%s(%s)" % (self.email, self.product)


    class Meta:
        verbose_name = u"账号"
        verbose_name_plural = u"账号"


class Domain(models.Model):
    domain = models.CharField(verbose_name=u"域名", max_length=50, unique=True)
    account_id = models.ForeignKey("Account", verbose_name=u"关联账号")
    zone_id = models.CharField(max_length=256, verbose_name=u"区域ID", null=True, blank=True)

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = u"域名"
        verbose_name_plural = u"域名"
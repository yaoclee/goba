# coding=utf-8
from __future__ import unicode_literals

from django.db import models

SELECT_ACTIVITY = (
    ('0', u'限时特卖'),
    ('1', u'1元抢购'),
    ('2', u'新人专享'),
    ('3', u'9块9'),
)

SELECT_SETTLEMENT = (
    ('0', u'平台扣款'),
    ('1', u'淘宝扣款'),
)

SELECT_CLASSIFICATION = (
    ('0', u'女装'),
    ('1', u'男装'),
    ('2', u'母婴'),
    ('3', u'内衣'),
    ('4', u'食品'),
    ('5', u'美妆'),
    ('6', u'箱包'),
    ('7', u'鞋帽'),
    ('8', u'珠宝'),
    ('9', u'配饰'),
    ('10', u'文体'),
    ('11', u'家电'),
    ('12', u'居家百货'),
    ('13', u'家装家纺'),
    ('14', u'手机数码'),
    ('15', u'户外运动'),
)

def item_img_folder(insntance, filename):
    return "images/%s/%s" % (insntance.id, filename)

class SignUpItem(models.Model):
    activity = models.CharField(verbose_name=u'选择活动', max_length=1, choices=SELECT_ACTIVITY, blank=True)
    link = models.CharField(u'链接', max_length=200, null=False, blank=False)
    name = models.CharField(u'标题', max_length=200, null=False, blank=False)
    price = models.DecimalField(u'普通价', max_digits=6, decimal_places=2, null=False, blank=False)
    price_activity = models.DecimalField(u'活动价', max_digits=6, decimal_places=2, null=True, blank=True)
    img = models.ImageField(u'图片', upload_to=item_img_folder);
    commision = models.DecimalField(u'佣金',max_digits=6, decimal_places=2, null=True, blank=True)
    settlement = models.CharField(verbose_name=u'结算方式', max_length=1, choices=SELECT_SETTLEMENT, blank=True)
    limitations = models.IntegerField(u'每人限购', null=True, blank=True)
    classification = models.CharField(verbose_name=u'类目', max_length=2, choices=SELECT_CLASSIFICATION, blank=True)
    
    class Meta:
        verbose_name = u"添加报名"
        verbose_name_plural = u"添加报名"
    
    def __unicode__(self):
        return self.name

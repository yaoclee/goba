# coding=utf-8
from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from operate.models import SignUpItem

def index(request):
    context = RequestContext(request)
    return render_to_response("index.html", context)

import json
def get_all_items(request):
    print "ok"
    sign_up_items = SignUpItem.objects.all();
    items = []
    
    for sign_up_item in sign_up_items:
        item = {u'活动' : sign_up_item.activity, 
                u'链接' : sign_up_item.link.encode('utf-8'),
                u'标题' : sign_up_item.name.encode('utf-8'),
                u'价格' : str(sign_up_item.price),
                u'活动价格' : str(sign_up_item.price_activity),
                u'图片' : 'media/' + str(sign_up_item.img),
                u'佣金比例' : str(sign_up_item.commision),
                u'每人限购' : str(sign_up_item.limitations),
                u'类目' : sign_up_item.classification
                }
        items.append(item)
    
    return HttpResponse(json.dumps(items), content_type='application/json')

def get_all_items_en(request):
    print "ok"
    sign_up_items = SignUpItem.objects.all();
    items = []
    
    for sign_up_item in sign_up_items:
        item = {'activity': sign_up_item.activity, 
                'link': sign_up_item.link,
                'name': sign_up_item.name,
                'price' : str(sign_up_item.price),
                'activity_price' : str(sign_up_item.price_activity),
                'image' : 'media/' + str(sign_up_item.img),
                'ratio' : str(sign_up_item.commision),
                'count' : str(sign_up_item.limitations),
                'classification' : sign_up_item.classification
                }
        items.append(item)
    
    return HttpResponse(json.dumps(items), content_type='application/json')
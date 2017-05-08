# coding=utf-8
from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from operate.models import SignUpItem

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def index(request):
    context = RequestContext(request)
    return render_to_response("index.html", context)

import json
def get_all_items(request):
    print "ok"
    sign_up_items = SignUpItem.objects.all();
    items = []
    
    for sign_up_item in sign_up_items:
        item = {u'活动' : sign_up_item.get_activity_display(), 
                u'链接' : sign_up_item.link.encode('utf-8'),
                u'标题' : sign_up_item.name.encode('utf-8'),
                u'价格' : str(sign_up_item.price),
                u'活动价格' : str(sign_up_item.price_activity),
                u'图片' : 'media/' + str(sign_up_item.img),
                u'佣金比例' : str(sign_up_item.commision),
                u'每人限购' : str(sign_up_item.limitations),
                u'类目' : sign_up_item.get_classification_display(),
                }
        items.append(item)
    
    return HttpResponse(json.dumps(items, ensure_ascii=False, encoding='utf-8'), content_type='application/json')

def get_all_items_en(request):
    print "ok"
    sign_up_items = SignUpItem.objects.all();
    items = []
    
    for sign_up_item in sign_up_items:
        item = {'activity': sign_up_item.get_activity_display(), 
                'link': sign_up_item.link,
                'name': sign_up_item.name,
                'price' : str(sign_up_item.price),
                'activity_price' : str(sign_up_item.price_activity),
                'image' : 'media/' + str(sign_up_item.img),
                'ratio' : str(sign_up_item.commision),
                'count' : str(sign_up_item.limitations),
                'classification' : sign_up_item.get_classification_display(),
                }
        items.append(item)
    
    return HttpResponse(json.dumps(items, ensure_ascii=False, encoding='utf-8'), content_type='application/json')

import hashlib
import receive
import reply

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle(request):
    print "################in func handle ###############"
    if request.method == 'GET':
        print "################in func GET ###############"
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = 'hello2017'

        li = [token, timestamp, nonce]
        li.sort()
        #sha1 = hashlib.sha1()
        #map(sha1.update, li)
        hashcode = "%s%s%s" % tuple(li)
        hashcode = hashlib.sha1(hashcode).hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return HttpResponse(echostr, content_type="text/plain")
        else:
            return HttpResponse(None, content_type="text/plain")
    elif request.method == 'POST': 
        print "################in func POST ###############"
        webData = request.raw_post_data
        print "Handle POST webdata is:", webData
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == "text":
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = "test reply from developer"
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return HttpResponse(replyMsg.send())
        return HttpResponse(None);

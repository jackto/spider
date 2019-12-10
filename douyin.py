import urllib2
import re
import json
import time
import os.path
import ssl
#import execjs
import string

'''
ssl._create_default_https_context = ssl._create_unverified_context

url="https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqLV4UkWUjUPthc6Gm-EM7lAwvDqyjOWdzj7KjnlyeUgXBYF3whC_RtU2K4jk8YYjzGVKCAfKQckBISTJb7vJWznSQEsI3biRbHYimcRPBuwcsm8nlERUhq-1q3FotcRlmUD2CDfGBEpeKb0qZHW7PDeO00efWrWmm&type=1&query=%E6%B7%B1%E8%93%9D%E4%BF%9D&k=82&h=Y"
#url="https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%B7%B1%E8%93%9D%E4%BF%9D&ie=utf8&_sug_=n&_sug_type_="
url="https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqua-cnPJQ8VblN5h-po5IFgwvDqyjOWdzj7KjnlyeUgXBYF3whC_RtU2K4jk8YYjzGVKCAfKQckBISTJb7vJWznSQEsI3biRbHYimcRPBuwcsm8nlERUhq2vlcsJfInLIs9e9j2Y2eDKSte-oFjtKOmRTpLLTNgHY&type=1&query=%E6%B7%B1%E8%93%9D%E4%BF%9D"

headers ={
    "Cookie":"CXID=87356E3FC93A4F51668B4F1136F626B4; SUID=F411BA763565860A5CD39545000AB490; ad=1lllllllll2t1iqVlllllV8FuzllllllNroSdlllllwllllljqxlw@@@@@@@@@@@; IPLOC=CN1100; SUV=1557380118234187; ABTEST=0|1557380121|v1; weixinIndexVisited=1; JSESSIONID=aaainIqobEKjYfznayzPw; SNUID=E705AE6213169CAF995230A8140E7205; sct=9; PHPSESSID=7984cct5b1lhljc8ql6u3r4bj3",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer":"https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%B7%B1%E8%93%9D%E4%BF%9D&ie=utf8&_sug_=n&_sug_type_=",
    "Upgrade-Insecure-Requests":1
}

data=None
req = urllib2.Request(url,data,headers)
response  = urllib2.urlopen(req)
html = response.read()
print html
#ctx = execjs.compile(html)
#print ctx.eval("url")


url = 'https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqxMEFQh8bcXtyPuv9FdbqtgwvDqyjOWdzGKZpqcew4wqSAf39Rma6fvPgMoBGi2IY1rjcQK-tYx6a-R_37tkeMtYi8OkB1SM9M-q6bM_mGiKY_KWh2oV-g1d_mbgBLgQVp7f72mIfYC_sJs_Ieiu0WKUiiWOv1GPM&amp;type=1&amp;query=loveduobaoyu&amp;k=21&amp;h=U"'
b = 21
a = string.index(url, "url=")
c = -1
print url[a+4+26+b]
#print string.index(url,'U')
#c = string.index(url, "&k=")

#a = string.sub(a + 4 + parseInt("26") + b, 1), this.href += "&k=" + b + "&h=" + a)


url='https://api-hl.amemv.com/aweme/v1/aweme/post/?version_code=6.2.0&pass-region=1&pass-route=1&js_sdk_version=1.14.0.0&app_name=aweme&vid=5ED2ED12-501E-4130-B45C-B40775027D98&app_version=6.2.0&device_id=48084608407&channel=App%20Store&mcc_mnc=46000&aid=1128&screen_width=1242&openudid=af9b6e7c15336880cd90e3cb33a2695159cb11be&os_api=18&ac=WIFI&os_version=12.2&device_platform=iphone&build_number=62022&device_type=iPhone9,2&iid=71142816977&idfa=A40017A4-6783-4E3D-B1BD-B83931346404&min_cursor=0&user_id=72660292516&count=21&max_cursor=0&mas=01dd28d5c10e4cf81ea12698ed93fe8491c8be17dc2ac2659324e8&as=a235cb5e97e97cf0cc6657&ts=1559015575'

headers={
    'Host': 'api-hl.amemv.com',
    'Cookie': 'odin_tt=5484c800290184211a078fe6685587c6bb69c69ca6c3325192a78331b5abb4b284f38e176355d24a3c84312985d6d2f5; sid_guard=75eefaf746906136165f22571706bc2b%7C1558704218%7C5184000%7CTue%2C+23-Jul-2019+13%3A23%3A38+GMT; uid_tt=c1f34133a7de5f6f4649c189f5778884; sid_tt=75eefaf746906136165f22571706bc2b; sessionid=75eefaf746906136165f22571706bc2b; install_id=71142816977; ttreq=1$db7caa9ec962720119c4de3dafde56057692a171',
    'x-tt-token': '0075eefaf746906136165f22571706bc2bfe396236b2734d29a7a7a5a1ef91706133ce0fdc94ea89e09dd04f44812e835d10',
    'sdk-version': '1',
    'user-agent': 'Aweme 6.2.0 rv:62022 (iPhone; iOS 12.2; zh_CN) Cronet',
    'x-khronos': '1559015576',
    'x-pods': "'",
    'x-gorgon': '830000000000687bd5eeb28e07dde2a1572e85d18bc99ba3ddde',
}

data=None
req = urllib2.Request(url,data,headers)
response  = urllib2.urlopen(req)
html = response.read()
decode= json.loads(html)
print decode
'''

data_dir = "douyin"

filenames = os.listdir(data_dir)
for file in filenames:
    with open(data_dir+"/"+file) as load_f:
        load_dict = json.load(load_f)

    if 'aweme_list' not in load_dict:
        continue

    for each in load_dict['aweme_list']:
        url = each['video']['play_addr']['url_list'][0]
        print("%s$%s$%s$%s$%s$%s$%s$%s$%s"%(each['desc'],each['author']['nickname'],each['aweme_id'],url,each['statistics']['comment_count'],each['statistics']['digg_count'],each['statistics']['download_count'],each['statistics']['share_count'],each['statistics']['forward_count']))

        if os.path.exists(each['aweme_id']+".mp4"):
            continue
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        video = response.read()
        with open(each['aweme_id']+".mp4","w") as f:
            f.write(video)
            time.sleep(1)
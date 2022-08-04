import requests
import re
import json
import time
def vcf(name,tel):
    f = open("tel.vcf", "a",encoding="utf-8")
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:2.1\n")
    f.write("FN:"+name+"\n")
    f.write("TEL;CELL:"+tel+"\n")
    f.write("END:VCARD\n")
    f.close()
with open("data.txt","r",encoding="utf-8") as f:
    res=f.read()
    lr=re.findall("<a class=\"c_tx q_namecard hotclick\" data-hctag=\"spcaretab.commentlink.click\" data-hcsuffix=\"feedpage\"(.*?)\">",res)
    jl=1
    btwaf="14740193"
    rlist=[]
    for x in lr:
        t=x.rsplit("/",1)[1]
        isg=True
        for j in rlist:
            if t==j:
                print("发现重复",t,jl)
                isg=False
        if isg:
            r=requests.get("https://cloud.qqshabi.cn/api/qqinfo.php?qq="+t)
            r.encoding=r.apparent_encoding
            res=r.text
            print(res)
            hd={
    'authority': 'qb-api.ltd',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': "https://qb-api.ltd/allcha.php?qq="+t+"&btwaf="+btwaf,
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
            r1=requests.get("https://qb-api.ltd/allcha.php?qq="+t+"&btwaf="+btwaf,headers=hd)
            r1.encoding=r1.apparent_encoding
            res1=r1.text
            rrr=re.findall("window.location.href =\"(.*?)\";",res1)
            if len(rrr)>0:
                print("防火墙绕过",btwaf,jl)
                btwaf=rrr[0].rsplit("btwaf=",1)[1]
                r1=requests.get("https://qb-api.ltd"+rrr[0],headers=hd)
                r1.encoding=r1.apparent_encoding
                res1=r1.text
            code=json.loads(res1)["code"]
            if code==200:
                name=json.loads(res)["name"]+"("+json.loads(res1)["data"]["place"]+")"
                tel=json.loads(res1)["data"]["mobile"]
                print(name,tel)
                vcf(name,tel)
            rlist.append(t)
        jl=jl+1
        time.sleep(2)

    #https://zy.xywlapi.cc/qqcx?qq=2861882729
    #https://cloud.qqshabi.cn/api/qqinfo.php?qq=3521714145
    #https://cloud.qqshabi.cn/api/tiangou/api.php
    #https://www.591mf.top/api/Queryinfo?qq=3555417902
    #https://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=3521714145


#BEGIN:VCARD
#VERSION:2.1
#FN:7814260568 
#TEL;CELL:0017814260568
#END:VCARD
# coding = utf-8
"""
@Author: Zhiwei Cao
@function: python
"""


import dict_tool
test = """
Host: itemadmin.weiyingjia.org
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
If-None-Match: "5de76581-971"
If-Modified-Since: Wed, 04 Dec 2019 07:51:29 GMT
"""


def str_dict(str_headers):
    di = []
    for i in str_headers.split("\n"):
        he = i.split(": ", 1)
        if he != [""]:
            di.append(he)
    return dict(di)


print(dict_tool.str_dict(test))

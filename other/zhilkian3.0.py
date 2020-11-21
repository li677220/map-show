import requests

url = "https://fe-api.zhaopin.com/c/i/sou?at=fc248f426cfa4ebbbf02d77f1d8b7854&rt=3470eb27c47f4838af90fbd1aac21625&_v=0.26518362&x-zp-page-request-id=1efacd032d3e493cadbb52c5437baab1-1604330609183-416116&x-zp-client-id=e3efb563-7b6c-420a-a75a-3d054d318a65&MmEwMD=5T.zew.LLE264cZy5NB3zSvqjVw8GQbMKQC5ml.ks_JGhiqQMUDwh_Ref_TWz4zeU0Y3coSnrCgUkUlAQSPCFC1tWRrBnV8OZHnN2kyUsKMbujWdVsMevThG1TqmRay2g7NLMyXamKMW1gS4p8I2tK8R20Qq.HdlV8AAng8rPAP9rTPQl4K1kAILVYyb.E4Jfg7gkbDA1aJWVDlNM9MlSmXcO.b0jEw6aXS_rQlM.IBJBHAcqK0tYaBcJSB6__pLyT2ag0MgpwfLAg6LfY6g12TWTawUyPjHXNyfqkykpw9PZHQGoHkV3vqxi_ICzfTe6RqTS7UF5a5If2Psh.M3YcEkvVmJAdloVXap7BeXfK.A.ziP9LZiG3M7R1fA0CbMCnLgD.fAr5Jz7nUUZSrM7S_okbI_XLdLsQtIiPabb9A7qb5y9yT6yog.8LQJM82QoOTd"
#     "https://fe-api.zhaopin.com/c/i/sou?at=fc248f426cfa4ebbbf02d77f1d8b7854&rt=3470eb27c47f4838af90fbd1aac21625&_v=0.62558025&x-zp-page-request-id=60939427a6df4393b660b58a3f98f219-1604331236017-419306&x-zp-client-id=e3efb563-7b6c-420a-a75a-3d054d318a65&MmEwMD=5imKsbmsDuhWYy1cA1rOktx4lBu2ivEGgv3m.dmgerOM2TXvT7Lb2r6DHrM6kqkDyH4O7ZIxBJK7z7j.ntWJ0JZSP_A_oLji3iTGRDUFvr2fh8YHnEwVk0LLUEDJHHKebheB5IphZdh2boNsZ9fptu13R0hXNcoC0plnyYvIJ5DtnEoVB5jsjWXJ7aIGBMKNorAmdjovGxQbd.Ia63vgp5z85CMYbzV_KVLD1WHxVDTznRpR0CUvcLq7csT_qvkAe4yYGDBBKfa2vODwtJGEXTZiL2sqbJ0ziY6bYCNZHg5ViOxJfaLnu6lB7JmTitJTsBMqCbUTS9lD3UTi13Djqf78D7VlycjHlJXR1yjQawLkeO3PxPs3EtqyZdnySczOgo3h"
# _v;x-zp-page-request-id;MmEwMD
resheaders = {
    'access-control-allow-credentials': 'true',
    'access-control-allow-origin': 'https://sou.zhaopin.com',
    'content-length': '54527',
    'content-type': 'application/json; charset=utf-8',
    'date': 'Mon, 02 Nov 2020 15:23:32 GMT',
    'server': 'Tengine',
    'status': '200',
    'vary': 'Accept-Encoding',
    'vary': 'Accept-Encoding',
    'vary': 'Origin',
    'x-zp-page-request-id': '1efacd032d3e493cadbb52c5437baab1-1604330609183-416116',
    'x-zp-request-id': '6d263ddd50ad46308600881a328fa2dd'
}
reqheader = {
    'authority': 'fe-api.zhaopin.com',
    'method': 'POST',
    'path': '/c/i/sou?at=fc248f426cfa4ebbbf02d77f1d8b7854&rt=3470eb27c47f4838af90fbd1aac21625&_v=0.90501684&x-zp-page-request-id=1efacd032d3e493cadbb52c5437baab1-1604330609183-416116&x-zp-client-id=e3efb563-7b6c-420a-a75a-3d054d318a65&MmEwMD=5T.zew.LLE264cZy5NB3zSvqjVw8GQbMKQC5ml.ks_JGhiqQMUDwh_Ref_TWz4zeU0Y3coSnrCgUkUlAQSPCFC1tWRrBnV8OZHnN2kyUsKMbujWdVsMevThG1TqmRay2g7NLMyXamKMW1gS4p8I2tK8R20Qq.HdlV8AAng8rPAP9rTPQl4K1kAILVYyb.E4Jfg7gkbDA1aJWVDlNM9MlSmXcO.b0jEw6aXS_rQlM.IBJBHAcqK0tYaBcJSB6__pLyT2ag0MgpwfLAg6LfY6g12TWTawUyPjHXNyfqkykpw9PZHQGoHkV3vqxi_ICzfTe6RqTS7UF5a5If2Psh.M3YcEkvVmJAdloVXap7BeXfK.A.ziP9LZiG3M7R1fA0CbMCnLgD.fAr5Jz7nUUZSrM7S_okbI_XLdLsQtIiPabb9A7qb5y9yT6yog.8LQJM82QoOTd',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '313',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'adfbid2=0; x-zp-client-id=e3efb563-7b6c-420a-a75a-3d054d318a65; sts_deviceid=175877effd2422-058c91a837321b-303464-1327104-175877effd3ade; sajssdk_2015_cross_new_user=1; ZP_OLD_FLAG=false; POSSPORTLOGIN=5; CANCELALL=1; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DMxNfYOilcsvOMZ4RJHfPDRibByFAu2rZHqX3WBFNitfQI826cQ14j92duji67Dc3%26wd%3D%26eqid%3Da35ea2dc0001a4f3000000065fa012e6; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1604296074,1604302951,1604326124,1604328148; acw_tc=2760821c16043303442934001e369e1fc7ea5643d080268e39773c08cbd3ba; urlfrom=121113803; urlfrom2=121113803; sts_sid=175898db05d44d-0938ed55a2bbd-303464-1327104-175898db05ece3; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221028527247%22%2C%22first_id%22%3A%22175877effe7884-03e4dc6b758c7f-303464-1327104-175877effe8b85%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22%24device_id%22%3A%22175877effe7884-03e4dc6b758c7f-303464-1327104-175877effe8b85%22%7D; at=fc248f426cfa4ebbbf02d77f1d8b7854; rt=3470eb27c47f4838af90fbd1aac21625; LastCity=%E6%88%90%E9%83%BD; LastCity%5Fid=801; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d6025e85-a4d6-4d74-bbb1-305b31357809-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=5; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1604330611',
    'origin': 'https://sou.zhaopin.com',
    'referer': 'https://sou.zhaopin.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
data = {
    'at': "fc248f426cfa4ebbbf02d77f1d8b7854",
    'cityId': "801",
    'companyType': "-1",
    'cvNumber': "JI285272478R90500000000",
    'employmentType': "-1",
    'eventScenario': "pcSearchedSouIndex",
    'jobWelfareTag': "-1",
    'kt': "3",
    'kw': "java",
    'pageSize': "30",
    'rt': "3470eb27c47f4838af90fbd1aac21625",
    'userCode': 1028527247,
    'workExperience': "-1"
}

res = requests.post(url,data=data,headers=reqheader)
print(res)




# import json

# with open(r'C:\Users\lucky\1469502521.json', encoding='utf8') as fl:
#     a = json.loads(fl.read())

# for i in a['comments']:
#     print(f"{i['commenter']['bio']}")
import requests


url = 'https://dgeft87wbj63p.cloudfront.net/f034dcdb25e9d92d0d07_ryuusei_aika_45311556476_1651172361/chunked/index-dvr.m3u8'

# m3u8 = requests.get(url)
segs = url[:-14]
with open('ts_file.txt', 'w') as lf:
    for i in range(982):
        lf.write(f'curl {segs}{i}.ts -o {i}.ts\n')

# print(m3u8.text.split('\n')[-3][:-3])

import json
import subprocess
import os

# dic = {}
# some_shit = subprocess.check_output('rclone lsjson edu:', shell=True)
# json_data = json.loads(some_shit.decode('utf-8'))

# for dicts in json_data:
#     if dicts['IsDir']:
#         dic[dicts['Name']] = [dicts['ID']]

# some_shit = subprocess.check_output('rclone lsjson uwu:', shell=True)
# json_data = json.loads(some_shit.decode('utf-8'))
# for dicts in json_data:
#     if dicts['IsDir']:
#         dic[dicts['Name']] += ([dicts['ID']])

# with open('idk.json', 'w') as fl:
#     json.dump(dic, fl)

with open('idk.json') as fl:
    dic = json.load(fl)

os.chdir('S:/AutoRclone')
for name in dic:
    some_shit = subprocess.check_output(f'python rclone_sa_magic.py -s {dic[name][0]} -d {dic[name][1]}', shell=True)
    # print(some_shit.decode('utf-8'), end='')

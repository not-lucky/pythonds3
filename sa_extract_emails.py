import json
import glob

# write file and emails into a file
a = [i.split('\\')[1] for i in glob.glob("S:/AutoRclone/accounts/*.json")]
x = {}
with open('sa_json_and_emails.txt', 'w') as fl:
    for json_files in a:
        with open(rf'S:/AutoRclone/accounts/{json_files}') as json_file:
            x[json_files] = json.loads(json_file.read())['client_email']

    json.dump(x, fl, sort_keys=True, indent=4)

# read emails from the file create from above
fl = open('sa_json_and_emails.txt')
a = json.loads(fl.read())
fl.close()

with open('emails_only.txt', 'w') as fl:
    for v in a.values():
        print(v, file=fl)

# import subprocess
# import shlex
# import json

# with open('tests.txt', 'a') as fl:
#     subprocess.run(shlex.split('rclone lsjson edu:'), stdout=fl)

# lis = []
# with open('tests.txt') as fl:
#     a = json.loads(fl.read())

# for i in a:
#     print(i['ID'])
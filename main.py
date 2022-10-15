import os
import json
import csv
import urllib.request

path = 'messages'

print("\n\nWelcome to the discord attachment downloader\n\n")

msg_index: dict = None

with open(f'{path}/index.json', 'r') as f:
    msg_index = json.load(f)
    f.close()

channels = [x for x in os.listdir(path) if os.path.isdir(f'{path}/{x}')]

for i in channels:
    file_path = f'{path}/{i}/messages.csv'
    print(f'Reading channel {i}: ', msg_index[i[1:]])
    if not os.path.exists(file_path):
        print(f"WARNING channel has no messages.csv: missing", file_path)
    else:
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                if row[3]:
                    for n, att in enumerate(row[3].split(' ')):
                        print(att)
                        req = urllib.request.Request(
                            att, 
                            data=None, 
                            headers={
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
                            }
                        )
                        g = urllib.request.urlopen(req)
                        file_name = att.split('/')[-1]
                        with open(f'{path}/{i}/{row[0]}-{n}-{file_name}', 'b+w') as f:
                            f.write(g.read())
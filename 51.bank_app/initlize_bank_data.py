import json
import os

if not os.path.exists("accounts"):
    os.mkdir("accounts")

last_account = 1000

with open("last_account.json", "w") as fp:
    json.dump(last_account, fp)

print("files successfully created")

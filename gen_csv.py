import json, glob, random
from datetime import datetime
from pprint import pprint as pp

NAME = "Buy Me a Coffee"
DESC = "No utility, No roadmap. Just buy me a coffee 🙏"
IMG = "https://diewland.github.io/buy-me-a-coffee/assets/{}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
TOKEN_CONFIG = (
    (1, 84),
    (7, 10),
    (30, 5),
    (365, 1),
)

id = 0
for (qty, times) in TOKEN_CONFIG:
    for i in range(0, times):
        #cmd = "cp /Users/m1/Desktop/coffee/{}.png ./assets/{}.png"
        #print(cmd.format(img_name, id))

        # craft data
        metadata = {
          "name": "***",
          "description": DESC,
          "image": "***",
          "attributes": [
            {
              "trait_type": "Qty",
              "value": "***",
            },
          ],
          "compiler": ENGINE,
        }

        # update data
        metadata["name"] = "{} #{}".format(NAME, id)
        metadata["image"] = IMG.format(qty)
        metadata["attributes"][0]["value"] = qty

        # write to file
        with open("./{}/{}".format(OUTPUT_DIR, id), "w") as f:
            json.dump(metadata, f, ensure_ascii=False)

        # increase id
        id += 1

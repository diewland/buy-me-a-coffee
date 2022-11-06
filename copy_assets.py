config = (
    (1, 84),
    (7, 10),
    (30, 5),
    (365, 1),
)

id = 0
for (img_name, times) in config:
    for i in range(0, times):
        cmd = "cp /Users/m1/Desktop/coffee/{}.png ./assets/{}.png"
        print(cmd.format(img_name, id))
        id += 1

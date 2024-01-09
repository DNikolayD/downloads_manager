import os
import shutil

path = input("Chose an extraction path:")

while True:
    if os.path.exists(f"{path}/Music"):
        os.makedirs(f"{path}/Music")
    if os.path.exists(f"{path}/Photos"):
        os.makedirs(f"{path}/Photos")
    if os.path.exists(f"{path}/Videos"):
        os.makedirs(f"{path}/Videos")
    with os.scandir(path) as _dir:
        for file in _dir:
            if file.name.endswith('.wav') or file.name.endswith('.mp3'):
                shutil.move(file.path, f"{path}/Music")
            if file.name.endswith('.gif') or file.name.endswith('.mp4'):
                shutil.move(file.path, f"{path}/Videos")
            if file.name.endswith('.jpg') or file.name.endswith('.png') or file.name.endswith(
                    '.svg') or file.name.endswith('.bmp') or file.name.endswith('.webp'):
                shutil.move(file.path, f"{path}/Photos")

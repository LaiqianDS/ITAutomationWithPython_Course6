#!/usr/bin/env python3

import os, sys
from PIL import Image

for root, dirs, files in os.walk("."):
  for file in files:
    filename, extension = os.path.splitext(file)
    outfile = "/opt/icons/" + filename
    try:
      Image.open(file).rotate(270).resize((128,128)).convert("RGB").save(outfile, "JPEG")

    except IOError:
      print("cannot convert", file)

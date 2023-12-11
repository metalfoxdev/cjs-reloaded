import os

for root, dirs, files in os.walk("/public"):
    for file in files:
        if file.endswith(".html"):


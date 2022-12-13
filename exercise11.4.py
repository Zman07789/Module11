#By Zackary Paulson
import urllib.request
import re

url = input("Enter a URL: ")

try:
    fhand = urllib.request.urlopen(url)
except:
    print("Error: URL is improperly formatted or non-existent")
    exit()

total_paragraphs = 0
for line in fhand:
    line = line.decode().strip()
    paragraphs = re.findall('<p>', line)
    total_paragraphs += len(paragraphs)

print("Number of paragraphs: ", total_paragraphs)
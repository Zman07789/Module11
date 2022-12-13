#By Zackary Paulson

import urllib.request

url = input("Enter a URL: ")

try:
    fhand = urllib.request.urlopen(url)
except:
    print("Error: URL is improperly formatted or non-existent")
    exit()

total_chars = 0
for line in fhand:
    total_chars += len(line)
    if total_chars <= 3000:
        print(line.decode().strip())

print("Number of characters: ", total_chars)
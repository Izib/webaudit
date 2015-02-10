import sys
# Get the first 20 hits in Google
from google import search
for url in search(sys.argv[1], tld='com', lang='en', stop=20):
    print(url)
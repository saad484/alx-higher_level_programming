#!/usr/bin/python3
'''This script fetches data from
https://alx-intranet.htbn.io/status'''

if __name__ == "__main__":
    import urllib.request
    
    with urllib.request.urlopen("https://alx-intranet.htbn.io/status")\
        as response:
        body = response.read()
       
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print('\t- utf8 content: {}'.format(body.decode("utf-8", "replace")))

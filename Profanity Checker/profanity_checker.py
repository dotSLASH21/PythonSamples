import urllib.request

def read_text():
    file = open("movie_quotes.txt")
    contents = file.read()
    contents = contents.replace(' ', '%20')
    contents = contents.replace('\n', '%20')
    file.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read().decode("utf-8")
    connection.close()
    if "true" in output:
        print("Alert: Profane words detected!!!")
    elif "false" in output:
        print("This document has no profane words!")
    else:
        print("Couldn't scan the document properly!")
    
read_text()

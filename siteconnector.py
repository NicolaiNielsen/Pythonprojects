import urllib.request as urllib

#write a function that takes url
#returns response

webpage = "https://google.com/"

def check_connection(webpage):
    print("Checking connection to site")
    response = urllib.urlopen(webpage)

    print("Connected to " + webpage + " success")
    print("The response code was: " + str(response.getcode()))

check_connection(webpage)
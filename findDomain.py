"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
LEVEL : 5kyu"""
def domain_name(url):
    url = url.replace("www.","")
    url = url.replace("https://","")
    url = url.replace("http://","")
    
    return url[0:url.find('.')]

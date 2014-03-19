import urllib
import urllib2

data = {}
number = '12345'

for i in range(400):
    data['nothing'] = number
    url_values = urllib.urlencode(data)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    full_url = url + '?' + url_values

    result = urllib2.urlopen(full_url).read()
    print result
    print number
    foo = result.split(" ")
    try:
        number = [i for i in foo if i.isdigit()][0]
    except Exception as e:
        if "Yes. Divide by two and keep going" in result:
            number = int(number)/2
            print number
            continue
        else:
            print result
            break

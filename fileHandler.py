
# read a file as text and return the string (all web files are located in '/webapp/')
def readFile(path):
    file = open(path, 'r+')
    raw_str = file.read()
    file.close()
    return raw_str

### This is where I process the csv data, you can remove these since you will be using your own functions ##
def split_csv(data):
    raw = data.decode('ascii')
    split = raw.split(',')

    return split

def json_from_array(data):
    json = '{"data":['
    print(len(data))
    i = 0
    for x in data:
        json += '"' + x + '"'
        if not (i == len(data) - 1):
            json += ","

        i += 1

    json += ']}'

    print(json)

    return json

### ###
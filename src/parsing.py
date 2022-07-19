import json

class parse:
    def convert(sef,filename):
        with open(filename) as jf:
            values=json.load(jf)
            return(values)

obj1=parse()
            

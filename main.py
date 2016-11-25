import parser

class juiceTpl(text):
    items = {}
    def __init__(self, text):
        self.text = text

    def addItem(self, key, value):
        self.items[str(key)] = value

    def addItems(self, datas):
        self.items.update(datas)

    def getItem(self, key):
        return self.items.get(key)
    
    def delItem(self, key):
        del self.items[key]

    def parse(self):
        return parser.parse(self.text, self.values)
from datetime import datetime as date

class Tweet():
    
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at =  date.now().strftime("%Y.%m.%d-%H:%M:%S")

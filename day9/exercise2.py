class Notifier:
    def __init__(self, recipitent):
        self.recipitent = recipitent
        
    def send(self, message):
        raise NotImplemented("Subclasses must implement send()")
    
    def __str__(self):
        return f"{self.__class__.name}(recioient = {self.recipient})"
    
class EmailNotifier(Notifier):
    def __init__(self, recipient, email_address):
        super().__init__(recipient)
        self.email_address = email_address
        
    def send(self, message):
        return f"Email to {self.email_address}: {message}"
    
class SMSNotifier(Notifier):
    def __init__(self, recipent, phone_number):
        super().__init__(recipent)
        self.phone_number = phone_number
        
    def send(self, message):
        return f"SMS to {self.phone_number}: {message}"
    
class KakaoNotifier(Notifier):
    def __init__(self, recipent, kakao_id):
        super().__init__(recipent)
        self.kakao_id = kakao_id

    def send(self, message):
        return f"KakaoTalk to {self.kakao_id}: {message}"
    
notifiers = [
    EmailNotifier("Arjn", "arjun@gmail.com"),
    SMSNotifier("Arjun", "+4758745"),
    KakaoNotifier("Arjun", "arjun_kakaotalk")
    
]

for notifier in notifiers:
    print(notifier.send("Assignment due tomorrow!"))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
              
from abc import ABC, abstractmethod

#Insted of inheritance -  use composition
class MessageFormatter:
    def format(self, receipent, message):
        return f"Dear{receipent}: {message}"
    
class Emailsender:
    def send(self, address, content):
        return f"Email sent to {address} :{content}"
    
class kakosender:
    def send(self, kakao_id, content):
        return f"KakoTalk sent to {kakao_id} : {content}"
    
class Smssender:
    def send(self, phone, content):
        return f"Sms sent to {phone} : {content}"
    
class NotificationService:
    def __init__(self, sender, formatter=None):
        self.sender =sender #any sender object
        self.formatter = formatter or MessageFormatter()
        
    def notify(self, recipient, message, address):
        content = self.formatter.format(recipient, message)
        return self.sender.send(address, content)

email_service = NotificationService(sender=Emailsender())
kako_service = NotificationService(sender=kakosender())
sms_service = NotificationService(sender=Smssender())

print(email_service.notify("Arjun", "Assignment due Tomorrow", "arjun@gmail.com"))
print(kako_service.notify("Arjun", "video lecture available", "arjun_kako"))
print(sms_service.notify("Arjun", "Exam reminder", "+82-10-123-345"))
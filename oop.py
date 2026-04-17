class Phone:
    price = 5054654
    color = "black"
    brand = "samsung"

    features = ["camera", "fingerprint", "face unlock", "fast charging"]

    def call(self):
        print("Calling...")

    def send_message(self, phone, sms):
        text = f"sending sms to : {phone} with message : {sms}"
        return text


my_phone = Phone()
res = my_phone.send_message(123456789, "hello")
print(res)

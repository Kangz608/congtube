import requests


class Notification:
    def __init__(self):
        self.url = "https://api-alimtalk.cloud.toast.com/alimtalk/v1.4/appkeys/wlWnt7o7FWFODrKQ/messages"
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Secret-Key': '35gQk6cs',
        }

    def payment_complete(self, phonenumber, user, product_name, amount): # 결제완료
        data = f'|"plusFriendId":"콩튜브","templateCode":"ordercompleteend","requestDate":"","recipientList":[|"recipientNo":"{phonenumber}","templateParameter":|"고객명":"{user}","상품명":"{product_name}","결제금액":"{amount}","주문내역 확인하기 버튼":""??]?'
        result1 = data.replace("|", "{")
        result2 = result1.replace("?", "}")
        response = requests.post(self.url, headers=self.headers, data=result2.encode('utf-8'))
        print(response.status_code)
        print(response.text)

    def video_complete(self, phonenumber, user, channel): # 영상제작완료
        data = f'|"plusFriendId":"콩튜브","templateCode":"videocheckk","requestDate":"","recipientList":[|"recipientNo":"{phonenumber}","templateParameter":|"고객명":"{user}","채널명":"{channel}","콩튜브 바로가기 버튼":""??]?'
        result1 = data.replace("|", "{")
        result2 = result1.replace("?", "}")
        response = requests.post(self.url, headers=self.headers, data=result2.encode('utf-8'))
        print(response.status_code)
        print(response.text)

    def payment_cancel(self, phonenumber, user, channel, created_at, cancelreason): # 결제취소
        data = f'|"plusFriendId":"콩튜브","templateCode":"ordercancel","requestDate":"","recipientList":[|"recipientNo":"{phonenumber}","templateParameter":|"고객명":"{user}","채널명":"{channel}","주문일시":"{created_at}","취소사유":"{cancelreason}","연락가능시간":"10:00~20:00","카카오톡 콩튜브 채널 버튼":""??]?'
        result1 = data.replace("|", "{")
        result2 = result1.replace("?", "}")
        response = requests.post(self.url, headers=self.headers, data=result2.encode('utf-8'))
        print(response.status_code)
        print(response.text)

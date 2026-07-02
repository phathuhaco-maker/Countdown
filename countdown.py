from datetime import datetime
import requests
import os

today = datetime.utcnow().date()

events = [
    ("📚", "Đánh giá năng lực V-ACT đợt 1 năm 2027", datetime(2027,4,3).date()),
    ("📚", "Đánh giá năng lực HSCA đợt 1 năm 2027", datetime(2027,3,27).date()),
    ("📚", "Đánh giá năng lực SPT Đại học Sư phạm Hà Nội năm 2027", datetime(2027,2,13).date()),
    ("🧠", "Đánh giá tư duy TSA đợt 1 năm 2027", datetime(2027,1,24).date()),
    ("🏆", "Kỳ thi tốt nghiệp THPT 2027", datetime(2027,6,5).date()),
    ("📝", "Đánh giá năng lực HSA đợt 1 năm 2027", datetime(2027,2,28).date()),
]

message = ""

for emoji, name, date in events:
    days = (date - today).days
    message += f"{emoji} Còn **{days} ngày** đến kỳ thi {name}.\n"

requests.post(
    os.environ["WEBHOOK_URL"],
    json={
        "username": "Lo Mà Học",
        "avatar_url": "https://i.imgur.com/J5LVHEL.png",
        "content": message
    }
)

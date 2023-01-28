import random,time,requests,socket,datetime,os
from fake_useragent import UserAgent
ua = UserAgent()


def randomIp():
    classIp = ["a","b","c"]
    ip_standart = [i for i in range(1,254)]
    decision = random.choice(classIp)
    a = 0#Breakpoint
    if(decision == "c"):
        _1,_2,_3 = str(random.choice(ip_standart)),str(random.choice(ip_standart)),str(random.choice(ip_standart))
        endIp = "".join([_1,".",_2,".",_3,".",str(random.choice(ip_standart))])
        if(endIp == None):#cek jika return None
            randomIp()
        return endIp
    elif(decision == "b"):
        _1,_2 = str(random.choice(ip_standart)),str(random.choice(ip_standart))
        endIp = "".join([_1,".",_2,".",str(random.choice(ip_standart)),".",str(random.choice(ip_standart))])
        if(endIp == None):
            randomIp()
        return endIp
    elif(decision == "a"):
        _1 = str(random.choice(ip_standart))
        endIp = "".join([_1,".",str(random.choice(ip_standart)),".",str(random.choice(ip_standart)),".",str(random.choice(ip_standart))])
        if(endIp == None):
            randomIp()
        return endIp

def sendReq(mail):
    url = "https://pre.counterside.com/preReg/"
    header = {
        "User-Agent": ua.random
    }
    datas = {
        "email": mail,
        "ipAddr": randomIp(),
        "chkAgr2": "N"
    }
    res = requests.post(url,data = datas,headers=header)
    msg = res.json()
    if 'msg' in msg:
        if msg['msg'] == 'S':
            print("Success")
        else:
            print("Failed")


time_est = 5 * 100000
est_time = datetime.datetime.now() + datetime.timedelta(seconds=time_est)
print(f"Estimasi program selesai: {est_time}")


failed_data = []
with open("1M_GMAIL_mail_no_pass.txt") as f:
    lines = f.readlines()
    j = 0
    for i in lines[300020:]:#loncat ke baris 300020
        j += 1
        print("request ke ",j)
        while True:
            try:
                socket.create_connection(("www.google.com", 80))
                if i.replace("\n","") in failed_data:
                    sendReq(i.replace("\n",""))
                    failed_data.remove(i.replace("\n",""))  
                else:
                    sendReq(i.replace("\n",""))
                break
            except OSError:
                print("Tidak ada internet, mencoba lagi dalam 5 detik...")
                failed_data.append(i.replace("\n",""))
                time.sleep(5)
                continue
            except Exception as e:
                print(f"ada yang error: {e}")
                failed_data.append(i.replace("\n",""))
                break
        if j % 10 == 0:
            os.system('cls')
            print(f"Estimasi program selesai: {est_time}")
        time.sleep(5)#delay 5 detik, kasian server countersidenya kalau pake delay milisecond
        if(j == 50000):#stop kalau udah 50k request
            break

import random,time,requests,socket,datetime
from fake_useragent import UserAgent
ua = UserAgent()


def randomIp():
    classIp = ["a","b","c"]
    ip_standart = [i for i in range(1,254)]
    # print("ip : ",random.choice(classIp))
    decision = random.choice(classIp)
    a = 0
    if(decision == "c"):
        _1,_2,_3 = str(random.choice(ip_standart)),str(random.choice(ip_standart)),str(random.choice(ip_standart))
        endIp = "".join([_1,".",_2,".",_3,".",str(random.choice(ip_standart))])
        if(endIp == None):
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
    print(res)
    if 'msg' in msg:
        if msg['msg'] == 'S':
            print("Success")
        else:
            print("Failed")
# for i in range(100):
#     print(randomIp())
# with open("1M_GMAIL_mail_no_pass.txt") as f:
#     j = 0
#     for i in f:
#         j += 1
#         sendReq(i)
#         time.sleep(.5)
#         if(j == 200000):
#             break

time_est = 0.5 * 200000
est_time = datetime.datetime.now() + datetime.timedelta(seconds=time_est)
print(f"Estimasi program selesai: {est_time}")


failed_data = []
with open("1M_GMAIL_mail_no_pass.txt") as f:
    j = 0
    for i in f:
        j += 1
        while True:
            try:
                socket.create_connection(("www.google.com", 80))
                if i in failed_data:
                    sendReq(i)
                    failed_data.remove(i)  
                else:
                    sendReq(i)
                break
            except OSError:
                print("Tidak ada internet, mencoba lagi dalam 5 detik...")
                failed_data.append(i)
                time.sleep(5)
                continue
            except Exception as e:
                print(f"ada yang error: {e}")
                failed_data.append(i)
                break
        time.sleep(.5)
        if(j == 200000):
            break
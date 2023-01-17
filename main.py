import random,time,requests,socket,datetime,os
from fake_useragent import UserAgent
ua = UserAgent()


def randomIp():
    classIp = ["a","b","c"]
    ip_standart = [i for i in range(1,254)]
    decision = random.choice(classIp)
    a = 0#breakpoint
    if(decision == "c"):
        _1,_2,_3 = str(random.choice(ip_standart)),str(random.choice(ip_standart)),str(random.choice(ip_standart))
        endIp = "".join([_1,".",_2,".",_3,".",str(random.choice(ip_standart))])
        if(endIp == None):#check if returning value None
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

time_est = 0.05 * 100000
est_time = datetime.datetime.now() + datetime.timedelta(seconds=time_est)
print(f"Estimasi program selesai: {est_time}")


failed_data = []
with open("this") as f:#ganti this dengan wordlist email
    #opsi pertama
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
        if j % 10 == 0:
            os.system('cls')
        time.sleep(.05)
        if j == 100000:
            break

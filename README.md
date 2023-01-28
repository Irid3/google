# Install Module
Install dulu requirmentnya
```
pip install -r requirements.txt
```
atau
```
pip3 install -r requirements.txt
```

# Running

## Windows

```
Start-Process python -ArgumentList "main.py" -NoNewWindow -Wait
```
Program akan berhenti kalau terminal diclose.

<br />

---
Kalau ingin program berjalan di background :
---

<br />

```
powershell -Command "Start-Process python -ArgumentList 'main.py' -NoNewWindow -RedirectStandardOutput out.txt -RedirectStandardError err.txt -RedirectStandardInput in.txt
```

## Linux

<br />

```
nohup python main.py > output.log 2>&1 &
```
<br />


# Check realtime output
<br />

## Windows
```
Get-Content -path out.txt -Wait
```
<br />

## Linux
```
tail -f output.log
```

# Stop Program
## Windows

<br />

```
Stop-Process -Id (Get-Process -Name "python" | Select-Object -ExpandProperty Id)
```

<br />

## Linux
<br />
cek dulu pid pythonnya berapa :

<br />

```
ps aux | grep python
```
<br />

kalau udah ketemu tinggal :

<br />

```
kill [ID proses]
```
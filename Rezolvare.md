# Soluție

## 1. DNS over HTTPS
Am implementat funcția aici:
```python
def ipOf(hostname):
    headers = {
        "Accept" :  "application/dns-json"
    }

    par = {
        "name" : hostname,
        "type" : "A"
    }

    response = requests.get('https://1.1.1.1/dns-query', headers =headers, params=par)

    res = response.json()
    ans = res['Answer']
    bloc = ans[0]

    return bloc['data'] #aici e adresa

```
iar aici e un exemplu de execuție
```python
print(test, " are IP-ul ", ipOf(test))
"amazon.in are IP-ul 52.95.120.67"
```

## 2. Traceroute

Am implementat soluția iar aici este output-ul:

### Ruta către IP1 - 172.217.18.110(google.com)
```
TTL:  1
 IP:  216.182.229.28
 Oras:  Ashburn
 Regiune:  Virginia
 Tara:  United States


TTL:  2
 IP:  100.66.13.208
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  3
 IP:  100.66.14.62
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  4
 IP:  100.66.6.63
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  5
 IP:  100.66.5.209
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  6
 IP:  100.65.15.49
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  7
 IP:  52.93.29.13
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  8
 IP:  100.100.4.6
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  9
 IP:  99.83.65.1
 Oras:  Ashburn
 Regiune:  Virginia
 Tara:  United States


Socket timeout  timed out
Traceback (most recent call last):
  File "traceroute.py", line 42, in traceroute
    _, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

TTL:  10
 IP:  d
 Oras:  ICMP not received
 Regiune:  ICMP not received
 Tara:  ICMP not received


TTL:  11
 IP:  108.170.246.33
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  12
 IP:  108.170.246.34
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  13
 IP:  108.170.232.199
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  14
 IP:  142.250.60.103
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  15
 IP:  209.85.253.184
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  16
 IP:  108.170.238.61
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  17
 IP:  108.170.251.193
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  18
 IP:  172.253.64.119
 Oras:  None
 Regiune:  None
 Tara:  United States
```

### Ruta către 202.27.15.220(studyinaustralia.gov.au)
```
TTL:  1
 IP:  216.182.229.14
 Oras:  Ashburn
 Regiune:  Virginia
 Tara:  United States


TTL:  2
 IP:  100.66.9.250
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  3
 IP:  100.66.11.90
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  4
 IP:  100.66.7.91
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  5
 IP:  100.66.5.251
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  6
 IP:  100.65.15.193
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  7
 IP:  52.93.29.31
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  8
 IP:  100.100.4.24
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  9
 IP:  206.126.237.175
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  10
 IP:  114.31.199.38
 Oras:  San Jose
 Regiune:  California
 Tara:  United States


TTL:  11
 IP:  114.31.199.40
 Oras:  San Jose
 Regiune:  California
 Tara:  United States


TTL:  12
 IP:  175.45.72.33
 Oras:  Sydney
 Regiune:  New South Wales
 Tara:  Australia


TTL:  13
 IP:  175.45.108.214
 Oras:  Sydney
 Regiune:  New South Wales
 Tara:  Australia


TTL:  14
 IP:  124.47.128.38
 Oras:  Canberra
 Regiune:  Australian Capital Territory
 Tara:  Australia


TTL:  15
 IP:  125.7.35.134
 Oras:  Westmead
 Regiune:  New South Wales
 Tara:  Australia


TTL:  16
 IP:  125.7.26.2
 Oras:  Sydney
 Regiune:  New South Wales
 Tara:  Australia


TTL:  17
 IP:  103.83.230.2
 Oras:  None
 Regiune:  None
 Tara:  Australia
```

### Ruta către 54.239.33.92 (amazon.in)
```
//la ip imi mai returneaza 'd', pt ca printez addr[0]

TTL:  1
 IP:  216.182.229.24
 Oras:  Ashburn
 Regiune:  Virginia
 Tara:  United States


TTL:  2
 IP:  100.66.13.128
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  3
 IP:  100.66.14.22
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  4
 IP:  100.66.6.23
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  5
 IP:  100.66.5.113
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  6
 IP:  100.65.13.193
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  7
 IP:  52.93.29.15
 Oras:  None
 Regiune:  None
 Tara:  United States


TTL:  8
 IP:  100.100.6.52
 Oras:  None
 Regiune:  None
 Tara:  None


Socket timeout  timed out
Traceback (most recent call last):
  File "traceroute.py", line 42, in traceroute
    _, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

TTL:  9
 IP:  d
 Oras:  ICMP not received
 Regiune:  ICMP not received
 Tara:  ICMP not received


TTL:  10
 IP:  100.100.4.89
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  11
 IP:  100.100.82.68
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  12
 IP:  100.100.82.75
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  13
 IP:  100.100.10.72
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  14
 IP:  100.95.18.136
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  15
 IP:  100.65.12.10
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  16
 IP:  100.66.5.28
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  17
 IP:  100.66.7.172
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  18
 IP:  100.66.3.173
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  19
 IP:  100.66.0.29
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  20
 IP:  100.65.0.17
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  21
 IP:  100.64.0.123
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  22
 IP:  100.64.6.186
 Oras:  None
 Regiune:  None
 Tara:  None


TTL:  23
 IP:  100.64.22.129
 Oras:  None
 Regiune:  None
 Tara:  None


Socket timeout  timed out
Traceback (most recent call last):
  File "traceroute.py", line 42, in traceroute
    _, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

TTL:  24
 IP:  d
 Oras:  ICMP not received
 Regiune:  ICMP not received
 Tara:  ICMP not received


Socket timeout  timed out
Traceback (most recent call last):
  File "traceroute.py", line 42, in traceroute
    _, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

TTL:  25
 IP:  d
 Oras:  ICMP not received
```


## 3. Reliable UDP

### Emițător - mesaje de logging
Rulăm `docker-compose logs emitator` și punem rezultatul aici:
```
....
....
....
....
....
```


### Receptor - mesaje de logging
Rulăm `docker-compose logs receptor` și punem rezultatul aici:
```
....
....
....
....
....
```

# Soluție

## 1. Traceroute

Am folosit AWS pentru că în Windows nu îmi ajungeau ICMP-urile în Python.
Am implementat soluția iar aici este output-ul:

### Ruta către IP1 (cn.china.cn)
```
216.182.225.100 Ashburn, Virginia, United States
100.66.12.246 reserved range
100.66.14.202 reserved range
100.66.6.203 reserved range
100.66.5.55 reserved range
100.65.12.241 reserved range
52.93.28.229 Seattle, Washington, United States
100.100.8.72 reserved range
100.91.176.250 reserved range
100.91.160.74 reserved range
100.91.160.95 reserved range
100.91.198.94 reserved range
100.91.198.79 reserved range
Timeout timed out
52.93.129.248 Seattle, Washington, United States
54.239.44.56 Seattle, Washington, United States
100.91.5.53 reserved range
54.239.103.98 Seattle, Washington, United States
54.239.103.89 Seattle, Washington, United States
218.30.53.1 Beijing, Beijing, China
202.97.90.113 Beijing, Beijing, China
202.97.70.129 Beijing, Beijing, China
202.97.74.2 Beijing, Beijing, China
202.97.24.189 Beijing, Beijing, China
61.152.24.17 Shanghai, Shanghai, China
101.95.219.218 Shanghai, Shanghai, China
101.95.246.70 Shanghai, Shanghai, China
Request timed out. timed out
180.163.219.26 Shanghai, Shanghai, China
Request timed out. timed out
Request timed out. timed out
Request timed out. timed out
180.163.233.31 Shanghai, Shanghai, China
```

### Ruta către IP2 (digi24.ro)
```
216.182.226.132 Ashburn, Virginia, United States
100.66.9.80 reserved range
100.66.10.60 reserved range
100.66.6.61 reserved range
100.66.5.81 reserved range
100.65.13.1 reserved range
52.93.28.199 Seattle, Washington, United States
100.100.2.88 reserved range
69.174.15.253 Washington, District of Columbia, United States
213.200.113.198 Boca Raton, Florida, United States
87.119.98.154 Sofia, Sofia-Capital, Bulgaria
Request timed out. timed out
Request timed out. timed out
Request timed out. timed out
...
```

### Ruta către IP3 (abc.net.au)
```
216.182.238.175 Ashburn, Virginia, United States
100.65.80.112 reserved range
100.66.40.24 reserved range
100.66.43.154 reserved range
100.66.7.155 reserved range
100.66.5.13 reserved range
100.65.12.49 reserved range
52.93.28.221 Seattle, Washington, United States
100.100.2.72 reserved range
69.174.15.249 Washington, District of Columbia, United States
89.149.140.77 Neu Isenburg, Hesse, Germany
134.159.63.181 Singapore, , Singapore
202.40.149.178 Wanchai, Wan Chai, Hong Kong
202.84.137.102 Wanchai, Wan Chai, Hong Kong
203.50.13.89 Sydney, New South Wales, Australia
203.50.6.60 Sydney, New South Wales, Australia
203.50.11.97 Sydney, New South Wales, Australia
110.145.200.222 Sydney, New South Wales, Australia
Request timed out. timed out
Request timed out. timed out
Request timed out. timed out
...
```


## 2. Reliable UDP

### Emițător - mesaje de logging
Rulăm `docker-compose logs emitator` și punem rezultatul aici:
```
[LINE:47]# INFO     [2020-05-05 22:43:29,157]  [Connect] Ack Nr: "4077989984", Checksum: "56460", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,158]  [Send] Ack Nr: "4077991374", Checksum: "55070", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,159]  [Send] Ack Nr: "4077992764", Checksum: "53680", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,160]  [Send] Ack Nr: "4077994154", Checksum: "52290", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,160]  [Send] Ack Nr: "4077995544", Checksum: "50900", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,161]  [Send] Ack Nr: "4077996934", Checksum: "49510", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,162]  [Send] Ack Nr: "4077998324", Checksum: "48120", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,163]  [Send] Ack Nr: "4077999714", Checksum: "46730", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,164]  [Send] Ack Nr: "4078001104", Checksum: "45340", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,165]  [Send] Ack Nr: "4078002494", Checksum: "43950", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,166]  [Send] Ack Nr: "4078003884", Checksum: "42560", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,167]  [Send] Ack Nr: "4078005274", Checksum: "41170", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,168]  [Send] Ack Nr: "4078006664", Checksum: "39780", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,169]  [Send] Ack Nr: "4078008054", Checksum: "38390", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,170]  [Send] Ack Nr: "4078009444", Checksum: "37000", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,171]  [Send] Ack Nr: "4078010834", Checksum: "35610", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,171]  [Send] Ack Nr: "4078012224", Checksum: "34220", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,173]  [Send] Ack Nr: "4078013614", Checksum: "32830", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,174]  [Send] Ack Nr: "4078015004", Checksum: "31440", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,175]  [Send] Ack Nr: "4078016394", Checksum: "30050", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,176]  [Send] Ack Nr: "4078017784", Checksum: "28660", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,177]  [Send] Ack Nr: "4078019174", Checksum: "27270", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,178]  [Send] Ack Nr: "4078020564", Checksum: "25880", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,179]  [Send] Ack Nr: "4078021954", Checksum: "24490", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,180]  [Send] Ack Nr: "4078023344", Checksum: "23100", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,181]  [Send] Ack Nr: "4078024734", Checksum: "21710", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,182]  [Send] Ack Nr: "4078026124", Checksum: "20320", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,183]  [Send] Ack Nr: "4078027514", Checksum: "18930", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,184]  [Send] Ack Nr: "4078028904", Checksum: "17540", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,185]  [Send] Ack Nr: "4078030294", Checksum: "16150", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,186]  [Send] Ack Nr: "4078031684", Checksum: "14760", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,187]  [Send] Ack Nr: "4078033074", Checksum: "13370", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,188]  [Send] Ack Nr: "4078034464", Checksum: "11980", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,189]  [Send] Ack Nr: "4078035854", Checksum: "10590", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,189]  [Send] Ack Nr: "4078037244", Checksum: "9200", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,190]  [Send] Ack Nr: "4078038634", Checksum: "7810", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,191]  [Send] Ack Nr: "4078040024", Checksum: "6420", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,192]  [Send] Ack Nr: "4078041414", Checksum: "5030", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,193]  [Send] Ack Nr: "4078042804", Checksum: "3640", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,194]  [Send] Ack Nr: "4078044194", Checksum: "2250", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,195]  [Send] Ack Nr: "4078045584", Checksum: "860", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,196]  [Send] Ack Nr: "4078046974", Checksum: "65005", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,197]  [Send] Ack Nr: "4078048364", Checksum: "63615", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,198]  [Send] Ack Nr: "4078049754", Checksum: "62225", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,199]  [Send] Ack Nr: "4078051144", Checksum: "60835", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,200]  [Send] Ack Nr: "4078052534", Checksum: "59445", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,201]  [Send] Ack Nr: "4078053924", Checksum: "58055", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,201]  [Send] Ack Nr: "4078055314", Checksum: "56665", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,202]  [Send] Ack Nr: "4078056704", Checksum: "55275", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,203]  [Send] Ack Nr: "4078058094", Checksum: "53885", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,205]  [Send] Ack Nr: "4078059484", Checksum: "52495", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,205]  [Send] Ack Nr: "4078060874", Checksum: "51105", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,206]  [Send] Ack Nr: "4078062264", Checksum: "49715", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,207]  [Send] Ack Nr: "4078063654", Checksum: "48325", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,209]  [Send] Ack Nr: "4078065044", Checksum: "46935", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,210]  [Send] Ack Nr: "4078066434", Checksum: "45545", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,211]  [Send] Ack Nr: "4078067824", Checksum: "44155", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,212]  [Send] Ack Nr: "4078069214", Checksum: "42765", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,213]  [Send] Ack Nr: "4078070604", Checksum: "41375", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,213]  [Send] Ack Nr: "4078071994", Checksum: "39985", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,214]  [Send] Ack Nr: "4078073384", Checksum: "38595", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,216]  [Send] Ack Nr: "4078074774", Checksum: "37205", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,217]  [Send] Ack Nr: "4078076164", Checksum: "35815", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,217]  [Send] Ack Nr: "4078077554", Checksum: "34425", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,218]  [Send] Ack Nr: "4078078944", Checksum: "33035", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,219]  [Send] Ack Nr: "4078080334", Checksum: "31645", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,220]  [Send] Ack Nr: "4078081724", Checksum: "30255", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,221]  [Send] Ack Nr: "4078083114", Checksum: "28865", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,222]  [Send] Ack Nr: "4078084504", Checksum: "27475", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,223]  [Send] Ack Nr: "4078085894", Checksum: "26085", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,224]  [Send] Ack Nr: "4078087284", Checksum: "24695", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,225]  [Send] Ack Nr: "4078088674", Checksum: "23305", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,226]  [Send] Ack Nr: "4078090064", Checksum: "21915", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,227]  [Send] Ack Nr: "4078091454", Checksum: "20525", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,228]  [Send] Ack Nr: "4078092844", Checksum: "19135", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,229]  [Send] Ack Nr: "4078094234", Checksum: "17745", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,230]  [Send] Ack Nr: "4078095624", Checksum: "16355", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,231]  [Send] Ack Nr: "4078097014", Checksum: "14965", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,232]  [Send] Ack Nr: "4078098404", Checksum: "13575", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,233]  [Send] Ack Nr: "4078099794", Checksum: "12185", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,234]  [Send] Ack Nr: "4078101184", Checksum: "10795", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,235]  [Send] Ack Nr: "4078102574", Checksum: "9405", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,236]  [Send] Ack Nr: "4078103964", Checksum: "8015", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,237]  [Send] Ack Nr: "4078105354", Checksum: "6625", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,238]  [Send] Ack Nr: "4078106744", Checksum: "5235", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,239]  [Send] Ack Nr: "4078108134", Checksum: "3845", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,240]  [Send] Ack Nr: "4078109524", Checksum: "2455", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,241]  [Send] Ack Nr: "4078110914", Checksum: "1065", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,242]  [Send] Ack Nr: "4078112304", Checksum: "65210", Window: "1"
[LINE:115]# INFO     [2020-05-05 22:43:29,243]  [Send] Ack Nr: "4078113432", Checksum: "64082", Window: "1"
[LINE:81]# INFO     [2020-05-05 22:43:29,243]  [F] Ack Nr: "4078113433", Checksum: "64080", Window: "1"
```


### Receptor - mesaje de logging
Rulăm `docker-compose logs receptor` și punem rezultatul aici:
```
[LINE:37]# INFO     [2020-05-05 22:43:27,387]  Serverul a pornit pe 0.0.0.0 si portul 10000
[LINE:82]# INFO     [2020-05-05 22:43:29,157]  [S] Seq Nr: "4077989983", Checksum: "56460"
[LINE:82]# INFO     [2020-05-05 22:43:29,158]  [P] Seq Nr: "4077991374", Checksum: "55070"
[LINE:82]# INFO     [2020-05-05 22:43:29,159]  [P] Seq Nr: "4077992764", Checksum: "53680"
[LINE:82]# INFO     [2020-05-05 22:43:29,160]  [P] Seq Nr: "4077994154", Checksum: "52290"
[LINE:82]# INFO     [2020-05-05 22:43:29,160]  [P] Seq Nr: "4077995544", Checksum: "50900"
[LINE:82]# INFO     [2020-05-05 22:43:29,161]  [P] Seq Nr: "4077996934", Checksum: "49510"
[LINE:82]# INFO     [2020-05-05 22:43:29,162]  [P] Seq Nr: "4077998324", Checksum: "48120"
[LINE:82]# INFO     [2020-05-05 22:43:29,163]  [P] Seq Nr: "4077999714", Checksum: "46730"
[LINE:82]# INFO     [2020-05-05 22:43:29,164]  [P] Seq Nr: "4078001104", Checksum: "45340"
[LINE:82]# INFO     [2020-05-05 22:43:29,165]  [P] Seq Nr: "4078002494", Checksum: "43950"
[LINE:82]# INFO     [2020-05-05 22:43:29,166]  [P] Seq Nr: "4078003884", Checksum: "42560"
[LINE:82]# INFO     [2020-05-05 22:43:29,167]  [P] Seq Nr: "4078005274", Checksum: "41170"
[LINE:82]# INFO     [2020-05-05 22:43:29,168]  [P] Seq Nr: "4078006664", Checksum: "39780"
[LINE:82]# INFO     [2020-05-05 22:43:29,168]  [P] Seq Nr: "4078008054", Checksum: "38390"
[LINE:82]# INFO     [2020-05-05 22:43:29,169]  [P] Seq Nr: "4078009444", Checksum: "37000"
[LINE:82]# INFO     [2020-05-05 22:43:29,171]  [P] Seq Nr: "4078010834", Checksum: "35610"
[LINE:82]# INFO     [2020-05-05 22:43:29,171]  [P] Seq Nr: "4078012224", Checksum: "34220"
[LINE:82]# INFO     [2020-05-05 22:43:29,173]  [P] Seq Nr: "4078013614", Checksum: "32830"
[LINE:82]# INFO     [2020-05-05 22:43:29,174]  [P] Seq Nr: "4078015004", Checksum: "31440"
[LINE:82]# INFO     [2020-05-05 22:43:29,175]  [P] Seq Nr: "4078016394", Checksum: "30050"
[LINE:82]# INFO     [2020-05-05 22:43:29,176]  [P] Seq Nr: "4078017784", Checksum: "28660"
[LINE:82]# INFO     [2020-05-05 22:43:29,177]  [P] Seq Nr: "4078019174", Checksum: "27270"
[LINE:82]# INFO     [2020-05-05 22:43:29,178]  [P] Seq Nr: "4078020564", Checksum: "25880"
[LINE:82]# INFO     [2020-05-05 22:43:29,179]  [P] Seq Nr: "4078021954", Checksum: "24490"
[LINE:82]# INFO     [2020-05-05 22:43:29,180]  [P] Seq Nr: "4078023344", Checksum: "23100"
[LINE:82]# INFO     [2020-05-05 22:43:29,181]  [P] Seq Nr: "4078024734", Checksum: "21710"
[LINE:82]# INFO     [2020-05-05 22:43:29,182]  [P] Seq Nr: "4078026124", Checksum: "20320"
[LINE:82]# INFO     [2020-05-05 22:43:29,183]  [P] Seq Nr: "4078027514", Checksum: "18930"
[LINE:82]# INFO     [2020-05-05 22:43:29,184]  [P] Seq Nr: "4078028904", Checksum: "17540"
[LINE:82]# INFO     [2020-05-05 22:43:29,185]  [P] Seq Nr: "4078030294", Checksum: "16150"
[LINE:82]# INFO     [2020-05-05 22:43:29,186]  [P] Seq Nr: "4078031684", Checksum: "14760"
[LINE:82]# INFO     [2020-05-05 22:43:29,187]  [P] Seq Nr: "4078033074", Checksum: "13370"
[LINE:82]# INFO     [2020-05-05 22:43:29,188]  [P] Seq Nr: "4078034464", Checksum: "11980"
[LINE:82]# INFO     [2020-05-05 22:43:29,189]  [P] Seq Nr: "4078035854", Checksum: "10590"
[LINE:82]# INFO     [2020-05-05 22:43:29,189]  [P] Seq Nr: "4078037244", Checksum: "9200"
[LINE:82]# INFO     [2020-05-05 22:43:29,190]  [P] Seq Nr: "4078038634", Checksum: "7810"
[LINE:82]# INFO     [2020-05-05 22:43:29,191]  [P] Seq Nr: "4078040024", Checksum: "6420"
[LINE:82]# INFO     [2020-05-05 22:43:29,192]  [P] Seq Nr: "4078041414", Checksum: "5030"
[LINE:82]# INFO     [2020-05-05 22:43:29,193]  [P] Seq Nr: "4078042804", Checksum: "3640"
[LINE:82]# INFO     [2020-05-05 22:43:29,194]  [P] Seq Nr: "4078044194", Checksum: "2250"
[LINE:82]# INFO     [2020-05-05 22:43:29,195]  [P] Seq Nr: "4078045584", Checksum: "860"
[LINE:82]# INFO     [2020-05-05 22:43:29,196]  [P] Seq Nr: "4078046974", Checksum: "65005"
[LINE:82]# INFO     [2020-05-05 22:43:29,197]  [P] Seq Nr: "4078048364", Checksum: "63615"
[LINE:82]# INFO     [2020-05-05 22:43:29,198]  [P] Seq Nr: "4078049754", Checksum: "62225"
[LINE:82]# INFO     [2020-05-05 22:43:29,199]  [P] Seq Nr: "4078051144", Checksum: "60835"
[LINE:82]# INFO     [2020-05-05 22:43:29,200]  [P] Seq Nr: "4078052534", Checksum: "59445"
[LINE:82]# INFO     [2020-05-05 22:43:29,201]  [P] Seq Nr: "4078053924", Checksum: "58055"
[LINE:82]# INFO     [2020-05-05 22:43:29,201]  [P] Seq Nr: "4078055314", Checksum: "56665"
[LINE:82]# INFO     [2020-05-05 22:43:29,202]  [P] Seq Nr: "4078056704", Checksum: "55275"
[LINE:82]# INFO     [2020-05-05 22:43:29,203]  [P] Seq Nr: "4078058094", Checksum: "53885"
[LINE:82]# INFO     [2020-05-05 22:43:29,204]  [P] Seq Nr: "4078059484", Checksum: "52495"
[LINE:82]# INFO     [2020-05-05 22:43:29,205]  [P] Seq Nr: "4078060874", Checksum: "51105"
[LINE:82]# INFO     [2020-05-05 22:43:29,206]  [P] Seq Nr: "4078062264", Checksum: "49715"
[LINE:82]# INFO     [2020-05-05 22:43:29,207]  [P] Seq Nr: "4078063654", Checksum: "48325"
[LINE:82]# INFO     [2020-05-05 22:43:29,209]  [P] Seq Nr: "4078065044", Checksum: "46935"
[LINE:82]# INFO     [2020-05-05 22:43:29,210]  [P] Seq Nr: "4078066434", Checksum: "45545"
[LINE:82]# INFO     [2020-05-05 22:43:29,211]  [P] Seq Nr: "4078067824", Checksum: "44155"
[LINE:82]# INFO     [2020-05-05 22:43:29,212]  [P] Seq Nr: "4078069214", Checksum: "42765"
[LINE:82]# INFO     [2020-05-05 22:43:29,212]  [P] Seq Nr: "4078070604", Checksum: "41375"
[LINE:82]# INFO     [2020-05-05 22:43:29,213]  [P] Seq Nr: "4078071994", Checksum: "39985"
[LINE:82]# INFO     [2020-05-05 22:43:29,214]  [P] Seq Nr: "4078073384", Checksum: "38595"
[LINE:82]# INFO     [2020-05-05 22:43:29,216]  [P] Seq Nr: "4078074774", Checksum: "37205"
[LINE:82]# INFO     [2020-05-05 22:43:29,217]  [P] Seq Nr: "4078076164", Checksum: "35815"
[LINE:82]# INFO     [2020-05-05 22:43:29,217]  [P] Seq Nr: "4078077554", Checksum: "34425"
[LINE:82]# INFO     [2020-05-05 22:43:29,218]  [P] Seq Nr: "4078078944", Checksum: "33035"
[LINE:82]# INFO     [2020-05-05 22:43:29,219]  [P] Seq Nr: "4078080334", Checksum: "31645"
[LINE:82]# INFO     [2020-05-05 22:43:29,220]  [P] Seq Nr: "4078081724", Checksum: "30255"
[LINE:82]# INFO     [2020-05-05 22:43:29,221]  [P] Seq Nr: "4078083114", Checksum: "28865"
[LINE:82]# INFO     [2020-05-05 22:43:29,222]  [P] Seq Nr: "4078084504", Checksum: "27475"
[LINE:82]# INFO     [2020-05-05 22:43:29,223]  [P] Seq Nr: "4078085894", Checksum: "26085"
[LINE:82]# INFO     [2020-05-05 22:43:29,224]  [P] Seq Nr: "4078087284", Checksum: "24695"
[LINE:82]# INFO     [2020-05-05 22:43:29,225]  [P] Seq Nr: "4078088674", Checksum: "23305"
[LINE:82]# INFO     [2020-05-05 22:43:29,226]  [P] Seq Nr: "4078090064", Checksum: "21915"
[LINE:82]# INFO     [2020-05-05 22:43:29,227]  [P] Seq Nr: "4078091454", Checksum: "20525"
[LINE:82]# INFO     [2020-05-05 22:43:29,228]  [P] Seq Nr: "4078092844", Checksum: "19135"
[LINE:82]# INFO     [2020-05-05 22:43:29,229]  [P] Seq Nr: "4078094234", Checksum: "17745"
[LINE:82]# INFO     [2020-05-05 22:43:29,230]  [P] Seq Nr: "4078095624", Checksum: "16355"
[LINE:82]# INFO     [2020-05-05 22:43:29,231]  [P] Seq Nr: "4078097014", Checksum: "14965"
[LINE:82]# INFO     [2020-05-05 22:43:29,232]  [P] Seq Nr: "4078098404", Checksum: "13575"
[LINE:82]# INFO     [2020-05-05 22:43:29,233]  [P] Seq Nr: "4078099794", Checksum: "12185"
[LINE:82]# INFO     [2020-05-05 22:43:29,234]  [P] Seq Nr: "4078101184", Checksum: "10795"
[LINE:82]# INFO     [2020-05-05 22:43:29,235]  [P] Seq Nr: "4078102574", Checksum: "9405"
[LINE:82]# INFO     [2020-05-05 22:43:29,236]  [P] Seq Nr: "4078103964", Checksum: "8015"
[LINE:82]# INFO     [2020-05-05 22:43:29,237]  [P] Seq Nr: "4078105354", Checksum: "6625"
[LINE:82]# INFO     [2020-05-05 22:43:29,238]  [P] Seq Nr: "4078106744", Checksum: "5235"
[LINE:82]# INFO     [2020-05-05 22:43:29,239]  [P] Seq Nr: "4078108134", Checksum: "3845"
[LINE:82]# INFO     [2020-05-05 22:43:29,240]  [P] Seq Nr: "4078109524", Checksum: "2455"
[LINE:82]# INFO     [2020-05-05 22:43:29,241]  [P] Seq Nr: "4078110914", Checksum: "1065"
[LINE:82]# INFO     [2020-05-05 22:43:29,242]  [P] Seq Nr: "4078112304", Checksum: "65210"
[LINE:82]# INFO     [2020-05-05 22:43:29,243]  [P] Seq Nr: "4078113432", Checksum: "64082"
[LINE:82]# INFO     [2020-05-05 22:43:29,243]  [F] Seq Nr: "4078113432", Checksum: "64080"
```

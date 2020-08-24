import sys
import time
import speedtest
from datetime import datetime
from ping3 import ping, verbose_ping
from urllib.parse import urlparse



def test_servers(hosts):
    dt_string =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("="*20 +  dt_string + "="*20)
    for host in hosts:
        hostname = urlparse(host).hostname
        
        if hostname:
            tgt = hostname    
        else:
            tgt = host.strip()
        try:
            ping_ms = round(ping(tgt)*1000)
            print(tgt + "\t\t" + str(ping_ms)+"ms.")
        except:
            pass


def speedtest_server():
    try:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        print(res)
        return res["server"]["name"],res["download"]/1000.0/1000.0, res["upload"]/1000.0/1000.0, res["ping"]
    except:
        pass


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        content = f.readlines()
    while True:
        test_servers(content) 
        print(speedtest_server())
        time.sleep(10)
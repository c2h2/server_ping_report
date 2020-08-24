import sys

import speedtest
from ping3 import ping, verbose_ping
from urllib.parse import urlparse



def test_servers(hosts):
    for host in hosts:
        hostname = urlparse(host).hostname
        
        if hostname:
            tgt = hostname    
        else:
            tgt = host.strip()

        print(tgt + " " + str(ping(tgt)))
    print(speedtest_server())



def speedtest_server():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]



if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        content = f.readlines()
    print(content)
    test_servers(content)
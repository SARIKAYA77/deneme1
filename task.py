import requests
from bs4 import BeautifulSoup
sess = requests.Session()

http_proxy = "http://163.172.110.14:1457"

proxyDict = {
    "http":  http_proxy,
    "https": http_proxy
}


def step_one():
    headers = {
    'Host': 'anket.memurlar.net',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    params = {
        'primarykey': '0fc8dc49-3d61-e911-80e9-a0369f7d1486'
    }

    r = sess.get("https://anket.memurlar.net/anket/", headers=headers, params=params, proxies=proxyDict, verify=False)
                

    part1 = r.text.split('aspx?sessionguid=')[1]
    part2 = part1.split('"')
    sessionguid = part2[0]


    soup = BeautifulSoup(r.text, 'html.parser')
    options = '' 

    for i in soup.find_all('button'):
        if i.text == "Evet, önemli görüyorum":
            # print(i.text)
            # print(i.attrs)
            # print(i['name'])

            options = i['name']
    
    return step_two(sessionguid, options)


def step_two(sessionguid, options):
    headers = {
        "Host": "anket.memurlar.net",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Referer": "https://anket.memurlar.net/anket/?primarykey=0fc8dc49-3d61-e911-80e9-a0369f7d1486",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    data = {
        "options": options
    }

    params = {
        "sessionguid": sessionguid
    }


    r = sess.post("https://anket.memurlar.net/global/poll.vote.aspx",headers=headers, params=params, data=data, proxies=proxyDict, verify=False, allow_redirects=False)
                                    

    print(r.text)


    if "<a href=\"/global/poll.result.aspx?questionGUID" in r.text:
        result = "success"
    else:
        result = "fail"

    return result

def startTask():
    result = step_one()
    return result



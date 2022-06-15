import requests, threading, time, os # imports 
from colorama import Fore # for colors

os.system("cls") # clear the console

def slowprint(text):
    for char in text: # every char in text
        print(char, end='', flush=True) # flush is for printing without new line.
        time.sleep(0.02) # sleep .02 seconds for typing effect 

print(f"""
{Fore.BLUE}
                                                                                                                                                      
                                                                                                                                         
                            o--o  o--o   o-o o   o o   o       o-o o  o o--o   o-o o  o o--o o--o 
                            |   | |   | o   o \ /   \ /       /    |  | |     /    | /  |    |   |
                            O--o  O-Oo  |   |  O     O       O     O--O O-o  O     OO   O-o  O-Oo 
                            |     |  \  o   o / \    |        \    |  | |     \    | \  |    |  \ 
                            o     o   o  o-o o   o   o         o-o o  o o--o   o-o o  o o--o o   o
                                                                       
                                                                                                                                  
{Fore.WHITE}
- Proxy Checker v1.0
- Author: deTH           

Supported Proxy Types:

{Fore.BLUE}>{Fore.WHITE} http
{Fore.BLUE}>{Fore.WHITE} socks5
{Fore.BLUE}>{Fore.WHITE} socks4


""") # title


slowprint(f"[{Fore.GREEN}?{Fore.RESET}] Path to proxies: ") # this needs to be a txt file (you can see that it's using the slowprint function to imitate typing)
proxy_input = input() # ask for the input
slowprint(f"[{Fore.GREEN}?{Fore.RESET}] Timeout for proxies (in seconds): ") # if the proxy fails to respond in a that give time, it will be removed from the list
timeout = float(input()) # it needs to be a float so it can be like '1.4'

global work # it's global so it can be used in the add fucniton
work = 0 # every time there is a working proxy, 1 will be added to the work variable

with open(proxy_input, 'r') as f: # open the file
    proxy = f.readlines() # read the file
    proxy_count = len(proxy) # get how many proxies are in the file

def add(proxy, protocol): # add the proxy to the list
    global work # it's global so it can be used in the add fucniton
    work +=1 # add 1 to the work variable
    if protocol == "http": # if the protocol is http (protocol is given when the function is called via argument)
        with open("working_http.txt", 'a') as f: # open the file
            f.write(proxy) # write the proxy (given via fucntion argument) to the file
    elif protocol == "socks5": 
        with open("working_socks5.txt", 'a') as f:
            f.write(proxy)
    elif protocol == "socks4":
        with open("working_socks4.txt", 'a') as f:
            f.write(proxy)

def check(tryproxy): # check the proxy given in the argument 
    try: # firstly it tries with http protocoll
        r = requests.get("http://azenv.net/", proxies={"http": tryproxy, "https": tryproxy}, timeout=timeout) # send request to the proxy judge (azenv.net)
        add(tryproxy, "http") # write the proxy to the file
        print(f"{Fore.GREEN} >{Fore.RESET} {tryproxy}is working with https") # print the proxy that is working
    except: # if something occurs
        print(f"{Fore.RED} >{Fore.RESET} {tryproxy}is not working with https") # print out faliure message
    try: # then it tries with socks5 protocoll, then so on
        r = requests.get("http://azenv.net/", proxies={
            "http": f"socks5://{tryproxy}",
            "https": f"socks5://{tryproxy}"
            }, timeout=timeout)
        add(tryproxy, "socks5")
        print(f"{Fore.GREEN} >{Fore.RESET} {tryproxy}is working with socks5")
    except:
        print(f"{Fore.RED} >{Fore.RESET} {tryproxy}is not working with socks5")
    try:
        r = requests.get("http://azenv.net/", proxies={
            "http": f"socks4://{tryproxy}",
            "https": f"socks4://{tryproxy}"
            }, timeout=timeout)
        add(tryproxy, "socks4")
        print(f"{Fore.GREEN} >{Fore.RESET} {tryproxy} is working with socks4")
    except:
        print(f"{Fore.RED} >{Fore.RESET} {tryproxy} is not working with socks4")
 
start = time.time() # this is the time the checking starte

threads = [] # by default the threads list is empty

for tryproxy in proxy: # for each proxy in the list
    t = threading.Thread(target=check, args=(tryproxy,)) # create a thread for each proxy
    threads.append(t) # add the thread to the threads list
    t.start() # start the thread

os.system("cls") # clear the console
for t in threads: # for each thread in the threads list
    t.join() # join the thread

end = time.time() # this is the time the checking ended

os.system("cls") # clear the console

# print the results

# elapsed is calulated by the end time minus the start time
print(f"\n{Fore.GREEN} >{Fore.RESET} Done! Total checked proxies: {Fore.GREEN}{proxy_count}{Fore.RESET} Elapsed: {Fore.GREEN}{round(end - start, 0)}{Fore.RESET} seconds. Check rate: {Fore.GREEN}{round(proxy_count / (end - start), 2)}{Fore.RESET} proxies/second.\n Total working proxies: {Fore.GREEN}{work}{Fore.RESET} Working precent: {Fore.GREEN}{round(work / proxy_count * 100, 2)}%{Fore.RESET}.\n")

try:
    print(f"{Fore.BLUE} >{Fore.RESET} Press Control+C to exit")
    time.sleep(600) # 1 hour will be enough
    print(f"{Fore.BLUE} >{Fore.RESET} Timed out!") # if it timed out it will exit automatically
    os._exit(0) # exit with 0 code
except KeyboardInterrupt: # if contcol+c is pressed
    print(f"{Fore.RED} >{Fore.RESET} Exiting...") # print exit message
    os._exit(0) # exit with 0 code





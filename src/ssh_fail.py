import sys

users  = {}
ipl  = {}


def add_user(u):
    if u in users.keys():
        users[u] = users[u] + 1
    else:
        users[u] = 1

def add_ip(i):
    if(i in ipl.keys()):
        ipl[i] = ipl[i]+1
    else:
        ipl[i] = 1

for line in sys.stdin:
    l  = line.strip()
    FOUND = False
    try:
        pos = l.index("Failed password for invalid user")
        arr=  l[pos:].split(" ")
        user = arr[5]
        ip = arr[7]
        
        add_user(user)
        add_ip(ip)
        
        #print(user, ip)
        FOUND = True
    except:
        pass
    if(not FOUND):    
        try:
            pos = l.index("Failed password for")
            arr = l[pos:].split(" ")
            user = arr[3]
            ip = arr[5]
            add_user(user)
            add_ip(ip)
            #print(user, ip)
        except:
            #print("******Line skipped", l)
            pass

a = sorted_dict = dict(sorted(users.items(), key=lambda item: item[1], reverse=True))
b = sorted_dict = dict(sorted(ipl.items(), key=lambda item: item[1], reverse=True))
print(a)
print(b)

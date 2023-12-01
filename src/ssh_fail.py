import sys
import geocoder

users  = {}
ipl  = {}

def get_location_info(ip_address):
    try:
        # Specify the provider separately
        location = geocoder.ip(ip_address)
        location.geojson  # Force geocoding resolution

        print(f"IP: {ip_address}")
        print(f"City: {location.city}")
        #print(f"Region: {location.region}")
        print(f"Country: {location.country}")
        #print(f"Latitude: {location.latlng[0]}")
        #print(f"Longitude: {location.latlng[1]}")

    except Exception as e:
        print(f"An error occurred: {e}")


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

print("**************USERNAMES********************")
for u in a.keys():
    print ("- ", u, a[u])

print("""
.__                   __                                     
|  |__ _____    ____ |  | __ ___________                     
|  |  \\__  \ _/ ___\|  |/ // __ \_  __ \                    
|   Y  \/ __ \\  \___|    <\  ___/|  | \/                    
|___|  (____  /\___  >__|_ \\___  >__|                       
     \/     \/     \/     \/    \/                           
    .___               __                                    
  __| _/____   _______/  |________  ____ ___.__. ___________ 
 / __ |/ __ \ /  ___/\   __\_  __ \/  _ <   |  |/ __ \_  __ \\
/ /_/ \  ___/ \___ \  |  |  |  | \(  <_> )___  \  ___/|  | \/
\____ |\___  >____  > |__|  |__|   \____// ____|\___  >__|   
     \/    \/     \/                     \/         \/       

By Matteo Carrara, v1.0.0
""")      
for hacker in b.keys():
    #print(hacker, b[hacker])
    get_location_info(hacker)
    print("LOGIN:", b[hacker])
    print()
from BuycraftAPI import BuycraftAPI # import the BuycraftAPI.py file into here

# reads key from the token TXT file, and saves to a variable then passed to the main class (b = BuycraftAPI(buycraftToken))
with open('token.txt', 'r') as f:
    var = f.readlines()           
buycraftToken = var[0]            

# DO NOT DELETE, used to pass all methods through the API class, You will only need to use the b. function
# p instance is just used to make the following code look simpler
b = BuycraftAPI(buycraftToken)
p = b.listing()



def IDs(): # Run with b.IDs() <- IDs() function found in the main API Wrapper Class "BuycraftAPI"
    """Grab all packages in the store, output as Name : Package_ID """
    print(" --= Packages Overview =--")
    for i in range(len(p['categories'])): # Section and section ID
        print(p['categories'][i]['name'] + " : " + str(p['categories'][0]['id'])) 
    print("\n --= Items + ID\'s =--")
    for name in range(len(p['categories'])):
        for package in range(len(p['categories'][name]['packages'])):
            print(p['categories'][name]['packages'][package]['name'] + " : " + str(p['categories'][name]['packages'][package]['id']))

def serverInfo(): # Run with b.IDs()
    """Prints out some useful server info including name, domain, Account Key, and Server ID."""
    keys = ['name', 'domain']
    for key in keys:
        pprint.pprint(b.information()['account'][key])
    pprint.pprint("Account Key: " + str(b.information()['account']["id"]))
    pprint.pprint("Server ID: " + str(b.information()['server']['id']))

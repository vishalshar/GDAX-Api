import gdax


debug = False

###################
# LIVE API Access #
###################
secret = ''
key = ''
passphrase = ''


###################
# SANDBOX API Access #
###################
# secret = ''
# key = ''
# passphrase = ''


#############
# ENDPOINTS #
#############
sandBox_endpoint = "https://api-public.sandbox.gdax.com"
live_endpoint = "https://api.gdax.com"


#######################
# Authenticate Client #
#######################
auth_client = gdax.AuthenticatedClient(key, secret, passphrase)
# Use the sandbox API (requires a different set of API access credentials)
auth_client = gdax.AuthenticatedClient(key, secret, passphrase,api_url=live_endpoint)


# request = auth_client.get_fills(limit=1)
# print request[0] # Page 1 always present
# request[1] # Page 2+ present only if the data exists


#####################
## Account Details ##
#####################
account_info = auth_client.get_accounts()
for account in account_info:
    available = account['available']
    balance = account['balance']
    currency = account['currency']
    hold = account['hold']
    if debug:
        print available, balance, currency, hold


#######
#######
# BUY #
#######
#######

buy_type = ['limit', 'market', 'stop']
buy_product = '' # Product

##### LIMIT #####
buy_price = '0.0' # $
buy_size = '0.01'

##### MARKET #####
# buy_size = '0.01' # BTC
buy_funds = '1000' # $

##### STOP #####
buy_price = '0.001'
# buy_size = '0.001'
buy_funds = '0.001'

# API Call to buy
# auth_client.buy(price=buy_price, size=buy_size, product_id=buy_product, type = buy_type[0], funds = buy_funds)

########
########
# SELL #
########
########
sell_type = ['limit', 'market', 'stop']
sell_product = '' # Product

##### LIMIT #####
sell_price = '0.0' # $
sell_size = '0.01'

##### MARKET #####
# buy_size = '0.01' # BTC
sell_funds = '1000' # $

##### STOP #####
sell_price = '0.001'
sell_size = '0.001'
sell_funds = '0.001'


# API Call to sell
# auth_client.sell(price=sell_price, size=sell_size, product_id=sell_product, type = sell_type[0], funds = sell_funds)


##################
# ORDERS HISTORY #
##################
print auth_client.get_orders()


##########
##########
# CANCEL #
##########
##########
# auth_client.cancel_order('Order ID')
# auth_client.cancel_all(product='PRODUCT')



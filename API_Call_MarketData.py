import gdax

debug = False

#############
## Product ##
#############
product = 'BTC-USD'
print "Product ", product

##########################
## Connect Public Client #
##########################
public_client = gdax.PublicClient()
public_client.get_products()


################
## Order Book ##
################
# Get the order book at a specific level.
# Level 1 : Best bid and ask.
# Level 2 : Top 50 best bid and ask.
# Level 3 : All bids and asks
current_bid_ask = public_client.get_product_order_book(product, level=2)
current_bids = current_bid_ask['bids']
current_asks = current_bid_ask['asks']
if debug:
    print 'Level 2: bids and ask', len(current_bids), len(current_asks)


############
## TICKER ##
############
# Get the product ticker for a specific product.
product_ticker = public_client.get_product_ticker(product_id=product)
price = product_ticker['price']
size = product_ticker['size']
bid = product_ticker['bid']
ask = product_ticker['ask']
volume = product_ticker['volume']
time = product_ticker['time']
if debug:
    print product ," ticker: ",product_ticker


############
## TRADES ##
############
# Last 100 trades for the product
trades = public_client.get_product_trades(product_id=product)
for trade in trades:
    time = trade['time']
    price = trade['price']
    size = trade['size']
    side = trade['size'] # buy/sell
    if debug:
        print time, price, size, side
# print trades[0]



#####################
## Historic Trades ##
#####################
historic_trades = public_client.get_product_historic_rates(product)
for trade in historic_trades:
    time = trade[0]
    low = trade[1]
    high = trade[2]
    open = trade[3]
    close = trade[4]
    volume = trade[5]
    if debug:
        print time, low, high, open, close, volume
# Granularity time slice in seconds / NOT SUPPPORTED
# print public_client.get_product_historic_rates('ETH-USD', granularity=30)



################
## 24HR Stats ##
################
stats_24hr =  public_client.get_product_24hr_stats(product)
volume_24 = stats_24hr['volume']
last_24 = stats_24hr['last']
volume_30day = stats_24hr['volume_30day']
high_24hr = stats_24hr['high']
low_24hr = stats_24hr['low']
open_24hr = stats_24hr['open']
if debug:
    print volume_24, last_24, volume_30day, high_24hr, low_24hr, open_24hr


################
## Currencies ##
################
currencies = public_client.get_currencies()
for currency in currencies:
    min_size = currency['min_size']
    status = currency['status']
    message = currency['message']
    id = currency['id'] # Code ex. BTC, LTC
    name = currency['name'] # Name ex. bitcoin, litecoin
    if debug:
        print min_size, status, message, id, name


##########
## Time ##
##########
time = public_client.get_time()
time_iso = time['iso']
time_epoch = time['epoch']
if debug:
    print time_iso, time_epoch


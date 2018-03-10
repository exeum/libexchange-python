import os
import sys
import pprint

dir_name, _ = os.path.split(__file__)

sys.path.insert(0, "./%s/.." % dir_name)

from libexchange.types import Provider
from libexchange.providers import get_driver

d_driver = get_driver(Provider.BINANCE)

api_key = "%s_APIKEY" % Provider.BINANCE.upper()
secret_key = "%s_SECRET" % Provider.BINANCE.upper()

if api_key not in os.environ or secret_key not in os.environ:
    print("Please set %s and %s" % (api_key, secret_key))
    sys.exit(1)

driver = d_driver("api_key", "api_secret")

#print(driver.get_exchange_name())
#pprint.pprint(driver.get_symbols())
#pprint.pprint(driver.get_symbol_info("BNBBTC"))
#pprint.pprint(driver.get_ticker(symbol="ETHBTC"))
pprint.pprint(driver.get_all_tickers())

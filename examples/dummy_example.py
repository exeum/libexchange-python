import os
import sys

dir_name, _ = os.path.split(__file__)

sys.path.insert(0, "./%s/.." % dir_name)

from libexchange.types import Provider
from libexchange.providers import get_driver

d_driver = get_driver(Provider.DUMMY)

api_key = "%s_APIKEY" % Provider.DUMMY.upper()
secret_key = "%s_SECRET" % Provider.DUMMY.upper()

if api_key not in os.environ or secret_key not in os.environ:
    print("Please set %s and %s" % (api_key, secret_key))
    sys.exit(1)

driver = d_driver("api_key", "api_secret")

print(driver.get_exchange_name())


# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from libexchange.types import Provider
from libexchange.common.providers import get_exchange_driver
from libexchange.common.providers import set_exchange_driver

DRIVERS = {
        Provider.DUMMY: ("libexchange.drivers.dummy", "DummyDriver"),
        #Provider.TEST: ("libexchange.drivers.dummy", "TestDriver"),
        Provider.BINANCE: ("libexchange.drivers.binance", "BinanceDriver"),
        Provider.BITFINEX: ("libexchange.drivers.bitfinex", "Bitfinexriver"),
        Provider.GEMINI: ("libexchange.drivers.gemini", "GeminiDriver"),
        Provider.OKEX: ("libexchange.drivers.okex", "OkexDriver"),
}


def get_driver(provider):

    if provider not in DRIVERS:
        raise AttributeError("Providoer %s doesn't support" % (provider))

    return get_exchange_driver(drivers=DRIVERS, provider=provider)


def set_driver(provider, module, cls):

    if provider in DRIVERS:
        raise AttributeError("Providoer %s is already added" % (provider))

    return set_exchange_driver(drivers=DRIVERS, provider=provider, module=module, cls=cls)


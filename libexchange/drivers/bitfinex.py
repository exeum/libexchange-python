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

import sys
from libexchange.drivers.base import BaseDriver
from libexchange.drivers.base import print_package_install_info
try:
    from bitfinex.client import Client
except ImportError as e:
    print_package_install_info("bitfinex client", "bitfinex")
    sys.exit(1)

class BitfinexDriver(BaseDriver, Client):

    def __init__(self, api_key, api_secret):
        Client.__init__(self)

    def get_exchange_name(self):
        return "BITFINEX"

    def get_symbols(self):
        return self.symbols()

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

def get_exchange_driver(drivers, provider):

    if provider not in drivers:
        raise AttributeError("Providoer %s doesn't support" % (provider))

    mod_name, driver_name = drivers[provider]
    _mod = __import__(mod_name, globals(), locals(), [driver_name])

    return getattr(_mod, driver_name)


def set_exchange_driver(drviers, provider, module, cls):

    if provider in DRIVERS:
        raise AttributeError("Providoer %s is already added" % (provider))

    drivers[provider] = (module, cls)

    try:
        driver = get_exchage_driver(drivers, provider)
    except:
        exp = sys.exc_info()[1]
        drivers.pop(provider)
        raise exp

    return driver

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
from abc import *

ABC = ABCMeta("ABC", (object,), {})


class BaseDriver(ABC):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_exchange_name(self):
        pass


def print_package_install_info(client_name, pkg_name):
    print("%s is not installed. please install %s with 'pip%s install %s`" % (client_name, client_name, sys.version_info[0] if sys.version_info[0] > 2 else "", pkg_name))

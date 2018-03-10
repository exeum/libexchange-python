
from abc import *

ABC = ABCMeta("ABC", (object,), {})

class BaseDriver(ABC):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_exchange_name(self):
        pass

from logging import LoggerAdapter
import logging


class CustomAdapter(logging.LoggerAdapter):
    
    def process(self, msg, kwargs):
        customarg = kwargs.pop('customarg', self.extra['customarg'])
        return '[%s] %s' % (customarg, msg), kwargs

# get a standarad logger
logger_def = logging.getLogger('Demo Logging Adapter Class')

# in the formatter add contextual information key, in this case it's customargument
logging.basicConfig(format='%(asctime)s--%(message)s',level=logging.DEBUG)

# Pass the logger_def to CustomAdapter & assign value to customarg
adapter = CustomAdapter(logger_def, {'customarg': None})

try: 
    adapter.info("DOING SOMETHING STUPID", customarg="FULL MARKS FOR BEING EXTRA STUPID")
    1/0
except Exception as ex:    
    # replace value of customarg
    adapter.error("DID SOMETHING STUPID", customarg="NEVER DIVIDE BY ZERO")
from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

# lp = LogPrintMixin()
# lp.log_error('sdda')
# lp.log_success('dsadsa')

# lf = LogFileMixin()
# lf.log_success('dfasddasd')
# lf.log_error('jdsakda')

s1 = Smartphone('Galaxy')
s2 = Smartphone('Iphone')

s1.ligar()
s2.desligar()
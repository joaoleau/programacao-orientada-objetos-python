from pathlib import Path

LOG_DIR = Path(__file__).parent / 'log.txt'

# Abstracao

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente metodo log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

#Mixin -> uma classe com uma funcionalidade, outra classe pode implementa-la
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open (LOG_DIR, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('sdda')
    lp.log_success('dsadsa')

    lf = LogFileMixin()
    lf.log_success('dfasddasd')
    lf.log_error('jdsakda')



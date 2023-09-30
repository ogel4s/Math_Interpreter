import configparser


config = configparser.ConfigParser()
config.read('config.ini')


class ModeError(Exception):
    __module__ = Exception.__module__
    

class Trigonometry:

    PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    e  = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
    default_mode = config['DEFAULT']['mode']

    @classmethod
    def ln(self, x):
        n = 10 ** 6
        return n * ((x ** (1/n)) - 1)

    @classmethod
    def sin(self, theta, repetition=9, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        
        if 'j' in str(theta):

            if mode == 'rad':
                theta = (theta * 180) / self.PI
            
            result =  Trigonometry.sin(theta.real) * Trigonometry.cosh(theta.imag) + (0+1j) * Trigonometry.cos(theta.real) * Trigonometry.sinh(theta.imag)

            return result
            
        
        if mode == 'deg':
            if theta < 0:
                theta %= 360
            theta = (theta * self.PI) / 180
        
        if theta < 0:
            theta %= 2*self.PI
        
        theta %= 2*self.PI
        if theta > self.PI:
            theta -= 2*self.PI
            if theta < -self.PI/2:
                theta = -self.PI - theta
        elif theta > self.PI/2:
            theta = self.PI - theta

        result = 0
        denominator = 1
        for i in range(1, 2*repetition+2, 2):
            denominator *= i
            result += (theta ** i) / denominator
            denominator *= -(i + 1)
        
        return result

    @classmethod     
    def cos(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if 'j' in str(theta):

            if mode == 'rad':
                theta = (theta * 180) / self.PI
            
            result = self.cos(theta.real) * self.cosh(theta.imag) - (0+1j) * self.sin(theta.real) * self.sinh(theta.imag)

            return result

        if mode == 'deg':
            if theta < 0:
                theta %= 360
            theta = (theta * self.PI) / 180
        
        if theta < 0:
            theta %= 2*self.PI
        
        _sin = self.sin(theta=theta, mode='rad')
        
        return (1 - (_sin ** 2)) ** 0.5 if (self.PI / 2 >= theta >= 0) or (2*self.PI >= theta >= (3*self.PI)/2)  else -1 * ((1 - (_sin ** 2)) ** 0.5)
    
    @classmethod
    def tan(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _sin = self.sin(theta=theta, mode='rad')
        _cos = self.cos(theta=theta, mode='rad')

        return _sin / _cos if _cos != 0 else (float('inf') if _sin > 0 else float('-inf'))
    
    @classmethod
    def cot(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _tan = self.tan(theta=theta, mode='rad')
        
        return 1 / _tan if _tan != 0 else (float('inf') if str(_tan)[0] != '-' else float('-inf'))
    
    @classmethod
    def sec(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _cos = self.cos(theta=theta, mode='rad')

        return 1 / _cos if _cos != 0 else (float('inf') if theta == self.PI / 2 else float('-inf'))
    
    @classmethod
    def csc(self, theta, mode=default_mode):
        
        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _sin = self.sin(theta=theta, mode='rad')

        return 1 / _sin if _sin != 0 else (float('inf') if theta == 0 else float('-inf'))

    @classmethod
    def arcsin(self, x, a=0, N=10**5, mode=default_mode):

        def f(x):
            return 1 / (1 - x**2) ** 0.5
        
        value = 0
        value2 = 0
        for n in range(1 , N+1):
            value += f(a+((n - (1/2)) * ((x-a)/N)))
        value2 = ((x-a) / N) * value

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return value2

        value2 = (value2 * 180) / self.PI

        if 'j' in str(value2):
            return complex(value2)
        
        result = str(value2)[:str(value2).index('.')]

        for item in str(value2)[str(value2).index('.'):]:
            if item != '9':
                result += item
            else:
                result += item
                break
        
        rnd_check = len(str(result)[str(result).index('.')+1:])

        return round(float(result), rnd_check - 1)

    @classmethod
    def arccos(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return self.PI / 2 - self.arcsin(x, mode='rad')

        return 90 - self.arcsin(x)

    @classmethod
    def arctan(self, x, a=0, N=10**5, mode=default_mode):

        def f(x):
            return 1 / (1 + x**2)
        
        value = 0
        value2 = 0
        for n in range(1 , N+1):
            value += f(a+((n - (1/2)) * ((x-a)/N)))
        value2 = ((x-a) / N) * value

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return value2
        
        if str(value2) == 'nan':
            return value2

        value2 = (value2 * 180) / self.PI

        result = str(value2)[:str(value2).index('.')]

        for item in str(value2)[str(value2).index('.'):]:
            if item != '0':
                result += item
            else:
                result += item
                break
        
        rnd_check = len(str(result)[str(result).index('.')+1:])

        return round(float(result), rnd_check - 1)

    @classmethod
    def arccot(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
    
        if mode == 'rad':
            return self.arctan(1/x if x != 0 else (1/float('inf') if x > 0 else 1 /float('-inf')), mode='rad')
        
        return self.arctan(1/x if x != 0 else (1/float('inf') if x > 0 else 1 /float('-inf')))

    @classmethod
    def arcsec(self, x, mode=default_mode):
        
        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return self.arccos(1/x, mode='rad')
        
        return self.arccos(1/x)

    @classmethod
    def arccsc(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return self.arcsin(1/x, mode='rad')
        
        return self.arcsin(1/x)

    @classmethod
    def sinh(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if 'j' in str(theta):

            if mode == 'rad':
                theta = (theta * 180) / self.PI
            
            result = self.sinh(theta.real) * self.cos(theta.imag) + (0+1j) * self.cosh(theta.real) * self.sin(theta.imag)
            return result
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        return ((self.e ** theta) - (self.e ** (-theta))) / 2
    
    @classmethod
    def cosh(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if 'j' in str(theta):

            if mode == 'rad':
                theta = (theta * 180) / self.PI
            
            result = self.cosh(theta.real) * self.cos(theta.imag) + (0+1j) * self.sinh(theta.real) * self.sin(theta.imag)

            return result
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        return ((self.e ** theta) + (self.e ** (-theta))) / 2

    @classmethod
    def tanh(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _sinh = self.sinh(theta=theta, mode='rad')
        _cosh = self.cosh(theta=theta, mode='rad')

        return _sinh / _cosh if _cosh != 0 else (float('inf') if _sinh > 0 else float('-inf'))

    @classmethod
    def coth(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _tanh = self.tanh(theta=theta, mode='rad')

        return 1 / _tanh if _tanh != 0 else (float('inf') if str(_tanh)[0] != '-' else float('-inf'))

    @classmethod
    def sech(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _cosh = self.cosh(theta=theta, mode='rad')

        return 1 / _cosh if _cosh != 0 else (float('inf') if str(_cosh)[0] != '-' else float('-inf'))
    
    @classmethod
    def csch(self, theta, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'deg':
            theta = (theta * self.PI) / 180
        
        _sinh = self.sinh(theta=theta, mode='rad')

        return 1 / _sinh if _sinh != 0 else (float('inf') if str(_sinh)[0] != '-' else float('-inf'))
    
    @classmethod
    def arcsinh(self, x, a=0, N=10**5, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        value2 = self.ln(x + (x ** 2 + 1) ** 0.5)

        if mode == 'rad':
            return value2

        value2 = (value2 * 180) / self.PI

        if 'j' in str(value2):
            return complex(value2)
        
        result = str(value2)[:str(value2).index('.')]

        for item in str(value2)[str(value2).index('.'):]:
            if item != '0':
                result += item
            else:
                result += item
                break
        
        rnd_check = len(str(result)[str(result).index('.')+1:])

        return round(float(result), rnd_check - 1)
    
    @classmethod
    def arccosh(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')

        value2 = self.ln(x + (x ** 2 - 1) ** 0.5)

        if mode == 'rad':
            return value2

        value2 = (value2 * 180) / self.PI

        if 'j' in str(value2):
            return complex(value2)
        
        result = str(value2)[:str(value2).index('.')]

        for item in str(value2)[str(value2).index('.'):]:
            if item != '0':
                result += item
            else:
                result += item
                break
        
        rnd_check = len(str(result)[str(result).index('.')+1:])

        return round(float(result), rnd_check - 1)
    
    @classmethod
    def arctanh(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        value2 = 0.5 * (self.ln(1 + x) - self.ln(1-x))

        if mode == 'rad':
            return value2

        value2 = (value2 * 180) / self.PI

        if 'j' in str(value2):
            return complex(value2)
        
        result = str(value2)[:str(value2).index('.')]

        for item in str(value2)[str(value2).index('.'):]:
            if item != '9':
                result += item
            else:
                result += item
                break
        
        rnd_check = len(str(result)[str(result).index('.')+1:])

        return round(float(result), rnd_check - 1)

    @classmethod
    def arccoth(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
    
        if mode == 'rad':
            return self.arctanh(1/x if x != 0 else (1/float('inf') if x > 0 else 1 /float('-inf')), mode='rad')
        
        return self.arctanh(1/x if x != 0 else (1/float('inf') if x > 0 else 1 /float('-inf')))

    @classmethod
    def arcsech(self, x, mode=default_mode):
        
        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return self.arccosh(1/x, mode='rad')
        
        return self.arccosh(1/x)

    @classmethod
    def arccsch(self, x, mode=default_mode):

        if mode.lower() not in ['deg', 'rad']:
            raise ModeError(f'Invalid mode: {mode}')
        
        if mode == 'rad':
            return self.arcsinh(1/x, mode='rad')
        
        return self.arcsinh(1/x)





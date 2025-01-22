"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""

def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        
        return instances[the_class]
    
    print(instances)
    print(get_class)
    return get_class

@singleton
class AppSettings:
    def __init__(self):
        """ O inti será chamado todas as vezes que a classe for instanciada """
        self.tema = 'O tema escuro'
        self.font = '18px'

if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'''
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)




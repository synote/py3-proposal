"""
meta-despcriptor
"""
class Chainer(object):
    def __init__(self, methods, callback=None):
       self._methods = methods
       self._callback = callback
    def __get__(self, instance, klass):
       if instance is None:
           # only for instances
           return self
       results = []
       for method in self._methods:
           results.append(method(instance))
           if self._callback is not None:
               if not self._callback(instance,method,results):
                   break
       return results

class TextProcessor(object):
    def __init__(self, text):
        self.text = text
    def normalize(self):
        if isinstance(self.text, list):
            self.text = [t.lower()
                         for t in self.text]
        else:
            self.text = self.text.lower()
    def split(self):
        if not isinstance(self.text, list):
            self.text = self.text.split()
    def treshold(self):
        if not isinstance(self.text, list):
            if len(self.text) < 2:
                self.text = ''
        self.text = [w for w in self.text if len(w) > 2]

def logger(instance, method, results):
    print 'calling %s' % method.__name__
    return True

def add_sequence(name, sequence):
    """
    add_sequence('simple_clean', ('split', 'treshold'))
    """
    setattr(TextProcessor, name,Chainer(
        [getattr(TextProcessor, n) for n in sequence], logger))


if __name__ == '__main__':
    add_sequence('simple_clean', ('split', 'treshold'))
    my = TextProcessor(' My Taylor is rich')
    my.simple_clean
    print(my.text)

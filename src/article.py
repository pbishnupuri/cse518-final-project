
class Article(object):
  def __init__(self, bias):
    self.bias = bias

  def get_bias(self):
    return self.bias
  
  def __str__(self):
    return f'Article {self.bias}'

  def __repr__(self):
    return self.__str__()
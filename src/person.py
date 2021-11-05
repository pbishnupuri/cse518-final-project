# from article import Article

class Person(object):
  def __init__(self, stance, trust, empathy):
    self.stance = stance
    self.trust = trust
    self.empathy = empathy

  def update_func(self, article_bias):
    self.stance = self.stance + article_bias
  
  def get_range(self):
    return [max(-1, self.stance - self.empathy), min(self.stance + self.empathy, 1)]

  def simulate_paths(self, paths):
    starting_stance = self.stance
    all_stances = []
    for path in paths:
      current_stance = starting_stance
      for article in path:
        current_stance += article.get_bias()
      all_stances.append(current_stance)
    
    return all_stances

  
  def __str__(self):
    return f'Person {self.stance}'
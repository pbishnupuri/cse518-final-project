# from article import Article
import math
import numpy as np

class Person(object):
  def __init__(self, stance, empathy, inertia):
    self.stance = stance
    # self.trust = trust
    self.empathy = empathy
    self.inertia = inertia

  # def update_func(self, article_bias):
  #   # self.stance = self.stance + article_bias
  #   trust = math.exp(-(((article_bias - self.stance)**2)/(self.empathy)))
  #   self.stance = (((self.inertia * self.stance)+(self.stance * trust)) / (self.inertia * trust))
  def get_stance(self):
    return self.stance

  def update_func2(self, stance, article_bias):
    # self.stance = self.stance + article_bias
    trust = math.exp(-(((article_bias - self.stance)**2)/(self.empathy)))
    sig = np.sign(stance - article_bias)
    if trust >= .5:
          stance = stance + (1-self.inertia)*((1-self.inertia)*trust)*(article_bias - stance)
    else:
        stance = stance - (1-self.inertia)*((1-self.inertia)*trust)*(article_bias - stance)

    # stance = ((self.inertia * stance)+(stance * trust)) / (self.inertia + trust)
    # print(f'article bias: {article_bias}')
    # print(f'trust: {trust}')
    # print(f'stance: {stance}')
    # print('==================')
    return stance
  
  # def get_range(self):
  #   return [max(-1, self.stance - self.empathy), min(self.stance + self.empathy, 1)]

  def simulate_paths(self, paths):
    starting_stance = self.stance
    all_stances = []
    for path in paths:
      current_stance = starting_stance
      for article in path:
        current_stance =  self.update_func2(current_stance, article.get_bias())
      all_stances.append(current_stance)
    
    return all_stances

  
  def __str__(self):
    return f'Person {self.stance}'
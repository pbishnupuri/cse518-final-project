# This is where the programming is done
from person import Person
from article import Article
from helper import Helper
from graph import Graph
import numpy as np
import random
import math

def calculateStandardDevOpinion(persons):
  all_stances = []
  for person in persons:
    all_stances.append(person.get_stance())
  
  return (math.sqrt(np.var(all_stances)))

def calculateStandardDevOpinion2(opinions):
  all_stances = []
  for opinion in opinions:
    all_stances.append(opinion)
  
  return (math.sqrt(np.var(all_stances)))

def main():
  NUM_POP = 10
  NUM_ARTICLE = 5
  # Doing Normal Distribution
  mu, sigma = 0.5, (0.5/3) # mean and standard deviation
  inertia_values = np.random.normal(mu, sigma, NUM_POP).tolist()
  empathy_values = np.random.normal(mu, sigma, NUM_POP).tolist()
  
  population_values = np.random.normal(mu, sigma, NUM_POP)
  for i in range(len(population_values)):
    if population_values[i] < 0:
      population_values[i] = 0
    if population_values[i] > 1:
      population_values[i] = 1
  
  for i in range(len(inertia_values)):
    if inertia_values[i] < 0:
      inertia_values[i] = 0
    if inertia_values[i] > 1:
      inertia_values[i] = 1

  for i in range(len(empathy_values)):
    if empathy_values[i] < 0:
      empathy_values[i] = 0
    if empathy_values[i] > 1:
      empathy_values[i] = 1


  persons = []
  for opinion in population_values:
    inertia = random.choice(inertia_values)
    empathy = random.choice(empathy_values)
    persons.append(Person(opinion, inertia, empathy))
    inertia_values.remove(inertia)
    empathy_values.remove(empathy)

  # for person in persons:
  #   print(person)

  print(f'starting stdev: {calculateStandardDevOpinion(persons)}')

  article_values = np.random.normal(mu, sigma, NUM_ARTICLE).tolist()
  for i in range(len(article_values)):
    if article_values[i] < 0:
      article_values[i] = 0
    if article_values[i] > 1:
      article_values[i] = 1

  articles = []
  for opinion in article_values:
    articles.append(Article(opinion))

  # for article in articles:
  #   print(article)
  # helper = Helper()
  p1 = Person(.2, .9, .2)
  # # print(p1)
  # # helper.create_data("hello")

  # # Creating articles
  # # articles = [Article(.1), Article(.8), Article(.3), Article(.5)]
  graph = Graph(articles)
  # # print(graph.all_edges())
  # # print(graph.all_vertices())

  # # for vertice in graph:
  # #   print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

  all_paths = []
  for article in articles:
    for other in articles:
        paths = graph.find_all_paths(article, other)
        # print(paths)
        for path in paths:
          all_paths.append(path)

  final_stances = []
  for person in persons:
    all_stances = person.simulate_paths(all_paths)
    absolute_difference_function = lambda list_value : abs(list_value - .5)
    closest_value = min(all_stances, key=absolute_difference_function)
    final_stances.append(closest_value)
  # print(all_paths)
  # print(all_stances)
  print(f'ending stdev: {calculateStandardDevOpinion2(final_stances)}')
  # for i in range(len(all_paths)):
  #   print(all_paths[i])
  #   print(all_stances[i])
  #   print('==================')
  

if __name__ == "__main__":
  main()
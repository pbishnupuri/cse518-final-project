# This is where the programming is done
from person import Person
from article import Article
from helper import Helper
from graph import Graph
import numpy as np


def main():
  # mu, sigma = 0.5, (0.5/3) # mean and standard deviation
  # values = np.random.normal(mu, sigma, 100)
  # for i in range(len(values)):
  #   if values[i] < 0:
  #     values[i] = 0
  #   if values[i] > 1:
  #     values[i] = 1
  # print(max(values))
  # print(min(values))


  helper = Helper()
  p1 = Person(.2, .9, .2)
  # print(p1)
  # helper.create_data("hello")

  # Creating articles
  articles = [Article(.1), Article(.8), Article(.3), Article(.5)]
  graph = Graph(articles)
  # print(graph.all_edges())
  # print(graph.all_vertices())

  # for vertice in graph:
  #   print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

  all_paths = []
  for article in articles:
    for other in articles:
        paths = graph.find_all_paths(article, other)
        all_paths.append(paths[0])

  
  all_stances = p1.simulate_paths(all_paths)
  # print(all_paths)
  # print(all_stances)

  for i in range(len(all_paths)):
    print(all_paths[i])
    print(all_stances[i])
    print('==================')
  

if __name__ == "__main__":
  main()
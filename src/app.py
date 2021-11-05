# This is where the programming is done
from person import Person
from article import Article
from helper import Helper
from graph import Graph


def main():
  helper = Helper()
  # print("Hello World!")
  p1 = Person(.5, .02, .25)
  # print(p1)
  # helper.create_data("hello")


  # Creating articles
  articles = [Article(.5), Article(0), Article(-0.5)]
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

  print(all_paths)
  all_stances = p1.simulate_paths(all_paths)
  print(all_stances)
  

if __name__ == "__main__":
  main()
# Will probably split into multiple files and then have app.py put it all together

##### Graph
  # Characteristics of the graph
    # 1. Will be a complete graph
    # 2. Nodes represent a person's political stance
    # 3. Edges represent a news source 
    # 4. You can't go through the same edge twice

  # Characteristics of edge:
    # 1. Political stance [-1, 1] - use can use media bias chart [-1, 1]
    # 2. History of influence on persons? - like how has this media channel historically made left/right people feel
    #    (i.e CNN makes extreme right people go more right)

  # Characteristics of the algorithm - two options
  #######################################################
    ## Option 1 - Brute Force
      # 1. Go through the graph, keeping a history of each movement
      # 2. Loop through the history, find the one where the person's political stance is closest to 0
      # Pro - Will find minimum
      # Cons - Not scalable, takes up a lot of space, no way it's realistic for user to read all of those articles 
    ## Option 2 - Greedy Appraoch
      # 1. Start at a node, take the edge that gets your political stance closest to 0
      # 2. Repeat until out of nodes to take
      # Pros - Faster, more scable?, lowers political polarization, more realistic (since we can show person one article at a time)
      # Cons - Doesn't mind minumum

##### Person Object
  ## Characteristics each person will start with:
  # 1. Initial political stance [-1, 1]
  # 2. Adversity to news (i.e. showing liberal news will make them more conservative and vise versa) [-1, 1]? -- probably an equation
  # 3. Influence by news

  ## Characteristics of node (updated person, similar to initial person):
  # 1. Updated political stance [-1, 1]
  # 2. Updated adversity to news (i.e. showing liberal news will make them more conservative and vise versa) [-1, 1] -- probably an equation
  # 3. Updated influence by news


##### Project Design for Milestone 3
  # Do both!
  # 1. We can start with a small number of news channels, say 5-10
  # 2. Create the data
  # 3. Create 2 model persons (keep it easy) - 
  #    they will be relatively moderate, so they are susceptible to moderately leaning news (easy to mimic)
  # 4. Run person using both brute force and greedy
  # 5. Report data
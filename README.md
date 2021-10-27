# Mitigating Polarization via Strategic News Exposure
**Julia Smith, Pratyay Bishnupuri, Katherine Henry**

In this project, we plan to model human opinion dynamics by implementing a recommendation system that aims to mitigate polarization and converge political ideology towards a moderate stance. This project involves simulating a population that regularly interacts with some news source. To simulate such a population, we will create a dataset of agents that mimics human behavior. Each member of the population will begin with a political leaning indicated by [-1, 1] where -1 represents the far right and 1 represents far left. From there, we will generate a set of “articles,” i.e. interactions that agents will have in each iteration that will influence their political opinion. Each of these articles will have its own political influence rating denoted once again by [-1,1]. In each iteration, the agent will read an article or a set of articles. The influence from the article will either move the agent more to the left, to the right, or keep them at the same place depending on the (un)favorability of their interaction with the article. At the end of the iteration, the agent will receive a new political leaning floating value. The model will continue simulating these iterations until we have received a min(variance) of the population’s political leaning. This paper will also discuss the advantages and disadvantages of enforcing a depolarized ideology and the role fake news plays. A possible addition to this paper would be to incorporate a factor of skepticism when calculating opinion updates and determining which news article to recommend to consumers.

**Relevant Research**
- Opinion dynamics of skeptical agents: https://people.scs.carleton.ca/~alantsang/files/skeptical14.pdf
- Does Disagreement Mitigate Polarization? How Selective Exposure and Disagreement Affect Political Polarization: https://journals.sagepub.com/doi/full/10.1177/1077699015596328
- (Re)Design to Mitigate Political Polarization: Reflecting Habermas' ideal communication space in the United States of America and Finland: https://dl.acm.org/doi/abs/10.1145/3359243
- Modeling of the Public Opinion Polarization Process with the Considerations of Individual Heterogeneity and Dynamic Conformity
	https://www.mdpi.com/2227-7390/7/10/917
- Social Media, Network Heterogeneity, and Opinion Polarization
	https://academic.oup.com/joc/article-abstract/64/4/702/4086042
- Opinion dynamics: models, extensions and external effects
https://arxiv.org/pdf/1605.06326.pdf
---
### PROJECT MILESTONE 1
**LITERATURE REVIEW**
The subject of polarization across social networks has been explored with many different theoretical and empirical experiments, though much less attention has been placed on the dynamics of skepticism. Our literature review focused on understanding both classic and more novel trust-based models. “Opinion Dynamics: Models, Extensions, and External Effects” describes the backing theory and proofs of many different models of opinion dynamics, providing a better idea of how opinion dynamics works.  Other papers use theoretical simulations, similar to our proposed project; “Modeling of the Public Opinion Polarization Process with the Considerations of Individual Heterogeneity and Dynamic Conformity and Social Media” uses its own selection of mathematical models to research the spread of polarization (or depolarization) through a network. Finally, the paper “Opinion Dynamics of Skeptical Agents” provides general insight into how skepticism affects opinion dynamics. This paper also uses a proposed theoretical model to enrich models of polarization described in other theoretical papers. 

We will incorporate features from many of these papers in our model to mitigate polarization in a social network via media exposure including trust-based opinion dynamics and skepticism measurements. We aim to design a graph where nodes represent the political leaning of the given person in a network, each node will also have a skepticism value that will be dependent on the individual’s extremism (more polar opinions have higher skepticism values). Edges in this graph will have weights that represent the influence of an article towards the right or left. Given this influence and the opinion of a person at a certain time or step as well as their skepticism value, we will have a function that calculates the person’s opinion after passing through the given edge. Using this complete graph, we will produce an algorithm that outputs a series of edges to take such that opinions are depolarized after passing through the graph. This set of edges will represent the news articles that the individual will read to influence their political leaning. Furthermore, we hope to explore how various methods of media exposure affect polarized opinions and how strategic exposure can mitigate this behavior.

**GOALS**
1. Understand and have a meaningful discussion of the importance of social networks’ phenomena of polarization.
2. Use simulated experiments to concisely explain how people in social networks are depolarized based on trust dynamics.
3. Explore and understand a trust-based opinion spread using the Ishii-Kawahata model (https://arxiv.org/pdf/1812.11845.pdf) with experiments on different kinds of graphs.
4. Provide helpful recommendations to mitigate depolarization and/or induce polarization in networks, with respect to skepticism.
Understand how skepticism affects polarization.






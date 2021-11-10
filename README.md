# Pagerank

An AI to rank web pages by importance based on Google's pagerank algorithm. The AI uses two methods to calculate the rank of a page: random surfer model, iterative algorithm. 
The random surger model considers the behavior of a hypothetical surfer on the internet who clicks on links at random while the iterative algorithm implements a recursive 
mathematical expression to determine the page's rank.

```
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```

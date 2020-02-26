## Pandas practice script
import pandas as pd
import numpy as np
### read the movies dataset
movie = pd.read_csv("IMDB-Movie-Data.csv")
movie.head()
movie.tail(2)
map(lambda *a: a, range(3))

pandas 
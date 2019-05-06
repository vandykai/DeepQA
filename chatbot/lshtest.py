# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from lshash.lshash import LSHash
import numpy as np
lsh = LSHash(6, 8)
lsh.index([1,2,3,4,5,6,7,8])
lsh.index([2,3,4,5,6,7,8,9])
lsh.index([10,12,99,1,5,31,2,3])
print(lsh.query([1,2,3,4,5,6,7,7],num_results=4, distance_func="cosine"))

ai = [1,2,3,4,5,6,7,7]
bi = [1,2,3,4,5,6,7,8]
print(np.dot(ai,bi)/(np.linalg.norm(ai)*(np.linalg.norm(bi)))) #cosing距离
bi = [2,3,4,5,6,7,8,9]
print(np.dot(ai,bi)/(np.linalg.norm(ai)*(np.linalg.norm(bi)))) #cosing距离
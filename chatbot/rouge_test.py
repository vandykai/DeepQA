# -*- coding: utf-8 -*-

from rouge_score import rouge_n

reference = [[1,2,3,4], [1,2,4]]
candidate = [1,2,3,5]
score = rouge_n(reference, candidate, 1)
print(score)
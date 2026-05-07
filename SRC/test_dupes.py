from search import search_bert
from dupe_detector import get_dupes
from search import search_bert_extended

query = "Baccarat Rouge 540"

results = search_bert_extended(query)

print("\nALL RESULTS")
print(results)

print("\nDUPES")
print(get_dupes(results))
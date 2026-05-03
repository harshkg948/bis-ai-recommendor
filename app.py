# Simple keyword-based BIS recommender (NO libraries needed)

docs = [
    "IS 1786: High strength deformed steel bars for concrete reinforcement",
    "IS 456: Code of practice for plain and reinforced concrete",
    "IS 383: Specification for coarse and fine aggregates",
    "IS 269: Ordinary Portland Cement specification",
    "IS 8112: 43 grade OPC cement"
]

query = input("Enter product: ").lower()

# Simple matching
results = []
for doc in docs:
    score = sum(word in doc.lower() for word in query.split())
    results.append((score, doc))

# Sort by relevance
results.sort(reverse=True)

print("\nRecommended BIS Standards:\n")
for i in range(3):
    print(f"{i+1}. {results[i][1]}")

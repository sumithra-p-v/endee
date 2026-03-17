# Simple Search Project (No external libraries - Guaranteed to run)

# Documents
documents = [
    "Hello world! This is my first Endee project.",
    "Python is easy to learn.",
    "Vector databases are used in AI applications.",
    "Machine learning is the future."
]

# Search function
def search(query):
    results = []
    for doc in documents:
        if query.lower() in doc.lower():
            results.append(doc)
    return results

# Query
query = "hello"

# Get results
results = search(query)

# Print results
print("Search Query:", query)
print("Results:")
for r in results:
    print("-", r)
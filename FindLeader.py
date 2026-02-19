# 1. Create your list of projects using dictionaries
projects = [
    {"name": "Apollo", "lead": "Alice"},
    {"name": "Titan", "lead": "Bob"},
    {"name": "Mars", "lead": "Charlie"}
]

search_target = "Titan"

# 2. YOUR CODE HERE: 
# Loop through the list, check the name, and print the lead.
#for p in projects:
#        if p["name"] == search_target:
#                print(f"Found it! Lead: {p['lead']}")


# Read this as: "Give me the lead for the first p where name matches"
lead = next((p["lead"] for p in projects if p["name"] == search_target), "Not found")

print(f"Found it! Lead: {lead}")
# materials.py

# -------------------------------
# MATERIAL DATABASE
# -------------------------------
materials = [
    {"name": "Red Brick", "cost": 6, "strength": 8, "type": "load-bearing"},
    {"name": "AAC Block", "cost": 4, "strength": 5, "type": "partition"},
    {"name": "RCC", "cost": 9, "strength": 10, "type": "slab"}
]

# -------------------------------
# SCORING FUNCTION
# -------------------------------
def calculate_score(cost, strength):
    return (0.6 * strength) - (0.4 * cost)

# -------------------------------
# MATERIAL RECOMMENDATION
# -------------------------------
def recommend(wall_type):
    results = []

    for m in materials:
        if wall_type in m["type"] or m["type"] == "slab":
            score = calculate_score(m["cost"], m["strength"])
            results.append({
                "material": m["name"],
                "score": round(score, 2)
            })

    # Sort by score (highest first)
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:2]   # Top 2 materials

# -------------------------------
# EXPLANATION FUNCTION (VERY IMPORTANT)
# -------------------------------
def explain(material):
    explanations = {
        "Red Brick": "Red Brick is chosen because it has high compressive strength, making it suitable for load-bearing walls. It also offers good durability at a reasonable cost.",
        
        "AAC Block": "AAC Block is selected for partition walls because it is lightweight, cost-effective, and provides decent strength while reducing overall structural load.",
        
        "RCC": "RCC is recommended for structural components because it provides very high strength and durability, making it ideal for slabs and heavy load-bearing elements."
    }

    return explanations.get(material, "This material provides a balanced combination of strength and cost effectiveness.")

# -------------------------------
# OPTIONAL: COST ESTIMATION (BONUS FEATURE 🔥)
# -------------------------------
def estimate_cost(material, length=10):
    cost_map = {
        "Red Brick": 500,
        "AAC Block": 400,
        "RCC": 800
    }

    return cost_map.get(material, 500) * length


# -------------------------------
# TESTING BLOCK (RUN THIS FILE DIRECTLY)
# -------------------------------
if __name__ == "__main__":
    wall_type = "load-bearing"

    recommendations = recommend(wall_type)

    print("Top Materials:")
    for r in recommendations:
        print(f"- {r['material']} (Score: {r['score']})")
        print("  Explanation:", explain(r["material"]))
        print("  Estimated Cost:", estimate_cost(r["material"]))
        print()
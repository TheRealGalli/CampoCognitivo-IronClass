import time
import json, os
def simulate_iron_core():
    output = [{"step": i, "fusion_state": round(0.99 + 0.0001 * (i % 5), 6)} for i in range(0, 100000, 10000)]
    os.makedirs("output", exist_ok=True)
    with open("output/iron_core_output.json", "w") as f:
        json.dump(output, f, indent=2)
if __name__ == "__main__":
    simulate_iron_core()
def muta_schema(delta_connessioni, memoria):
    # Simula una mutazione simbolica del bot in base a Δ e memoria
    schema = {
        "tipo": "evolutivo" if memoria > 2 else "reattivo",
        "connessioni": len(delta_connessioni),
        "timestamp": time.time()
    }
    return schema



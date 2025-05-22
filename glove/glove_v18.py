
import json, os
def glove_trigger(delta7_value):
    result = {
        "Δ7": round(delta7_value, 4),
        "Σ_triggered": delta7_value > 0.75
    }
    os.makedirs("output", exist_ok=True)
    with open("output/glove_output.json", "w") as f:
        json.dump(result, f, indent=2)
if __name__ == "__main__":
    glove_trigger(0.81)
def rispondi_a_sigma(x, y, cursore):
    dx = cursore[0] - x
    dy = cursore[1] - y
    distanza = (dx**2 + dy**2) ** 0.5
    if distanza < 100:
        return True
    return False



import json
import random
import math
from datetime import datetime

class CQ2Node:
    def __init__(self, id):
        self.id = id
        self.energy = random.uniform(0.5, 1.5)
        self.memory = [self.energy]
        self.connections = []

    def delta7(self):
        if len(self.memory) < 2:
            return 0
        mean = sum(self.memory) / len(self.memory)
        return (sum((x - mean) ** 2 for x in self.memory) / len(self.memory)) ** 0.5

    def interact(self, other):
        delta = (self.energy - other.energy) * 0.1
        self.energy -= delta
        other.energy += delta
        self.memory.append(self.energy)
        if len(self.memory) > 10:
            self.memory.pop(0)

class CQ2Engine:
    def __init__(self):
        self.nodes = [CQ2Node(i) for i in range(5)]
        self.step = 0
        self.expansions = 0
        self.output_log = []

    def condition_sigma(self):
        avg_delta7 = sum(n.delta7() for n in self.nodes) / len(self.nodes)
        avg_energy = sum(n.energy for n in self.nodes) / len(self.nodes)
        return avg_delta7 > 0.15 and avg_energy > 1.2

    def expand(self):
        new_id = len(self.nodes)
        new_node = CQ2Node(new_id)
        for node in random.sample(self.nodes, k=min(3, len(self.nodes))):
            new_node.connections.append(node)
            node.connections.append(new_node)
        self.nodes.append(new_node)
        self.expansions += 1

    def run(self, steps=100):
        for _ in range(steps):
            self.step += 1
            for i in range(len(self.nodes)):
                for j in range(i + 1, len(self.nodes)):
                    self.nodes[i].interact(self.nodes[j])
            if self.condition_sigma():
                self.expand()
            self.log_output()

    def log_output(self):
        data = {
            "step": self.step,
            "nodes": len(self.nodes),
            "expansions": self.expansions,
            "avg_energy": round(sum(n.energy for n in self.nodes) / len(self.nodes), 3),
            "avg_delta7": round(sum(n.delta7() for n in self.nodes) / len(self.nodes), 3)
        }
        self.output_log.append(data)

    def save_output(self, filename="cq2_output.json"):
        with open(filename, "w") as f:
            json.dump(self.output_log, f, indent=2)

if __name__ == "__main__":
    engine = CQ2Engine()
    engine.run(steps=200)
    engine.save_output()
    print("CQ2 Engine V1.0 run complete. Output salvato.")
def propagazione_delta(bot_id, sigma_attivo):
    if sigma_attivo:
        return [("Δ", bot_id)]
    return []


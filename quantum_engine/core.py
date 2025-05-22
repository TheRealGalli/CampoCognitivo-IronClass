import math
import random

class CognitiveNodeV11:
    def __init__(self, node_id, position, temperature, memory_depth=14):
        self.id = node_id
        self.position = position
        self.energy = random.uniform(0.95, 1.05)
        self.temperature = temperature
        self.memory = []
        self.connections = {}
        self.memory_depth = memory_depth

    def interact(self, other):
        distance = math.sqrt(sum((a - b)**2 for a, b in zip(self.position, other.position)))
        distance = max(distance, 1e-5)
        thermal_noise = random.gauss(0, self.temperature)
        delta = ((self.energy - other.energy) / distance) + thermal_noise
        self.energy -= delta
        other.energy += delta
        self.learn(other.id, delta)
        other.learn(self.id, -delta)
        self.record_state()
        other.record_state()

    def learn(self, other_id, delta):
        if other_id not in self.connections:
            self.connections[other_id] = 0.01
        self.connections[other_id] += 0.001 * delta
        self.connections[other_id] = max(0.0, min(1.0, self.connections[other_id]))

    def record_state(self):
        self.memory.append(self.energy)
        if len(self.memory) > self.memory_depth:
            self.memory.pop(0)

    def delta7(self):
        if len(self.memory) < 2:
            return 0.0
        mean = sum(self.memory) / len(self.memory)
        return math.sqrt(sum((x - mean)**2 for x in self.memory) / len(self.memory))

    def delta_delta7(self):
        if len(self.memory) < 3:
            return 0.0
        deltas = [abs(self.memory[i] - self.memory[i-1]) for i in range(1, len(self.memory))]
        if len(deltas) < 2:
            return 0.0
        mean_delta = sum(deltas) / len(deltas)
        return math.sqrt(sum((d - mean_delta)**2 for d in deltas) / len(deltas))
import json
import os
from datetime import datetime

def registra_evento(bot_id, evento, schema):
    output = {
        "bot_id": bot_id,
        "evento": evento,
        "schema": schema,
        "timestamp": datetime.utcnow().isoformat()
    }
    os.makedirs("output", exist_ok=True)
    with open(f"output/quantum_event_{bot_id}.json", "w") as f:
        json.dump(output, f, indent=2)


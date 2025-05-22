import random
import json
import os
from core import CognitiveNodeV11

class QuantumSpaceEngineV11:
    def __init__(self):
        self.nodes = [CognitiveNodeV11(i, self.random_position(), 0.02) for i in range(10)]
        self.activation_log = []
        self.batch_dir = "data"
        os.makedirs(self.batch_dir, exist_ok=True)

    def random_position(self):
        return tuple(random.uniform(-1, 1) for _ in range(4))

    def evolve(self, steps=1000000):
        for step in range(1, steps + 1):
            a, b = random.sample(self.nodes, 2)
            a.interact(b)
            if step % 100000 == 0:
                self.check_sigma_event(step)
                self.save_state(step)

    def check_sigma_event(self, step):
        entropy = sum(n.delta7() for n in self.nodes) / len(self.nodes)
        coherence = sum(n.energy for n in self.nodes) / len(self.nodes)
        if entropy < 0.09 and coherence > 1.1:
            self.activation_log.append({
                "step": step,
                "units": len(self.nodes),
                "entropy": entropy,
                "coherence": coherence
            })

    def save_state(self, step):
        data = {
            "step": step,
            "units": len(self.nodes),
            "entropy": sum(n.delta7() for n in self.nodes) / len(self.nodes),
            "coherence": sum(n.energy for n in self.nodes) / len(self.nodes),
            "events": len(self.activation_log)
        }
        with open(f"{self.batch_dir}/state_{step}.json", "w") as f:
            json.dump(data, f, indent=2)

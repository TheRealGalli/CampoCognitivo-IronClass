
# INTELLECTUS V3 – Simulazione Cognitiva Reale (Iron-Class)
# Esegue i moduli reali: cq2, glove, core, iron_core, quantum_engine

import pygame
import random
import math
import json
import time
from datetime import datetime

from cq2 import engine as cq2_engine
from glove import glove_v18
from core import sim_v18
from iron_core import iron_core_simulation
from quantum_engine import core as quantum_core

LARGHEZZA, ALTEZZA = 800, 600
FPS = 60
NUM_BOT = 100
SOGLIA_SIGMA = 60

pygame.init()
screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("INTELLECTUS V3 – Campo Cognitivo™ Iron-Class")
clock = pygame.time.Clock()

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
GRIGIO = (50, 50, 50)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)
BLU = (0, 150, 255)
ARANCIO = (255, 165, 0)

eventi_sigma = []

class Bot:
    def __init__(self, x_range, iron=False):
        self.x = random.uniform(*x_range)
        self.y = random.uniform(0, ALTEZZA)
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.iron = iron
        self.id = random.randint(1000, 9999)
        self.memoria = 0
        self.delta_conn = []
        self.colore = VERDE if not iron else BLU

    def muovi(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > LARGHEZZA: self.dx *= -1
        if self.y < 0 or self.y > ALTEZZA: self.dy *= -1

    def percepisci_sigma(self, cursore):
        dist = math.hypot(self.x - cursore[0], self.y - cursore[1])
        if dist < SOGLIA_SIGMA:
            self.colore = ROSSO
            self.memoria += 1
            evento = {
                "bot_id": self.id,
                "timestamp": datetime.utcnow().isoformat(),
                "x": round(self.x, 2),
                "y": round(self.y, 2),
                "evento": "Σ-attivato",
                "memoria": self.memoria
            }
            eventi_sigma.append(evento)
            stato_glove = glove_v18.rispondi_a_sigma(self.x, self.y, cursore)
            self.delta_conn = cq2_engine.propagazione_delta(self.id, stato_glove)
            _ = iron_core_simulation.muta_schema(self.delta_conn, self.memoria)
            quantum_core.registra_evento(self.id, evento, self.delta_conn)
            self.dx, self.dy = -self.dy, self.dx
        else:
            self.colore = ARANCIO if self.memoria > 2 else (BLU if self.iron else VERDE)

    def disegna(self, surf):
        pygame.draw.circle(surf, self.colore, (int(self.x), int(self.y)), 4)
        for conn_id in self.delta_conn:
            pygame.draw.line(surf, (100, 100, 255), (int(self.x), int(self.y)),
                             (int(self.x + random.uniform(-30, 30)), int(self.y + random.uniform(-30, 30))), 1)

bot_classici = [Bot((0, LARGHEZZA//2), iron=False) for _ in range(NUM_BOT)]
bot_iron = [Bot((LARGHEZZA//2, LARGHEZZA), iron=True) for _ in range(NUM_BOT)]

def main():
    running = True
    while running:
        clock.tick(FPS)
        screen.fill(NERO)
        cursore = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.line(screen, GRIGIO, (LARGHEZZA//2, 0), (LARGHEZZA//2, ALTEZZA), 2)
        font = pygame.font.SysFont("monospace", 14)
        screen.blit(font.render("Campo Cognitivo™ Iron-Class – INTELLECTUS V3", True, BIANCO), (20, 10))

        for bot in bot_classici:
            bot.muovi()
            bot.disegna(screen)

        for bot in bot_iron:
            bot.muovi()
            bot.percepisci_sigma(cursore)
            bot.disegna(screen)

        pygame.display.flip()

    with open("output/proof_of_cognition_v3.json", "w") as f:
        json.dump(eventi_sigma, f, indent=2)

    pygame.quit()

if __name__ == "__main__":
    main()

import os
import sys
import numpy as np
import unittest
from datetime import datetime

# Importa il core pubblico autosufficiente
from core_pubblico_autosufficiente import funzione_pubblica, ModuloCore

# Import dei test (assumendo che siano in tests/test_core.py)
import tests.test_core as test_core
import tests.test_DeltaPsi_simulation as test_DeltaPsi_simulation

OUTPUT_DIR = "output"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def run_core_demo():
    # Demo: uso diretto del core
    valore = 3
    risultato = funzione_pubblica(valore)
    core_mod = ModuloCore(valore)
    elab = core_mod.elabora()
    with open(os.path.join(OUTPUT_DIR, "core_demo.txt"), "w") as f:
        f.write(f"funzione_pubblica({valore}) = {risultato}\n")
        f.write(f"ModuloCore({valore}).elabora() = {elab}\n")
    print(f"[INFO] Demo core completata. Output in {OUTPUT_DIR}/core_demo.txt")

def run_tests_and_save():
    # Esegue tutti i test e salva l'output
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(test_core))
    suite.addTests(loader.loadTestsFromModule(test_DeltaPsi_simulation))

    test_output_file = os.path.join(OUTPUT_DIR, "test_report.txt")
    with open(test_output_file, "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)

    print(f"[INFO] Test eseguiti. Risultati in {test_output_file}")

def run_simulation_and_save():
    # Esempio di simulazione: salva dati numerici
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    sim_data_file = os.path.join(OUTPUT_DIR, "simulation_data.csv")
    np.savetxt(sim_data_file, np.column_stack([x, y]), delimiter=",", header="x,y", comments="")
    print(f"[INFO] Dati simulazione salvati in {sim_data_file}")

def main():
    print("=== Main Launcher ===")
    print(f"Data/Ora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    run_core_demo()
    run_tests_and_save()
    run_simulation_and_save()
    print(f"[INFO] Tutto salvato in cartella {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
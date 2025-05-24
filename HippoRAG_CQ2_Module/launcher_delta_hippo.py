from hipporag_runner import run_hipporag

def main():
    question = "What is the function of the hippocampus?"
    response = run_hipporag(question)
    print("[Campo Cognitivo] Δ-Response:", response)

if __name__ == "__main__":
    main()

import json

def save_output(question, response):
    output = {
        "question": question,
        "response": response,
        "source": "HippoRAG Bridge Node"
    }
    with open("hipporag_output.json", "w") as f:
        json.dump(output, f, indent=2)

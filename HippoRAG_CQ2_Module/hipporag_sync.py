import requests

BASE_URL = "https://raw.githubusercontent.com/OSU-NLP-Group/HippoRAG/main/"
files_to_pull = ["hipporag_runner.py", "hipporag_pagerank.py", "hipporag_graph.py"]

def download_and_store():
    for file in files_to_pull:
        content = requests.get(BASE_URL + file).text
        with open(f"hipporag_mirror/{file}", "w") as f:
            f.write(content)

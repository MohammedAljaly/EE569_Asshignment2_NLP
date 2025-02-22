# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P0vRaH6mqLhVzXnqAelIC0u0AJiwtaM6
"""

import json
from sentence_transformers import SentenceTransformer
# download transform model
transformer_model = SentenceTransformer('distilbert-base-nli-mean-tokens')

# reading the data from the json file and convert it into vectors
with open('QA.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

embeddings = []
for section in ["FAQ", "Guide"]:
    if section in data:
        for item in data[section]:
            texts = [item.get("question"), item.get("answer"), item.get("title"), item.get("content")]
            for text in texts:
                if text and isinstance(text, str):
                    embedding = transformer_model.encode(text)
                    embeddings.append({"embedding": embedding.tolist(), "metadata": item, "text": text})

# saving vectors in json file
with open('embeddings.json', 'w', encoding='utf-8') as f:
    json.dump(embeddings, f, ensure_ascii=False, indent=4)
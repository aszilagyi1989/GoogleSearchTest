import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

load_dotenv()

file_path = "mol csoport integrált éves jelentés 2024.pdf" # nke-10k-2023.pdf
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))

print(f"{docs[0].page_content[:200]}\n")
print(f"{docs[0].metadata}\n")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, chunk_overlap = 200, add_start_index = True
)
all_splits = text_splitter.split_documents(docs)

print(len(all_splits))

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large")


vector_1 = embeddings.embed_query(all_splits[0].page_content)
vector_2 = embeddings.embed_query(all_splits[1].page_content)

assert len(vector_1) == len(vector_2)
print(f"\nGenerated vectors of length {len(vector_1)}\n")
print(f"\n{vector_1[:10]}\n")


vector_store = InMemoryVectorStore(embeddings)

ids = vector_store.add_documents(documents = all_splits)


results = vector_store.similarity_search(
    "Mennyi a cég 2024. évi értékesítés nettó árbevétele az eredménykimutatás szerint?" # How many distribution centers does Nike have in the US?
)
# print(f"\n{results[0]}\n")

for result in results:
  print(f"\n{result}\n")
  

results = vector_store.similarity_search_with_score("Mennyi a cég 2024. évi értékesítés nettó árbevétele az eredménykimutatás szerint?")
doc, score = results[0]
print(f"\nScore: {score}\n")
print(doc)



# results = vector_store.asimilarity_search("Mennyi a cég 2024. évi nettó árbevétele az eredménykimutatás szerint?") # When was Nike incorporated?
# # print(f"\n{results[0]}\n")
# 
# for result in results:
#   print(f"\n{result}\n")

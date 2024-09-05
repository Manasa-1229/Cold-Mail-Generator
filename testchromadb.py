import chromadb
client = chromadb.Client()
collection=client.create_collection(name="my_collection")
collection.add(
    documents=[
        "this is a new document",
        "this is my first chroma db doc",
        "this is doc is about Delhi",
        "this doc is about New York"
    ],
    ids= ['id1','id2','id3','id4']
)
all_docs =collection.get()

print(all_docs)

results= collection.query(
    query_texts = ['Query is about chole Bhature'],
    n_results =2
)

print(results)
import pymongo
import pandas as pd

conexao_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(conexao_string)

db = client["lis_promotora"]
collection = db["CPF_MATRICULA"]

tabela = pd.DataFrame(list(collection.find()))
tabela = tabela.drop(columns=["_id", "nome"])
print(tabela)

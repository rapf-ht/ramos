import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Carregar a base de dados
tabela = pd.read_csv("clientes.csv")

# 2. Pré-processamento: Transformar texto em números
# Criação de um dicionário de codificadores para poder reusar se necessário, 
# mas aqui usamos apenas um para simplificar
colunas_texto = ["profissao", "mix_credito", "comportamento_pagamento"]
codificador = LabelEncoder()

for coluna in colunas_texto:
    tabela[coluna] = codificador.fit_transform(tabela[coluna])

# 3. Separar dados de Treino e Teste
y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# 4. Criar e Treinar a Inteligência Artificial (Random Forest)
modelo = RandomForestClassifier()
modelo.fit(x_treino, y_treino)

# 5. Avaliar o modelo (Opcional, apenas para você ver a precisão no terminal)
previsao_teste = modelo.predict(x_teste)
acuracia = accuracy_score(y_teste, previsao_teste)
print(f"Modelo treinado com sucesso! Acurácia atual: {acuracia:.2%}")

# 6. Fazer previsões em novos clientes
try:
    novos_clientes = pd.read_csv("novos_clientes.csv")
    
    # Aplicar o mesmo tratamento (texto -> número) na nova tabela
    for coluna in colunas_texto:
        novos_clientes[coluna] = codificador.fit_transform(novos_clientes[coluna])
    
    previsao_novos = modelo.predict(novos_clientes)
    print("-" * 30)
    print("Previsão para os novos clientes:")
    print(previsao_novos)
    
except FileNotFoundError:
    print("Arquivo 'novos_clientes.csv' não encontrado para previsão.")
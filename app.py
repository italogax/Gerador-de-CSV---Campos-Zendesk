import pandas as pd

# Leitura do arquivo CSV
df_entrada = pd.read_csv('entrada.csv')
# Verificar as colunas do DataFrame
print(df_entrada.columns)
# Criar um novo DataFrame baseado no modelo
df_saida = pd.DataFrame()

df_saida['value'] = df_entrada['campo'] # Nome do campo é mantido no CSV de saída porem na coluna value
df_saida['tag'] = (
    df_entrada['tag_endereco'].str.replace(' ', '_').str.lower() + '_' +
    df_entrada['campo'].str.replace(' ', '').str.lower() # Cria a tag utilizando o nome do campo removendo os " " e tornando todas as letras minúsculas.
    )
df_saida['default'] = False # Configura o campo Default para sempre ser False.

#Salva o arquivo CSV de saida.
df_saida.to_csv('saida.csv', index=False)
print(df_saida)
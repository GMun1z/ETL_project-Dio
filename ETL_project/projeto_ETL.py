import pandas as pd
df = pd.read_csv('Vcto_NF.csv', encoding='utf-8',sep=';',index_col='ID')
df_ordenado_data_vencimento=df.sort_values('Data de Vencimento')
print(df_ordenado_data_vencimento)
df_ordenado_data_vencimento.to_csv('Vcto_NF_ordenado.csv')
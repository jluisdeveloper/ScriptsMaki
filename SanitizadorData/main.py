import pandas as pd

##############################################################################################
#              SANITIZADO DE CORREO ELECTRONICOS                                             #
##############################################################################################

df = pd.read_csv (r'/home/anarchist/Proyectos/Maki/Scripts Personalizados/SanitizadorData/Clientes_Email_Empresa.csv')

def is_nan(x):
  return (x != x)

df = df.drop(df[is_nan(df['Correo Electrónico'])].index)

for row in df.iterrows():
  text =row[1]['Correo Electrónico']
  x = text.split("@")
  if (x[0][len(x[0])-1].isalnum() == False):
    df = df.drop(row[0])

df.to_csv('Clientes_Email_Empresa_output.csv',index=False)


##############################################################################################
#              SANITIZADO DE NUMEROS DE CELULAR                                              #
##############################################################################################

df2 = pd.read_csv (r'/home/anarchist/Proyectos/Maki/Scripts Personalizados/SanitizadorData/Clientes_Telefonos_Empresa.csv')
df2 = df2.drop_duplicates(subset=['Celular'])
df2 = df2.drop(df2[is_nan(df2['Celular'])].index)

for row in df2.iterrows():
  aux = row[1]['Celular']
  aux = aux.replace(" ","")

  df2['Celular'] = df2['Celular'].replace(row[1]['Celular'],aux)

  if (aux[0] == "+"):
    aux = aux.replace("+51","")

  if (aux[0] != "9" or len(aux) != 9):    
    df2 = df2.drop(row[0])

df2.to_csv('Clientes_Telefonos_Empresa_output.csv',index=False)
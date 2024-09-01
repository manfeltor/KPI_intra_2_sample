import pandas as pd
import glob

pd.set_option('display.max_rows', None)
excel_data = r'C:\Users\ftorres\OneDrive - INTRALOG ARGENTINA S.A\kpi\dash_pr\TMS_por_meses\*.xlsx'

excel_files = glob.glob(excel_data)
df_inc = []
for file in excel_files:
    df = pd.read_excel(file)
    df_inc.append(df)

bdfin = pd.concat(df_inc, ignore_index=True)


date_columns = ['fechaCreacion', 'fechaColecta', 'fechaRecepcion', 'fechaDespacho', 'fechaEntrega']

for column in date_columns:
    bdfin[column] = bdfin[column].str[:10]

try:
    
    for i in date_columns:
        print(i)
        bdfin[i] = pd.to_datetime(bdfin[i])
        print(i, 'x')

except:

    pass
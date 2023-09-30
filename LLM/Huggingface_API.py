import requests
import pandas as pd



API_URL = "https://ip4ayzbgw1xd1wa4.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer CaEZyVTntOdJdqaXpaRKsXnIxUcPKwNPNKJOFKelBbbwjrqKqfPoUsBTglEZIvEOkyMcHiYapPvHzZpgoEHkRDRidPeMTMuEMHdhTojwkDffSaCZdQKMGUBlnCDyHOOH",
	"Content-Type": "application/json"
}

#import csv as df 
df=pd.read_csv('combined.csv')
#take strings from cells in content column

value = df.iloc[0, 6]

#prompt: ¿puede resumir este texto? (zusammenfassen, funktioniert der output? welche task? sumamrisation, question answering?)
#im for loop, in dem gleichen csv in der gleichen zeile in neuer Zelle antworten als df abspeichern 
#take strings from summary cell, 
#neuer prompt: übersetz das auf Deutsch, dann abspeichern
#weiterlaufen bis alle zusammengefasst sind 
#einstellungen ändern: temp runter, output länge lang

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "resumir este texto: Aunque dice que no tiene aliados políticos, ha recibido el coaval de los partidos Conservador, Liberal, Centro Democrático, Cambio Radical, movimiento de Salvación Nacional, Creemos, Verde Oxígeno y está pendiente de la firma con Colombia Justas Libres.Si llega a ser gobernador de Santander, ¿qué es lo primero que va a hacer en su administración?Lo primero que haría sería citar a los 87 alcaldes de la región para presentarles mi programa de seguridad, y que todos trabajamos alineados para recuperar la seguridad del departamento, la gente tiene miedo, zozobra, no quiere repetir lo de hace 20 años, tenemos un programa detallado de seguridad, sería la primera acción, la unión, para mostrar las líneas de acción, que vamos a invertir, que necesitamos de ellos y que sientan que hay un líder. ",
})

print(output)
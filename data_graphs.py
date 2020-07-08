import requests
import pandas as pd
from datetime import datetime 

def ISLAPool():
    sent = requests.get('https://api.bloxy.info/token/token_holders_list?token=0x3203d789bfdB222bfdd629B8de7C5Dc38e8241eC&key=ACCunOMWYpmCp&format=table').json()
    df = pd.DataFrame(sent)
    df.rename(columns={0:'Token Holder', 2:'Balance'}, inplace=True)
    df['Token Holder'] = df['Token Holder'].str[:5]
    df = df[['Token Holder', 'Balance']]
    df.to_csv('ISLAPool.csv', index=False)

def ISLAToken():
    sent = requests.get('https://api.bloxy.info/token/token_holders_list?token=0x697ef32b4a3f5a4c39de1cb7563f24ca7bfc5947&key=ACCunOMWYpmCp&format=table').json()
    df = pd.DataFrame(sent)
    df.rename(columns={0:'Token Holder', 2:'Balance'}, inplace=True)
    df['Token Holder'] = df['Token Holder'].str[:5]
    df = df[['Token Holder', 'Balance']]
    df.to_csv('ISLAToken.csv', index=False)

def main():
    ISLAPool()
    ISLAToken()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("run_log.txt","a")
    f.write("Ran at " + dt_string + "\n")
    f.close() 

if __name__ == '__main__':
    main()

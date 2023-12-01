import pandas as pd
import requests

r = requests.get(url="https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022"
                 ,params=None, verify=False)
tables = pd.read_html(r)
tables

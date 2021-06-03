import pandas as pd

tb = pd.read_csv('Resources/cities_dateconv.csv')

tb.to_html('table.html')

html_table = tb.to_html()
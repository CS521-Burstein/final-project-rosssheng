import pandas as pd
import matplotlib.pyplot as plt
CSV_URL = "https://github.com/bursteinalan/Data-Sets/raw/master/Fake%20News/news.csv"
df = pd.read_csv(CSV_URL)

# Downloading a data set
import requests
r = requests.get(CSV_URL, allow_redirects=True)
content = r.content
r.content.decode("utf-8")[:100]
file = 't.csv'
open(file, 'wb').write(content)

df_1 = df.groupby(['label'])['label'].count()
df_1
print(df_1.plot.bar)


from collections import Counter
import re
text = r.text
text = text.lower()
text = re.sub("[^\w ]", "", text)

words = text.split(" ")
count = Counter(words).most_common(20)
count



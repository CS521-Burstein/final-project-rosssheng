import pandas as pd
import matplotlib.pyplot as plt
import requests
CSV_URL = "https://github.com/bursteinalan/Data-Sets/raw/master/Fake%20News/news.csv"
df = pd.read_csv(CSV_URL)

data_frame = pd.DataFrame(df)



# Downloading a data set

#r = requests.get(CSV_URL, allow_redirects=True)
#content = r.content
#r.content.decode("utf-8")[:100]
#file = 't.csv'
#open(file, 'wb').write(content)

df_1 = df.groupby(['label'])['label'].count()

x = ['Fake', 'Real']
y = []
y.append(df_1[0])
y.append(df_1[1])

c = ['red', 'blue']


plt.bar(x, y, color=c)
plt.title("Total Number of Fake and Real News")
plt.xlabel("Fake/Real")
plt.ylabel("Number of fakes and reals")
plt.show()





#df_1.plot.bar




#from collections import Counter
#import re
#text = r.text
#text = text.lower()
#text = re.sub("[^\w ]", "", text)

#words = text.split(" ")
#count = Counter(words).most_common(20)

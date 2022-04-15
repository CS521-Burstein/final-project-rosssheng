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


df_fake =df.loc[df['label'] == "FAKE", ['text']]
df_fake['text'] = df_fake['text'].str.lower()
df_fake

df_fake["text_new"] = df_fake['text'].str.lower().str.replace('[^\w\s]','')
new_df_1 = df_fake.text_new.str.split(expand=True).stack().value_counts().reset_index()
new_df_1.columns = ['Word', 'Frequency']
new_df_1

x = []
y = []
y.append(new_df_1[0])
y.append(new_df_1[1])

plt.scatter.plot(x, y)
plt.title("The frequency of words for fake news")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()

df_real = df.loc[df['label'] == "REAL", ['text']]
df_real['text'] = df_real['text'].str.lower()
df_real

df_real["text_new"] = df_real['text'].str.lower().str.replace('[^\w\s]','')
new_df_2 = df_real.text_new.str.split(expand=True).stack().value_counts().reset_index()
new_df_2.columns = ['Word', 'Frequency']
new_df_2

x = []
y = []
y.append(new_df_2[0])
y.append(new_df_2[1])

plt.scatter.plot(x, y)
plt.title("The frequency of words for real news")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()

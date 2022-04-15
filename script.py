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

#plotting bar graph with total fake/real content 
plt.bar(x, y, color=c)
plt.title("Total Number of Fake and Real News")
plt.xlabel("Fake/Real")
plt.ylabel("Number of fakes and reals")
plt.show()
####################


#plotting bar graph with values counting keywords 

#counters for y axis values
counter_FTrump = 0
counter_TTrump = 0
                 
counter_FClinton = 0
counter_TClinton = 0

counter_FRepublican = 0
counter_TRepublican = 0

counter_FDemocrat = 0
counter_TDemocrat = 0

counter_FGOP = 0
counter_TGOP = 0

counter_FObama = 0
counter_TObama = 0



for i in range(6335):
    title = data_frame.loc[i,'title']
    label = data_frame.loc[i,'label'] 
    
    if 'Trump' in title and 'FAKE' in label:
        counter_FTrump += 1

    if 'Trump' in title and 'REAL' in label :
        counter_TTrump += 1

    if 'Hillary' in title and 'FAKE' in label:
        counter_FClinton += 1

    if 'Hillary' in title and 'REAL' in label:
        counter_TClinton += 1
        
    if 'Republican' in title and 'FAKE' in label:
        counter_FRepublican += 1
    if 'Republican' in title and 'REAL' in label:
        counter_TRepublican += 1
        
    if 'Democrat' in title and 'FAKE' in label:
        counter_FDemocrat += 1
    if 'Democrat' in title and 'REAL' in label:
        counter_TDemocrat += 1
    
    if 'GOP' in title and 'FAKE' in label:
        counter_FGOP += 1
    if 'GOP' in title and 'REAL' in label:
        counter_TGOP += 1

    if 'Obama' in title and 'FAKE' in label:
        counter_FObama += 1
    if 'Obama' in title and 'REAL' in label:
        counter_TObama += 1


x1 = ['FAKETrump','REALTRUMP', 'FAKEHillary','REALHillary', 'FAKERepublican','REALRepublican','FAKEDemocrat','REALDemocrat','FAKEGOP','REALGOP','FAKEObama','REALObama']
y1 = [counter_FTrump,counter_TTrump,counter_FClinton,counter_TClinton,counter_FRepublican,counter_TRepublican,counter_FDemocrat,counter_TDemocrat,counter_FGOP,counter_TGOP,counter_FObama,counter_TObama]


c = ['red','blue']

        
plt.bar(x1, y1, color=c)
plt.title("Read/Fake news according to a few select keywords")
plt.xlabel("Fake/Real")
plt.ylabel("Number of fakes and reals")
plt.show()
#####################################









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

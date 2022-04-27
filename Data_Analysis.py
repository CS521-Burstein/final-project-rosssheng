import script

df = script.df
data_frame = script.data_frame

# 1. Count the number of fake and real news
df_1 = df.groupby(['label'])['label'].count()

x1 = ['Fake', 'Real']
y1 = []
y1.append(df_1[0])
y1.append(df_1[1])

c = ['red', 'blue']

# 2. Make a bar graph for total number of fake and real news
plt.bar(x1, y1, color=c)
plt.title("Total Number of Fake and Real News")
plt.xlabel("Fake/Real")
plt.ylabel("Number of fakes and reals")
plt.show()


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

# Extract data for fake news from a label column
df_fake =df.loc[df['label'] == "FAKE", ['text']]
df_fake['text'] = df_fake['text'].str.lower()
df_fake


# Count word in the text of fake news
df_fake["text_new"] = df_fake['text'].str.lower().str.replace('[^\w\s]','')
new_df_1 = df_fake.text_new.str.split(expand=True).stack().value_counts().reset_index()
new_df_1.columns = ['Word', 'Frequency']
head_df_1 = new_df_1.head(20)
head_df_1

# Make a bar plot for the word frequency in the text of fake news
head_df_1.plot.barh(x="Word", y = "Frequency")

# Extract data for real news from a label column
df_real = df.loc[df['label'] == "REAL", ['text']]
df_real['text'] = df_real['text'].str.lower()
df_real

# Count word in the text of real news
df_real["text_new"] = df_real['text'].str.lower().str.replace('[^\w\s]','')
new_df_2 = df_real.text_new.str.split(expand=True).stack().value_counts().reset_index()
new_df_2.columns = ['Word', 'Frequency']
head_df_2 = new_df_2.head(20)
head_df_2

# Make a bar plot for the word frequency in the text of real news
head_df_2.plot.barh(x="Word", y = "Frequency")

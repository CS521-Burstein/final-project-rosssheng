# FAKE NEWS DETECTOR
CS521 Final Project: Ross Sheng and Futaba Kikuchi 

FILES INCLUDED AND AN EXPLANATION TO HOW TO REPRODUCE RESULTS:

script.ipynb:

	This is the script used to download the csv dataset. We use pandas to retrieve the information from the csv file and be put into a dataset where the news 'text' is a 
	column and the 'label' of whether it is real or fake is another column. 

Data_Analysis.ipynb
		
	This file was made so we would be able to perform our initial data analysis and look at the kind of data we were dealing with. 
	Made a bar graph that charts the total volume of fake and real news there are: We found that the total number is relatively the same, though off by about 100. 
	We also made another bar graph that graphs each real and each fake pieces of news made according to the keywords we looked up.
 	After analysis of this bar graph, we found that the words Trump, Hillary, and Obama had the most pieces of real and fake news made fabout them. 
	Additionally, it looks like there was an overwhelming amount of real news reported about trump, while fake news made about trump also was quite high.
	News about clinton and obama were also quite dominant in this graph. Another interesting observation is that there seems like there is a lot more 
	real news reported than in comparison to their fake news counterpart, however, news about hillary clinton seems to be the exception in this case. 
	Count a word in the text of fake news and real news and make a graph for word frequency. As we can see from the two graph, there is also no big difference between the 
	word frequency in the text of fake news and that of real news. So we should remove the word like "the", "and", "to" and so on and make the same graphs and compare them. 



Machine Learning Classifier and prediction model.ipynb
	
	This file was made so we could compare classifier models. We tried to implement the Multinominal Naive Bayes Classifier model in this file. 
	First, we import script to get the dataframe we created within our script file where we downloaded the dataset. In the second cell, we looked at the shate of the dataframe
	and dropped duplicates while checking to see if there were any missing values in the first cell. We looked at the head of the dataframe in the fourth cell, and labeled our 
	x and y variables in the fifth cell. We then split our data into train and test data after importing train_test_split from sklearn. With this, we can test our classifier to see
	how accurate it is after it is trained by our dataset. We then vectorize the text content with a TF-IDF vectorizer so that it could be read in by the classifier through natural language processing. 
	Lastly, we input the training data into our Multinominal NB classifier with classifier.fit(tfidf_train, y_train), and then try to see how accurate the classifier was when compared with the test data using 
	y_pred = classifier.predict(tfidf_test). The accuracy score is then shown with accuracy_score from sk metrics. 

machine learning 2.ipynb

	This file was made so we could compare classifeir models, and this file was chosen to be the main file where we would implement its classifier model to predict fake or real news. First, we imported script 
	to manipulate the dataset. Then we split the data into x and y variables, and split those variables to training and test sets with train_test_split. We then used tfidf vectorizer to vectorize the content for
	the classifier. After comparing the accuracy with the Multinominal NB classifier, we decided to go with this file to use for our extention. For our webapp, we implemented a pipeline so that new data can be vectorized
	and fed to the passive aggressive classifier to determine the correct fake or real value. The code below was used to serialize the trained classifier model to be read by our web application. The code below has to be run with a .py file since pickle dump file could not be created through Jupyter.
	with open('model.pkl', 'wb') as handle: 
		pickle.dump(pipeline, handle, protocol=pickle.HIGHEST_PROTOCOL)



fake_news_application.py

	This python file was made to complete our second extension where we would create a simple web application to upload URLs of articles and see if they are real or fake. This file implements flask modules to initialize the application and assign the template for the model of the application.
	We use index.html as a template for the application within main(). We then use pickle to open and read the model.pkl we created within machine learning 2.ipynb. Then with the predict method, we load the url through request,article,and newspaper modules that we imported. We parse the url contents,
	and use our classifier to predict whether the news article we have is either real or fake. 

templates

	Within this folder, we have templates for our index.html file and style guide created with CSS. the html file defines a simple title, URL input bar, and return values. The style file was taken online from: https://codepen.io/tecdysis/pen/BaagQwX though we don't understand why it didnt load with the 
	appropriate font and colors. 



DELIVERABLES:

4/15 Deliverable:


1. Made a bar graph that charts the total volume of fake and real news there are: We found that the total number is relatively the same, though off by about 100. 

2. We also made another bar graph that graphs each real and each fake pieces of news made according to the keywords we looked up.
 		After analysis of this bar graph, we found that the words Trump, Hillary, and Obama had the most pieces of real and fake news made fabout them. 
		Additionally, it looks like there was an overwhelming amount of real news reported about trump, while fake news made about trump also was quite high.
		News about clinton and obama were also quite dominant in this graph. Another interesting observation is that there seems like there is a lot more 
		real news reported than in comparison to their fake news counterpart, however, news about hillary clinton seems to be the exception in this case. 

3. Count a word in the text of fake news and real news and make a graph for word frequency. As we can see from the two graph, there is also no big difference between the 
		word frequency in the text of fake news and that of real news. So we should remove the word like "the", "and", "to" and so on and make the same graphs and compare them. 






4/27 Deliverable:
We first made adjustments to our submission based on the feedback including separating the download script with the data analysis.
To make sure we are both well versed in trying to understand how the Machine Learning and training/modeling data works, we decided to 
both do a version of trying to use a classifier model. 

Ross: I created the file Machine Learning Classifier and prediction model.ipynb, processed the data byb removing useless words from the data,
	converted strings to integer counts, split the data for training, and created/used a classifier model from sklearn and printed a classification 
	report as well as a few bar graphs to display. 

Futaba: I created the file 'machine learning 2'. It processes removing the non-required value, cleaning the data, dividing the data into 
	train and test set, classifying the data, comparing train data to test data, calculating the accuracy of predict value, and printing classification report.
# FAKE NEWS DETECTOR
CS521 Final Project: Ross Sheng and Futaba Kikuchi 

Script includes code to download csv data through pandas

4/15 Deliverable:


1. Made a bar graph that charts the total volume of fake and real news there are: We found that the total number is relatively the same, though off by about 100. 

2. We also made another bar graph that graphs each real and each fake pieces of news made according to the keywords we looked up.
 		After analysis of this bar graph, we found that the words Trump, Hillary, and Obama had the most pieces of real and fake news made fabout them. 
		Additionally, it looks like there was an overwhelming amount of real news reported about trump, while fake news made about trump also was quite high.
		News about clinton and obama were also quite dominant in this graph. Another interesting observation is that there seems like there is a lot more 
		real news reported than in comparison to their fake news counterpart, however, news about hillary clinton seems to be the exception in this case. 

3. Count a word in the text of fake news and real news and make a graph for word frequency. As we can see from the two graph, there is also no big difference between the word frequency in the text of fake news and that of real news. So we should remove the word like "the", "and", "to" and so on and make the same graphs and compare them. 






4/27 Deliverable:
We first made adjustments to our submission based on the feedback including separating the download script with the data analysis.
To make sure we are both well versed in trying to understand how the Machine Learning and training/modeling data works, we decided to 
both do a version of trying to use a classifier model. 

Ross: I created the file Machine Learning Classifier and prediction model.ipynb, processed the data byb removing useless words from the data,
	converted strings to integer counts, split the data for training, and created/used a classifier model from sklearn and printed a classification 
	report as well as a few bar graphs to display. 
# POCSummarization of Online Text Reviews

2020 Version
Release Date: March 18, 2020

----------------------------------------------------------------------------------------------------------------------

README CONTENTS

1.1 Introduction
1.2 Description
1.3 Code Explanation
1.4 Challenges Faced
1.5 Conclusion/Future Work

2.0 Sentiment_Analyzer.ipynb
2.1 JSON Files

----------------------------------------------------------------------------------------------------------------------

1.1 Introduction

Online reviews are seemingly growing by the increased e-commerce users. 
Many users rely on these online reviews in building up their opinion on the products that are being purchased.
More time needs to be invested by the user inorder to look through these giant set of reviews and to get a jist out of them.
Our attempt is to reduce this time of the user by providing an automated summary of all the reviews present on the product, 
thus making it easier for the user to arrive at a conclusion by just looking at one single review that our model generates.

----------------------------------------------------------------------------------------------------------------------

1.2 Description

We are using the data sets that we've build under DSCI-511 Term project by performing web-scrapping on www.91mobiles.com.
This website displays the user reviews from e-commerce giants Flipkart and Amazon on mobile phones and other electronic devices.
We have limited our scope to mobile phones and have built two JSON files one for each Flipkart and Amazon reviews respectively.

Building up on these data sets, in the current project under DSCI-521, we are trying to generate a summary of all the reviews without
missing out on the curucial information that the user provides. This will help saving the time from reading through all the reviews.

To achieve this, we are using the unsupervised LDA (Latent Dirichlet Allocation) model.
Below is the step by step process that we have followed.
	- Cleaning the data to remove special characters and emoticons
	- Tokenization of the reviews
	- Removal of stop-words and contractions
	- Performing Stemming and Lemmatization
	- Applying TF-IDF to convert words to vector
	- Above generated vectorized data can then be fed to the LDA model to generate the specified number of topics
	- NLTK Sentiment Vader helps assessing the polarity of the reviews
	- Bi-grams and Tri-grams are then being applied to the output from LDA model
	- Thus generating a review with the most important topics on both the 

----------------------------------------------------------------------------------------------------------------------
1.3 Code Explanation

Section - 1




----------------------------------------------------------------------------------------------------------------------

1.4 Challenges Faced and Overcomed


LDA model provided the output in terms of topics with words which has certain score.
But these were just single words and doesn't necessarily congratulate or
negate a particular feature of the phone as it's just a single word.

To overcome this situation, we have come across the idea of utilizing the Bi-grams and Tri-grams
to produce two and three word pairs for positive, negative and neutral polarities.
These pairs helped us in better understanding the feature that are actually positive, neutral and negative.
It also provided a compound score.

There is a chance that our input data might have been diluted by the Opinion Spam and if these reviews go unidentified,
then the final sentiment about a particular feature might change in an incorrect direction.

It has been assumed that all the reviews would be entirely in English language but that wasn't the case.
We could also observe slang words and emoticons in the reviews.
These slang words and emoticons are difficult to understand mainly because they can also be treated as a sarcastic comment.
We have currently filtered out all the special characters thus eliminating the complexity of involving emoticons.

Slang words in the reviews could be better evaluated had there been a dedicated embedding model that supported them.

----------------------------------------------------------------------------------------------------------------------

1.5 Conclusion/Future Work

We've used the unsupervised LDA as this fits the data we have. 
Futher enhancement can be done with either Labeled-LDA or Multi-Grain LDA.
But the limitations with the data set that we have is blocking us from implementing them. 
Reason being that the Labeled-LDA and Multi-Grain LDA needs the labels from input data and current data sets we have lack this.

By improving the input data sets we have, i.e. by including the labels which Labeled-LDA and Multi-Grain LDA utilises,
enhancements can be done to the model.

----------------------------------------------------------------------------------------------------------------------

2.0 Sentiment_Analyzer.ipynb

This is the jupyter notebook where we have all our code along with the description of what the code in each cell does.

----------------------------------------------------------------------------------------------------------------------

2.2 JSON Files

'91mobiles_final_data_flipkart.json' and '91mobiles_new_amazon_data.json' files provide the dictionary structure of the data that is being used as input.
These files consists of multi-layered dictionaries.


<end of file>




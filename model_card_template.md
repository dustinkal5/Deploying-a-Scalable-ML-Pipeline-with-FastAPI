# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model in use is a Logistic regression model that was trained on the 1994 census database

## Intended Use
Use of the model is to predict whether an individual makes over 50K a year based on different categories. Ex: age, occupation, & gender
Other uses is for UDacity's ml projects

## Training Data
Data in use is from 1994 Census database. In total has 15 columns 
## Evaluation Data

## Metrics
Utilizes Precision, Recall, & F1 metrics
The model itself was able to achieve Precision: 0.5974, Recall: 0.3408, & F1: 0.4340

## Ethical Considerations
The model does not consider bias between each individual such as current occupation, family history, or gender.

## Caveats and Recommendations
Further factors from those listed could lead to change how the individual is seen within the model itself
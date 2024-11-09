# **Housing Price Prediction Model**
This repository contains a machine learning model for predicting housing prices based on a variety of features. The model leverages historical  
data to capture trends and patterns, helping estimate property values accurately.  

## **Features**  
The dataset includes property attributes such as:  

- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude	Price

### **Approach**
**Data analysis** : Heatmap to check correlation between features and Histogram to check number of houses in a certain price range.
**Data Preprocessing** : California housing dataset provided by scikit-learn library , had no missing values or categorical data to be encoded
**Model Selection**: Tested Gradient Boosting (XGBoost)
**Evaluation** : Assessed using MAE,R² Score for accuracy.

#### **Getting Started**
Clone the repo and install dependencies.
This model serves as a tool for real estate investors, buyers, and sellers to make data-driven decisions. Contributions are welcome!

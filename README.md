# Linear Regression Model 

## Intro:

Hello guys, I will try to explain shortly about linear regression models. As far as there is many documentation of machine learning, here we are going to discuss about supervised model which has two types. linear regression is focused into numerical data and on the other hand, classification is related to categorical data.

A basic introduction of machine learning, we need to think how machine learn? ...


# **point 0:** How to explore the data?

# **point 1:** How to define the model? 

A linear regression model can be represented as a linear combination of features to represent a label. It is like a line with an slope ans intercep(bias).

y = a*x + b

In general, we can consider an hiperplane of n dimensions:

Y_pred = a1x1 +a2X2 + ... + an*Xn + b0

Where:

ai are the weights
Xi are the features
b0 is the bias.
In matriz format:

Y = A dot X

About the weigths, there are 2 concepts:

Slope is the measue of how steep is the data distributed on the plane.
Intercept(Bias) is like a default value of the label when there is no data. The default level of toxity.
As

# **point 2:** How to get the weights? How to define the algorithm?

A linear regression is a line which wants to fit in the best way all points. In this way, we need to set up an algorithm to find the weigths. There are many ways to set up this procedure, but here is the general way:

A basic algorithm:

- Input: points, a dataset of points
- Output: a line which passes close to the data,  a model which best fit the data
- Procedure:
    1. pick a model with random weigth and bias
    2. repeat many times: Adjust the weigths and bias to improve predictions
    3. return a model
    
At first look, we can said the weights are between [0.5, 1] and the bias between [3, 9]

# **point 3:** How to measure/evaluate if our algorithm is the best? How to get the best weigths?

To measure we need to know the diference about real value and predicted value

MAE
MSE
RMSE

# **point 5:** How to optimize the algorithm?


# **point 4:** How to use the model?

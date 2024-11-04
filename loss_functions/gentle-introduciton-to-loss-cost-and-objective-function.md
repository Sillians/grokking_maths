# A gentle introduciton to Loss, Cost and Objective Function

Most often, the terms `loss function`, `cost function` and the `objective function` are used interchangeably, and are key concepts in machine learning and optimization; despite this, they do have distinct definitions. 
There are nuanced differences in their context and application. This brief article tends to explain the core difference between the loss, cost, and objective functions in machine learning. Let's break them down;


## 1. **Loss Function**:
The loss function quantifies how much a model's prediction deviates from the ground truth for one particular object. In a simpler term, the loss function measures how well a single data point is predicted by the model.

- `Core Functionality:` It quantifies the difference between the actual value (label) and the predicted value for an individual sample. The aim is to calculate the error for a single observation. 
So, when we calculate loss, we do it for a single object in the training or test sets.

- `Example:` In a regression task, a common loss function is `Mean Squared Error (MSE)`, which measures the squared differences between the actual and predicted values. 

`Loss Function (Mean Squared Error for a single data point)`: 

```math
L(y, \hat{y}) = (y - \hat{y})^2 
```


`Case Scenario:`

You have a dataset with the actual price of a house and a predicted price from your model, which takes into account factors like:
- Square meters 
- Location
- Number of bedrooms

The model outputs the predicted house price, and you compare it to the actual price.

Actual price of the house (true label, y) = $500,000

Predicted price from the model $(\hat{y})$ = $480,000

Calculation:

$$
L(500,000, 480,000) = (500,000 - 480,000)^2 = (20,000)^2 = 400,000,000
$$

The loss for a single prediction is = 400,000,000


`Usage:` The loss function is applied to each data point during the model's training process.




## 2. **Cost Function**: 
The term cost is often used as synonymous with loss. However, there is a distinct difference between the two. The cost function represents the average (or sum) of the loss function over the entire training dataset. 
It measure's the model's error on a group of data, whereas the loss function deals with a single data instance. 

- `Core Functionality:` The cost function aggregates the errors from all individual data points, providing a single scalar value that indicates how well the model is performing overall on the dataset.

- `Example:` In a regression task using `Mean Squared Error` (MSE), the cost function would be the average of all individual squared errors.

`Cost Function (Mean Squared Error for the entire dataset)`: 

$$
\text{Cost}(Y, \hat{Y}) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 
$$


Let's extend the example above to demonstrate the cost function using `Mean Squared Error (MSE)` for multiple data points (houses). The cost function aggregates the loss across multiple predictions and provides a measure of how well the model is performing overall.

`Case Scenario`: 

Suppose you're predicting house prices for 3 different houses. The actual and predicted prices are as follows:

| House | Actual Price  | Predicted Price  |
|-------|---------------|------------------|
| 1     | $500,000      | $480,000         |
| 2     | $700,000      | $750,000         |
| 3     | $400,000      | $420,000         |


The cost function is the average of the squared differences between the actual and predicted values across all houses:

$$ 
\text{Cost}(Y, \hat{Y}) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 
$$

where;
- Y is the vector of actual house prices.
- $\hat{Y}$ is the vector of predicted house prices.
- 𝑛 is the number of houses (3 in this case).


Calculation:

$$
\text{Cost}(Y, \hat{Y}) = \frac{1}{3} \sum_{i=1}^{3} (y_i - \hat{y}_i)^2
$$

1. For House 1: 
   $$(500,000 - 480,000)^2 = 20,000^2 = 400,000,000$$
2. For House 2: 
   $$(700,000 - 750,000)^2 = (-50,000)^2 = 2,500,000,000$$
3. For House 3: 
   $$(400,000 - 420,000)^2 = (-20,000)^2 = 400,000,000$$

Final cost:

$$
\text{Cost}(Y, \hat{Y}) = \frac{1}{3} \left( 400,000,000 + 2,500,000,000 + 400,000,000 \right) = 1,100,000,000
$$


Therefore, the cost (or Mean Squared Error) for the model across all three houses is 1,100,000,000.


`Usage:` The cost function is used during training to evaluate the performance of the model and to optimize its parameters (weights) by minimizing the overall error.



## 3. **Objective Function**: 
The objective function refers to the general function that we want to optimize (either minimize or maximize) in a machine learning model or optimization problem.
While training a model, we minimize the cost (loss) over the training data. However, its low value isn't the only thing we should care about. The generalization capability is even more important since the model that works well only for the training data is not optimal in prediction. 
So, to avoid overfitting, we add a regularization term that penalizes the model's complexity.

- `Core Functionality:` In machine learning, the objective function is typically the combination of a cost function and a regularization term that helps prevent overfitting by penalizing large model weights. 
The objective function can be the cost function, but it can also include other factors like `regularization terms`. It defines the goal of the optimization process. 
That being said, the objective function is the one we optimize, i.e., whose value we want to either minimize or maximize. 


- `Example:` In regularized regression (e.g., Ridge regression), the objective function combines the cost function (MSE) with a regularization term to prevent overfitting. 


Objective Function (Regularized MSE for Ridge Regression): 

```math
\text{Objective} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2 
```


`Case Scenario`:

You're building a linear regression model to predict house prices. In this case, you not only want to minimize the error (MSE), but you also want to regularize the model to prevent overfitting by penalizing large weights.
Let's walk through an example using `Ridge Regression`, where the objective function combines the `Mean Squared Error (MSE)` with `L2 regularization`.

The objective function in Ridge Regression is: 

```math
\text{Objective} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2 
```

Where;
- $y_i$ is the actual house price for the `i-th` data point.
- $\hat{y}_i$ is the predicted house price.
- n is the total number of data points (houses).
- $w_j$ is the `𝑗-th` weight (parameter) of the model.
- $\lambda$ is the regularization parameter (controls the strength of regularization).
- _p_ is the number of features (e.g., square meters, number of bedrooms, etc.).


Now, Let’s assume:

- We have predictions for 3 houses, as in the previous example.
- The actual and predicted prices are the same as before.
- The model has 2 features: square meters and location.
- The weights for these features are $w_1$ = 500 and $w_2$ = 200.
- The regularization parameter $\lambda$ = 0.01.


| House | Actual Price  | Predicted Price  |
|-------|---------------|------------------|
| 1     | $500,000      | $480,000         |
| 2     | $700,000      | $750,000         |
| 3     | $400,000      | $420,000         |


`Step-by-Step Calculation:`

Calculate the MSE (Cost Function);
1. For House 1: 
   $$(500,000 - 480,000)^2 = 20,000^2 = 400,000,000$$
2. For House 2: 
   $$(700,000 - 750,000)^2 = (-50,000)^2 = 2,500,000,000$$
3. For House 3: 
   $$(400,000 - 420,000)^2 = (-20,000)^2 = 400,000,000$$

Total MSE = 
```math
\text{Cost}(Y, \hat{Y}) = \frac{1}{3} \left( 400,000,000 + 2,500,000,000 + 400,000,000 \right) = 1,100,000,000 
```

Calculate the L2 Regularization Term:  

$$ 
\lambda \sum_{j=1}^{p} w_j^2 = 0.01 \times (500^2 + 200^2) = 2,900 
$$

Calcualte the final Objective Function: 

$$ 
\text{Objective} = 1,100,000,000 + 2,900 = 1,100,002,900 
$$



#### A bit of explanation:

The `MSE` part is the same as the cost function, showing how much error the model makes on average.
The regularization term penalizes large weights, helping to prevent overfitting. The smaller the weights, the lower the penalty, helping the model generalize better to unseen data.


`Usage:` The objective function is what the optimization algorithm (e.g., gradient descent) tries to minimize (or maximize) during the model training process.



### You might care to take note of this:
All three functions are related to the model's performance, with the loss function providing per-instance error, the cost function summarizing the overall error, and the objective function being the broader goal to optimize during training. 


### Summary of Differences:
- Loss Function: Measures error for a single data point.
- Cost Function: Aggregates loss across all data points (i.e., average or sum of the loss).
- Objective Function: General function to optimize, which can be the cost function or the cost function combined with other terms (e.g., regularization).






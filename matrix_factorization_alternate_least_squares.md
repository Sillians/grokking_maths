# Matrix Factorization using Alternating Least Square(ALS)

A very common problem faced by internet companies is that of recommending new products to users in personalized settings (e.g. Amazon's product recommender system, and Netflix movie recommendations).
This can be formulated as a learning problem in which we are given the ratings that users have given certain items and are tasked with predicting their ratings for the rest of the items. 

## Introduction
In this post, I took a deep dive into matrix factorization using alternating least squares, or ALS for short. I was curious to understand the maths and 
algorithm behind collaborative filtering used in recommendation system, it's objective and how things work behind the fancy libraries we use to optimize the 
model or system.

Matrix Factorization using Alternating Least Squares (ALS) is a popular algorithm for building recommendation systems, especially collaborative filtering-based systems. 
Technically, it is a technique used in recommendation systems where we decompose a large matrx (typically a user-item interaction matrix) into two smaller matrices. 
These smaller matrices represent latent factors that describe patterns between users and items.

Consider the interaction matrix $R$ of size $n$ x $m$, where
- $n$ is the number of users.
- $m$ is the number of items.
- $R_{ui}$ is the rating or interaction for item $i$ by the user $u$. 

Matrix $R$ has many missing entries indicating unobserved ratings, and our task is to estimate these unobserved ratings.


## Matrix Factorization: Objective and ALS Algorithm on s Single Machine.
A popular approach for this is a `matrix factorization`, where we fix a relatively small number $k$ (e.g. $k \approx 10$), and summarize each user $u$ with a 
$k$ dimensional vector $x_u$, and each item $i$ with a $k$ dimensional vector $y_i$. These vectors are referred to as $factors$.

Matrix factorization seeks to decompose $R$ into two matrices:
- `User matrix` $X$ (size $n$ x $k$): Each row corresponds to a user, and each column represents a $k$ dimensional vector or latent factor, $x_u$.
- `Item matrix` $Y$ (size $m$ x $k$): Each row corresponds to the item, and each column represents a $k$ dimensional vector or latent factor, $y_i$.

Then, to predict user $u$'s rating for item $i$, we simply predict $r_{ui} \approx x^T_{u} y_i$. 

This can be put in matrix form: 
- Let $R_{ui}$ be the rating of user $u$ on item $i$,
- Let $x_1,...,x_n \in \mathbb{R}^k$ be the latent factors vector for the users, and 
- Let $y_1,...,y_m \in \mathbb{R}^k$ be the latent factors vector for the items.

Note: The value of $K$ (the number of latent factors) is much smaller than $n$ or $m$, making the problem computationally feasible.

The $k$ x $n$ user matrix $X$, and the $k$ x $m$ item matrix $Y$ are then defined or represented by:

$$ \
X = \begin{bmatrix} | & | & & | \\
x_1 & x_2 & \cdots & x_n \\
| & | & & |
\end{bmatrix}, \quad
Y = 
\begin{bmatrix}
| & | & & | \\
y_1 & y_2 & \cdots & y_m \\
| & | & & |
\end{bmatrix}
\ $$

Where:

- $X \in \mathbb{R}^{n \times k}$ is the matrix of user factors, with each column  $x_u$ being the latent factor vector for user $u$.
- $Y \in \mathbb{R}^{m \times k}$ is the matrix of item factors, with each column $y_i$ being the latent factor vector for item $i$.

### Here's a sample diagram that can help you understand this concept;
![A sample representation](https://github.com/Sillians/small-scale-recommendations-systems/raw/main/assets/user-item-latent-factor.png)


### Alternating Least Squares (ALS)
`ALS` is a technique used to solve matrix factorization problems when there are missing values, i.e., when the matrix $R$ is sparse. Instead of directly solving
for both matrices $X$ and $Y$ at the same time (which is computationally expensive), ALS alternates between solving for $X$ while keeping $Y$ fixed, and then
solving for $Y$ while keeping $X$ fixed.

- **Objective Function**

Our overall goal is then to estimate the complete ratings matrix $R \approx X^T Y$.
We can formulate this problem as an optimization problem in which we aim to minimize an `objective function` and find optimal $X$ and $Y$. In particular, 
we aim to minimize the least squares error of the observed ratings i.e., to minimize the error between the predicted and actual ratings (and regularize).


```math
min_{X, Y} \sum_{(u,i) \in R_{\text{observed}}} \left( (R_{ui} - x_u^T y_i)^2 \right) + \lambda \left( \sum_u \|x_u\|^2 + \sum_i \|y_i\|^2 \right)
```

Where:
- $R_{ui}$ is the observed rating for user $u$ and item $i$,
- $x_u \in \mathbb{R}^k$ is the latent factor vector for user $u$,
- $y_i \in \mathbb{R}^k$ is the latent factor vector for item $i$,
- $x_u^T y_i$ is the dot product between the user $u$'s latent factors and item $i$'s latent factors,
- $\lambda$ is the regularization parameter that penalizes the magnitude of the latent factors to prevent overfitting,
- $\|x_u\|^2$ and $\|y_i\|^2$ are the squared Euclidean norms of the user and item factor vectors, respectively.


Notice that this objective is non-convex (because of the $x_u^T y_i$ term); in fact it's `NP-hard` to optimize. Gradient descent can be used as an approximate
approach here, however it turns out to be slow and costs lots of iterations. Note however, that if we fix the set of variables $X$ and treat them as constants, then
the objective is a convex function of $Y$ and vice versa. 

Our approach will therefore be to
- Fix $Y$ and optimize $X$ using `least squares` (hence the name Alternating Least Squares), 
- then fix $X$ and optimize $Y$ using `least squares`, 
- and repeat until convergence (i.e., until the values of $X$ and $Y$ stop changing significantly). 

Therefore, for our objective function, the alternating least squares algorithm is as follows:

### ALS for Matrix Completion
`Initialize` $X,Y$, 

- `repeat`

#### User Latent Factors Update Formula:

for $u = 1...n$ do;

```math
x_u = \left( \sum_{r_{ui} \in R_u^*} y_i y_i^T + \lambda I_k \right)^{-1} \sum_{r_{ui} \in R_u^*} r_{ui} y_i 
```

Where:
- $R_u^*$ is the set of items rated by user $u$,
- $r_{ui}$ is the observed rating for user $u$ and item $i$,
- $y_i \in \mathbb{R}^k$ is the latent factor vector for item $i$,
- $\lambda$ is the regularization parameter,
- $I_k$ is the identity matrix of size $k \times k$,
- $x_u \in \mathbb{R}^k$ is the latent factor vector for user $u$.


`end for`
#### Item Latent Factors Update Formula:

for $i = 1...m$ do;


```math
y_i = \left( \sum_{r_{ui} \in R_i^*} x_u x_u^T + \lambda I_k \right)^{-1} \sum_{r_{ui} \in R_i^*} r_{ui} x_u
```


Where:
- $R_i^*$ is the set of users who rated item $i$,
- $r_{ui}$ is the observed rating from user $u$ for item $i$,
- $x_u \in \mathbb{R}^k$ is the latent factor vector for user $u$,
- $\lambda$ is the regularization parameter,
- $I_k$ is the identity matrix of size $k \times k$,
- $y_i \in \mathbb{R}^k$ is the latent factor vector for item $i$.

`end for`

`until convergence` i.e., until the error (difference between predicted and actual ratings) stops decreasing significantly. 

Once we've computed the matrices $X$ and $Y$, there are several ways to do prediction. The first is to simply predict $r_{ui} \approx x^T_{u} y_i$ for each 
user $u$ and item $i$. This approach will cost $O(nmk)$ if we'd like to estimate every user-item pair. However, this approach is prohibitively expensive for most
real-world datasets. 

A second (and more holistic) approach is to use the $x_u$ and $y_i$ as features in another learning algorithm, incorporating these features with others that are
relevant to the prediction task.


### Computational Cost
So, for a single machine we can analyze the computational cost of this algorithm. Updating each $r_u$ will cost $O(n_{u}K^2 + K^3)$ where $n_u$ is the number
of items rated by user $u$, and similarly updating each $y_i$ will cost $O(n_{i}K^2 + K^3)$ where $n_i$ is the number of users that have rated item $i$.

### Regularization and Overfitting
To prevent overfitting, a regularization term $\lambda$ was added to the objective function. This penalizes large values in the latent factor matrices $X$ and $Y$,
ensuring that the learned latent factors generalize well to unseen data.

### Advantages of ALS
- Scalability: ALS is highly parallel and works well with large datasets.
- Handles Sparsity: Can deal well with sparse matrices (many missing values), which are very common in recommendation systems.
- Simplicity: ALS approach is relatively simple to implement and understand.

### Drawbacks of ALS
- Cold Start Problem: Can't seem to handle new users or items well, since no prior interactions.
- Choice of Hyperparameters: The number of latent factors $k$, and regularization parameter $\lambda$, and the convergence threshold all need to be tuned carefully.

### Other methods for Matrix Factorization
There are other methods / approaches for matrix factorization, include:
- Sparse Subspace Embedding
- Stochastic Gradient Descent (SGD)
- Singular Value Decomposition (SVD)
- Generalized Low Rank Models
- Fast ALS


### References
- This is a very helpful paper by Yehuda Koren, Robert Bell and Chris Volinsky, AT&T Labs—Research (MATRIX FACTORIZATION TECHNIQUES FOR RECOMMENDER SYSTEMS) **[Recommender-Systems-Netflix](https://datajobs.com/data-science-repo/Recommender-Systems-%5BNetflix%5D.pdf)**
- CME 323: Distributed Algorithms and Optimization, Spring 2015, Instructor: Reza Zadeh, Databricks and Stanford. **[Matrix Completion via Alternating Least Square(ALS)](https://stanford.edu/~rezab/classes/cme323/S15/notes/lec14.pdf)**
- Probabilistic Matrix Factorization by Ruslan Salakhutdinov and Andriy Mnih. **[Probabilistic Matrix Factorization](https://proceedings.neurips.cc/paper_files/paper/2007/file/d7322ed717dedf1eb4e6e52a37ea7bcd-Paper.pdf)**


### Helpful videos
1. Recommendation Engines Using ALS in PySpark (MovieLens Dataset)

[![IMAGE ALT TEXT](http://img.youtube.com/vi/FgGjc5oabrA/0.jpg)](http://www.youtube.com/watch?v=FgGjc5oabrA "Recommendation Engines Using ALS in PySpark (MovieLens Dataset)")


2. Recommender Systems | ML-005 Lecture 16 | Stanford University

[![IMAGE ALT TEXT](http://img.youtube.com/vi/GIcuSNAAa4g/0.jpg)](http://www.youtube.com/watch?v=GIcuSNAAa4g-Y?t2255 "Recommender Systems | ML-005 Lecture 16 | Stanford University | Andrew Ng)")








































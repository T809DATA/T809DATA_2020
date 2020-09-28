# Linear Models for Regression

So far we have tried to *classify* flowers from the Iris dataset. Classification tasks assume that we have a set of *features* and a set of *class labels* that we would like our models to learn to predict.

Regression tasks don't assume categorical labels. In regression tasks we again have some set of *features* but the value we want to predict isn't a label anymore but some value from a continuous domain. Therefore the the output domain of the model is continuous.

You can for example imagine the quadratic equation

$$
    y = ax^2 + bx + c
$$

An example of a regression task might be to predict what $a, b, c$ are given a feature set of multiple $(x, y)$ values.

In this assignment we will be using a altered version of the Iris dataset were we have ditched the class label targets and replaced them with the last feature column (representing the pedal length of the flower). You can load this data with `tools.load_regression_iris`.

## Section 1
We are going to use the Gaussian basis functions to predict real valued target variables of our data.
$$
\phi_k(x) = \frac{1}{(2\pi)^{D/2}} \frac{1}{|\Sigma_k|^{1/2}} e^{-\frac{1}{2} (x-\mu_k)^T \Sigma_k^{-1} (x-\mu_k)}
$$

We control the shift of the basis function using the mean vector $\mu_k$  but we force all covariance matrices to be identical and diagonal $\Sigma_k = \sigma\mathbf{I}$ for all $k$ so $\sigma$ is the parameter that controls the width of all the basis functions (in all directions).

### Section 1.1
Create a function `mvn_basis(features, mu, sigma)` that applies the multivariate normal basis function on the set of features. You should use `scipy.stats.multivariate_normal` to create your multivariate gaussians.

Example inputs and outputs:

*Load the data*
```
X, t = load_regression_iris()
N, D = X.shape
```

We need to define how many basis functions we are going to use and determine the mean vectors that we are using. We also have to define the variance, `sigma`. We do this arbitrarily.

```
M, sigma, i = 10, 10, 0
mu = np.zeros((M, D))
while i < D:
    mmin = np.min(X[i, :])
    mmax = np.max(X[i, :])
    mu[:, i] = np.linspace(mmin, mmax, M)
    i += 1
fi = mvn_basis(X, mu, sigma)
```

*Output*
```
[[0.00081185 0.00100599 0.00119015 ... 0.00137739 0.00123433 0.00105608]
 [0.00095701 0.0011535  0.00132743 ... 0.0013378  0.00116613 0.00097051]
 [0.00099061 0.00118896 0.00136247 ... 0.00134443 0.00116697 0.00096711]
 ...
 [0.00022494 0.00033425 0.00047422 ... 0.00136119 0.00146281 0.0015009 ]
 [0.00022415 0.00033669 0.00048286 ... 0.00146273 0.00158896 0.001648  ]
 [0.00031179 0.00045031 0.00062097 ... 0.00154612 0.00161495 0.00161053]]
```

### Section 1.2

Plot the output of each basis function, using the same parameters as above, as a function of the features. You should plot all the outputs onto the same plot.

A single basis function output is shown below

![Single basis function](images/single_basis.png)


### Section 1.3

Create a function `max_likelihood_linreg(fi, targets, lam)` that estimates the maximum likelihood values for the linear regression model.

Example inputs and outputs:
```
fi = mvn_basis(X, mu, sigma) # same as before
lamda = 0.001
max_likelihood_linreg(fi, t, lamda)
```
*Output*:
```
[  3.04661879   8.98364452  17.87352659  29.86144389  44.59162487
  61.12887842  78.01047234  93.44289728 105.61212037 113.03406275]
```

### Section 1.4
Finally create a function `linear_model(features, mu, sigma, w)` that predicts targets given the weights from your `max_likelihood_linreg`, the basis functions, defined by `mu` and `sigma`, and the `features`.

Example inputs and outputs:

```
wml = max_likelihood_linreg(fi, t, lamda) # as before
linear_model(X, mu, sigma, wml)
```
*Output*:
```
[0.72174704 0.71462572 0.72048698 0.75382486 0.73161981 0.7494642
 0.7502493  0.74274217 0.73390818 0.73639504 0.71611075 0.77254612
 ...
 0.77988157 0.60555882 0.61733184 0.62902646 0.75304099 0.57770296
 0.61914859 0.64629346 0.67533913 0.67677248 0.72763469 0.76905279]
```

### Bonus
This is a completely open ended bonus section. You are free to test out the methods in the assignment on different datasets, change the models, change parameters, make visualizations, analyze the models, or anything you desire.

Upload a short PDF document with your experiments and results. Upload all your added code as well.
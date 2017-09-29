# replicability-analysis-NLP
This code implements the methods described in [(Dror et al., 2017)](https://arxiv.org/abs/1709.09500) for reporting replicability outcomes of an experiment that involves comparing two algorithms performance on multiple datasets. The implementation includes the **Bonferroni** and **Fisher** tests for counting the number of datasets for which one algorithm was significantly better than the other, and the **Holm** procedure for identifying  these datasets (or some of them). 

## Getting Started 

### Input
A list of p-values from the comparisons of both algorithms on multiple datasets. 
A single p-value for each dataset.

### Running the tests
1. Write down the list of p-values with comma separating between the p-values.
2. Write down the desired significance level (alpha)
2. Choose the desired test:
* **B** for Bonferroni if the datasets are dependent.
* **F** for Fisher if the datasets are independent.

### Example
```
Enter p-values :
0.168,0.297,0.357,0.019,0.218,0.001
Enter significance level: 
0.05
Enter p-value combination method (B for Bonferroni, F for Fisher):
B
k estimator is:
Rejections list according to Holm procedure:
```



import sys
import numpy as np
from scipy import stats

### find_k_estimator(pvalues, alpha, method)
## This function calculates the estimator for k according to the method for combining the p-values given as input.
## Input:
    # pvals - list of p-values.
    # alpha - significance level.
    # method - 'B' for Bonferroni  or 'F' for Fisher.
## Output:
    # k_hat - estimator of k calculated according to method.
def find_k_estimator(pvalues, alpha, method ='B'):
    n = len(pvalues)
    pc_vec = [1]*n
    k_hat = 0
    pvalues = sorted(pvalues, reverse = True)
    for u in range(0,n):
        if (u == 0):
            pc_vec[u] = calc_partial_cunjunction(pvalues, u+1, method)
        else:
            pc_vec[u] = max(calc_partial_cunjunction(pvalues, u+1, method), pc_vec[u - 1])
    k_hat = len([i for i in pc_vec if i<=alpha])
    return k_hat

### Holm(pvalues, alpha)
## This function applies the Holm procedure to determine the rejections list
## Input:
    # pvals - list of p-values.
    # alpha - significance level.
## Output:
    # list of indeces of rejected null hypotheses. The rejected hypotheses are the hatk_Bonf. smallest p-values
def Holm(pvalues, alpha):
    k = find_k_estimator(pvalues, alpha)
    A = np.array(pvalues)
    idx = np.argpartition(A, k)
    return idx[:k]

### calc_partial_cunjunction(pvalues, u, method )
## This function calculates the partial conjunction p-value of u out of n.
## Input:
    # pvals - list sorted of p-values from big to small.
    # u - number of hypothesized true null hypotheses.
    # method - 'B' for Bonferroni  or 'F' for Fisher.
## Output:
    # p_u_n - p-value for the partial conjunction hypothesis of u out of n.
def calc_partial_cunjunction(pvalues, u, method ='B'):
    n = len(pvalues)
    sorted_pvlas = pvalues[0:(n-u+1)]
    if (method == 'B'):
        p_u_n = (n-u+1)*min(sorted_pvlas)
    elif (method == 'F'):
        sum_chi_stat = 0
        for p in sorted_pvlas:
            sum_chi_stat = sum_chi_stat -2*np.log(p)
        p_u_n = 1-stats.chi2.cdf(sum_chi_stat,2*(n-u+1))

    return p_u_n


def main():
    pvals = raw_input("Enter p-values (input example: 0.168,0.297,0.357,0.019,0.218,0.001 ): ")
    pvals = [float(x) for x in pvals.split(',')]
    datasets = {}
    key = 0
    for pval in pvals:
        key+=1
        datasets["dataset"+str(key)]=pval
    print datasets
    alpha = raw_input("Enter significance level: ")
    alpha = float(alpha)
    method = raw_input("Enter p-value combination method (B for Bonferroni, F for Fisher): ")
    print "The k estimator for the number of datasets with effect is: ", find_k_estimator(pvals, alpha, method)
    rejlist = Holm(pvals, alpha)
    print "The rejections list according to the Holm procedure is: "
    for rej in rejlist:
        print "dataset"+str(rej+1)

if __name__ == "__main__":
   main()

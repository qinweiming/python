import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

rng = np.random.RandomState(0)
n_samples_1 = 1000
n_samples_2 = 100
x = np.r_[1.5 * rng.randn(n_samples_1, 2), 0.5 * rng.randn(n_samples_2, 2) + [2, 2]]
y = [0] * (n_samples_1) + (n_samples_2)
print(x)
print(y)
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(x, y)
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - clf.intercept_[0] / w[1]
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(x, y)
ww = wclf.coef_[0]
wa = -ww[0] / ww[1]
wyy = wa * xx - wclf.intercept_[0] / ww[1]
h0 = plt.plot(xx, yy, "k-", label="no weigths")
h1 = plt.plot(xx, wyy, 'k--', label='with weights')
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.legend()

plt.axis('tight')
plt.show()

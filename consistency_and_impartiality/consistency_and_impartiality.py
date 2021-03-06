#! python3

import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas
import PIL
import sklearn

# 真の平均, 真の分散
true_mean = 0
true_variance = 1

# 標本データ作成
def create_data(mean, variance, N):
    return [np.random.normal(true_mean, true_variance) for i in range(N)]

# 標本平均, 標本分散, 不偏分散
def sample_mean(data_x):
    return np.mean(data_x)

def sample_variance(data_x):
    s_mean = sample_mean(data_x)
    return np.sum(np.power(data_x - s_mean, 2))/len(data_x)

def unbiased_variance(data_x):
    s_mean = sample_mean(data_x)
    return np.sum(np.power(data_x - s_mean, 2))/(len(data_x)-1)

# Nの範囲を設定
N = range(1, 51)
M = 40

mean_sm_list = []
mean_sv_list = []
mean_uv_list = []

sample_sm_list = []
sample_sv_list = []
sample_uv_list = []

# 標本数毎に計算を行う
for i in N:
    sm_list = []
    sv_list = []
    uv_list = []

    for j in range(2000):
        data_x = create_data(true_mean, true_variance, i)
        sm, sv, uv = sample_mean(data_x), sample_variance(data_x), unbiased_variance(data_x)
        sm_list.append(sm)
        sv_list.append(sv)
        uv_list.append(uv)

    mean_sm_list.append(np.mean(sm_list))
    mean_sv_list.append(np.mean(sv_list))
    mean_uv_list.append(np.mean(uv_list))

    sample_sm_list.extend(list(np.random.choice(sm_list, M)))
    sample_sv_list.extend(list(np.random.choice(sv_list, M)))
    sample_uv_list.extend(list(np.random.choice(uv_list, M)))

sample_N = []
for i in N:
    sample_N.extend([i]*M)

fig1, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(5, 4))

# 標本平均
ax1.plot(N, mean_sm_list, label='mean')
ax1.plot(sample_N, sample_sm_list, 'o', color='green', markersize=0.5)
ax1.set_title('Sample mean')
ax1.set_xlabel('N')
ax1.legend()

plt.savefig('consistency_and_impartiality/mean.png')

fig2, ax2 = plt.subplots(ncols=2, nrows=1, figsize=(10, 4), sharex=True)

# 標本分散
ax2[0].plot(N, mean_sv_list, label='mean')
ax2[0].plot(sample_N, sample_sv_list, 'o', color='green', markersize=0.5)
ax2[0].set_title('Sample variance')
ax2[0].set_xlabel('N')
ax2[0].legend()

# 不偏分散
ax2[1].plot(N, mean_uv_list, label='mean')
ax2[1].plot(sample_N, sample_uv_list, 'o', color='green', markersize=0.5)
ax2[1].set_title('Unbiased variance')
ax2[1].set_xlabel('N')
ax2[1].legend()

plt.savefig('consistency_and_impartiality/variance.png')
plt.show()

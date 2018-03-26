import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# The three distributions
nsamples = 1000
scale_normal = 1.0
mean_normal = 0
shape_gamma = 1.1
scale_gamma = 1.0
low_uniform = 0
high_uniform = 10
x1 = np.random.normal(mean_normal,scale_normal,nsamples)
x2 = np.random.gamma(shape_gamma,scale_gamma,nsamples)
x3 = np.random.uniform(low_uniform,high_uniform,nsamples)

# The initial plots
fig, axes = plt.subplots(1,3,sharey=True)
bins = 100
alpha = 0.5

axes[0].hist(x1,normed=True,bins=bins,alpha=alpha,color='blue')
axes[0].axvline(np.mean(x1),0,1,lw=2,color='r',alpha=alpha)
axes[0].set_xlim(-10,10)

axes[1].hist(x2,normed=True,bins=bins,alpha=alpha,color='green')
axes[1].axvline(np.mean(x2),0,1,lw=2,color='r',alpha=alpha)
axes[1].set_xlim(0,10)

axes[2].hist(x3,normed=True,bins=bins,alpha=alpha,color='magenta')
axes[2].axvline(np.mean(x3),0,1,lw=2,color='r',alpha=alpha)
axes[2].set_xlim(0,10)

# Sliders
min_samples = 100
max_samples = 1000
ax_samples = plt.axes([0.47, 0.9, 0.1, 0.03])

min_n, max_n = np.min(x1), np.max(x1)
axcolor = 'lightgoldenrodyellow'

axmean_n = plt.axes([0.14, 0.05, 0.2, 0.03], facecolor=axcolor)		#[left, bottom, width, height]
axstd_n = plt.axes([0.14, 0.01, 0.2, 0.03], facecolor=axcolor)

ax_shape_g = plt.axes([0.41, 0.05, 0.2, 0.03], facecolor=axcolor)
ax_scale_g = plt.axes([0.41, 0.01, 0.2, 0.03], facecolor=axcolor)

ax_low_u = plt.axes([0.68, 0.05, 0.2, 0.03], facecolor=axcolor)
ax_high_u = plt.axes([0.68, 0.01, 0.2, 0.03], facecolor=axcolor)

sl_samples = Slider(ax_samples,label='n_samples',valmin=100,valmax=1000,valinit=1000)
sl_mean_x1 = Slider(axmean_n,label='mean',valmin=-2,valmax=2,valinit=mean_normal)
sl_std_x1 = Slider(axstd_n,label='std',valmin=0,valmax=3.0,valinit=scale_normal)
sl_shape_x2 = Slider(ax_shape_g,label='shape',valmin=1.0,valmax=2.0,valinit=shape_gamma)
sl_scale_x2 = Slider(ax_scale_g,label='scale',valmin=1.0,valmax=2.0,valinit=scale_gamma)
sl_low_x3 = Slider(ax_low_u,label='low',valmin=0.0,valmax=10.0,valinit=low_uniform)
sl_high_x3 = Slider(ax_high_u,label='high',valmin=0.0,valmax=10.0,valinit=high_uniform)

# Slider callbacks
def update_nsamples(val):
	val = int(sl_samples.val)

	val1_axes1 = sl_mean_x1.val
	val2_axes1 = sl_std_x1.val

	val1_axes2 = sl_shape_x2.val
	val2_axes2 = sl_scale_x2.val

	val1_axes3 = sl_low_x3.val
	val2_axes3 = sl_high_x3.val

	x1 = np.random.normal(val1_axes1,val2_axes1,val)
	x2 = np.random.gamma(val1_axes2,val2_axes2,nsamples)
	x3 = np.random.uniform(val1_axes3,val2_axes3,nsamples)

	axes[0].cla()
	axes[0].hist(x1,normed=True,bins=bins,alpha=alpha,color='blue')
	axes[0].axvline(np.mean(x1),0,1,lw=2,color='r',alpha=alpha)
	axes[0].set_xlim(-10,10)
	axes[1].cla()
	axes[1].hist(x2,normed=True,bins=bins,alpha=alpha,color='green')
	axes[1].axvline(np.mean(x2),0,1,lw=2,color='r',alpha=alpha)
	axes[1].set_xlim(0,10)
	axes[2].cla()
	axes[2].hist(x3,normed=True,bins=bins,alpha=alpha,color='magenta')
	axes[2].axvline(np.mean(x3),0,1,lw=2,color='r',alpha=alpha)
	axes[2].set_xlim(0,10)
sl_samples.on_changed(update_nsamples)

def update_val1(val):
	val1 = sl_mean_x1.val
	val2 = sl_std_x1.val
	x1 = np.random.normal(val1,val2,nsamples)
	axes[0].cla()
	axes[0].hist(x1,normed=True,bins=bins,alpha=alpha,color='blue')
	axes[0].axvline(np.mean(x1),0,1,lw=2,color='r',alpha=alpha)
	axes[0].set_xlim(-10,10)
sl_mean_x1.on_changed(update_val1)
sl_std_x1.on_changed(update_val1)

def update_val2(val):
	val1 = sl_shape_x2.val
	val2 = sl_scale_x2.val
	x2 = np.random.gamma(val1,val2,nsamples)
	axes[1].cla()
	axes[1].hist(x2,normed=True,bins=bins,alpha=alpha,color='green')
	axes[1].axvline(np.mean(x2),0,1,lw=2,color='r',alpha=alpha)
	axes[1].set_xlim(0,10)
sl_shape_x2.on_changed(update_val2)
sl_scale_x2.on_changed(update_val2)

def update_val3(val):
	val1 = sl_low_x3.val
	val2 = sl_high_x3.val
	x3 = np.random.uniform(val1,val2,nsamples)
	axes[2].cla()
	axes[2].hist(x3,normed=True,bins=bins,alpha=alpha,color='magenta')
	axes[2].axvline(np.mean(x3),0,1,lw=2,color='r',alpha=alpha)
	axes[2].set_xlim(0,10)
sl_low_x3.on_changed(update_val3)
sl_high_x3.on_changed(update_val3)

plt.show()

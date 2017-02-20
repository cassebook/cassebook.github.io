#!/usr/bin/env python

# Example to illustrate the benefit of using EDHMM over HMM, to fit temporally structured event patterns.
#
# Written by Dan Stowell 2016.
#
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
# You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 


import numpy as np
from matplotlib import pyplot as plt

import pyhsmm
from pyhsmm.util.text import progprint_xrange
from pyhsmm.util.general import rle

import matplotlib
#matplotlib.use('PDF') # http://www.astrobetter.com/plotting-to-a-file-in-python/
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams.update({'font.size': 7})

np.random.seed(54321)

############################################################################
# a hand-made generative process for some data to analyse
gen_dur = [
	pyhsmm.distributions.Uniform(20, 25),
	pyhsmm.distributions.Uniform( 2,  4),
	]

ndims = 10    # dimnality of observations
if ndims==2:
	gen_obs = [
		pyhsmm.distributions.Gaussian(np.array([-1.5, -1.5]), np.eye(2)),
		pyhsmm.distributions.Gaussian(np.array([ 1.5,  1.5]), np.eye(2)),
		]
else:
	# higher dim
	tpl = [0.5, 1.35, 1.35, 1.35, 0.5, 0.5]
	gen_obs = [
		pyhsmm.distributions.Gaussian(np.array([0                 for idx in range(ndims)]), np.eye(ndims)),
		pyhsmm.distributions.Gaussian(np.array([tpl[idx%len(tpl)] for idx in range(ndims)]), np.eye(ndims)),
		]

def sample_some_data(dur):
	"Just samples from a simple binary EDHMM"
	ndims = gen_obs[0].rvs().shape[1]
	data = np.zeros((0, ndims))
	state = 0
	trueseq = []
	while data.shape[0] < dur:
		nextlen = int(gen_dur[state].rvs())
		data = np.vstack((data, gen_obs[state].rvs(nextlen)))
		trueseq.extend([state] * nextlen)
		state = 1 - state
	data    = data[:dur, :]
	trueseq = trueseq[:dur]
	return data, np.array(trueseq, dtype=int)

numframes = 4000
data, trueseq = sample_some_data(numframes)
print "data.shape: %s" % (data.shape,)

myxlim = (500, 1200)

############################################################################

def plot(self,fig=None,plot_slice=slice(None),update=False,draw=True):
	update = update and (fig is not None)
	fig = fig if fig else self.make_figure()
	feature_ax, stateseq_axs = self._get_axes(fig)

	sp1_artists = self.plot_observations(feature_ax,plot_slice=plot_slice,update=update)

	feature_ax.axhline(0, color=(0.7, 0.7, 0.7))
	feature_ax.axvline(0, color=(0.7, 0.7, 0.7))

	assert len(stateseq_axs) == len(self.states_list)
	sp2_artists = \
	    [artist for s,ax,data in zip(self.states_list,stateseq_axs,self.datas)
		for artist in self.plot_stateseq(s,ax,plot_slice,update=update,draw=False)]

	if draw: plt.draw()

	return sp1_artists + sp2_artists

############################################################################
#  posterior inference

# Set the weak limit truncation level
Nmax = 2   #25    # NOTE: the Geom mismatch shows up as selecting lots of states if we allow it. alternatively, if we restrict to 2 we see the effect directly in the durations.

# and some hyperparameters
obs_dim = data.shape[1]
obs_hypparams = {'mu_0':np.zeros(obs_dim),
                'sigma_0':np.eye(obs_dim),
                'kappa_0':0.25,
                'nu_0':obs_dim+2}
dur_hypparams_pois = {'alpha_0':2*15,     # NOTE: the prior seems to have clear influence. the mean duration (alpha/beta) being 15 fits much better than 30.
                 'beta_0':2}
dur_hypparams_geom = {'alpha_0':2,
                 'beta_0':5}

resultstore = {}
for mode in ['pois', 'geom']:
	print("=======================================")
	print("Running mode: %s" % mode)

	obs_distns = [pyhsmm.distributions.Gaussian(**obs_hypparams) for state in range(Nmax)]

	dur_distns = [
		{
			'pois': pyhsmm.distributions.PoissonDuration(**dur_hypparams_pois),
			'geom': pyhsmm.distributions.GeometricDuration(**dur_hypparams_geom),
		}[mode] for state in range(Nmax)]



	bestposteriormodel = False
	for _ in range(5): # we are re-running the model fit multiple times and keeping only the best

		posteriormodel = pyhsmm.models.WeakLimitHDPHSMM(
			alpha=6.,gamma=6., # these can matter; see concentration-resampling.py
			init_state_concentration=6., # pretty inconsequential
			obs_distns=obs_distns,
			dur_distns=dur_distns)
		posteriormodel.add_data(data,trunc=60) # duration truncation speeds things up when it's possible

		for idx in progprint_xrange(150):
			posteriormodel.resample_model()

		if bestposteriormodel==False or posteriormodel.log_likelihood() > bestposteriormodel.log_likelihood():
			print("We have a winner")
			bestposteriormodel = posteriormodel

	plot(bestposteriormodel)
	plt.title(mode)

	plt.show()

	thestateseq = bestposteriormodel.states_list[-1].stateseq
	# NOTE: here we fix the state-ambiguity by flipping the inferred state seq if it's become inverted
	if np.mean(thestateseq) > 0.5:
		thestateseq = 1 - thestateseq
	resultstore[mode] = {
		'stateseq': thestateseq,
		'rle': rle(thestateseq),
	}

# add 'true' to resultstore as if it were a result!
resultstore['true'] = {
	'stateseq': trueseq,
	'rle': rle(trueseq),
}

##############################################################################

#print resultstore
#print trueseq

modelist = ['true', 'geom', 'pois']
modedata = {
	'true': {'lbl': 'True',            'color': 'k', 'ls': '-'},
	'pois': {'lbl': 'EDHMM' # (Poisson)'
		, 'color': 'g', 'ls': '-'},
	'geom': {'lbl': 'HMM',             'color': 'b', 'ls': '-.'},
}


pdf = PdfPages('edhmm_example_fit.pdf')
plt.figure()

def plot_my_timeline(aseq, color='b'):
	if False:
		plt.imshow(np.tile(np.reshape(aseq['stateseq'], (1, -1)), (100, 1)), cmap='binary', interpolation='nearest')
	elif False:
		cumpos = np.cumsum(aseq['rle'][1])
		for whichpos, (stateval, adur) in enumerate(zip(*aseq['rle'])):
			if stateval==1:
				plt.axvspan(cumpos[whichpos-1], cumpos[whichpos-1]+adur, color='k')
	else:
		plt.fill_between(range(len(aseq['stateseq'])), aseq['stateseq'], step='mid', color=color)
		plt.ylim(-0.01, 1.1)

	plt.yticks([])
	plt.xticks([])
	if myxlim:
		plt.xlim(myxlim)
	else:
		plt.xlim(0, numframes)

if False:
	plt.subplot(8,1,1)
	if ndims > 2:
		vmin = np.percentile(data,  5)
		vmax = np.percentile(data, 95)
		plt.imshow(data[:, np.arange(0, data.shape[1], 0.15).astype(int)].T, cmap='Accent', interpolation='nearest', vmin=vmin, vmax=vmax)
		if myxlim:
			plt.xlim(myxlim)
	else:
		plt.plot(data)
	plt.yticks([])
	plt.ylabel("Observed")

for whichmode, mode in enumerate(modelist):
	plt.subplot(8,1,2+whichmode)
	plot_my_timeline(resultstore[mode], color=modedata[mode]['color'])
	plt.ylabel(modedata[mode]['lbl'])
plt.xlabel("Time (frames)")

# a histogram of the true and the inferred state durations encountered, separately for the on and the off states (therefore two plots, each with 3 "transparent" histograms on)
for whichsubplot, whichstate in [(3, 0), (4, 1)]:
	plt.subplot(2,2,whichsubplot)
	if False:
		durscollected = []
		for whichmode, mode in enumerate(modelist):
			durscollected.append([adur for stateval, adur in zip(*resultstore[mode]['rle']) if stateval==whichstate])

		plt.hist(durscollected, label=[modedata[mode]['lbl'] for mode in modelist], normed=True) #, histtype='step')
	else:
		for whichmode, mode in enumerate(modelist):
			binclump = [5, 1, ][whichstate]
			plotdata = np.bincount([int(np.ceil(adur/binclump)) for stateval, adur in zip(*resultstore[mode]['rle']) if stateval==whichstate])
			plotdata = np.array(plotdata, dtype=float) / np.sum(plotdata)
			plotdata = np.concatenate((plotdata, [0]))
			plt.fill_between(np.arange(len(plotdata))*binclump, plotdata, step='mid',  color=modedata[mode]['color'], alpha=0.1)
			plt.step(        np.arange(len(plotdata))*binclump, plotdata, where='mid', color=modedata[mode]['color'], label=modedata[mode]['lbl'], linestyle=modedata[mode]['ls'])
		plt.ylim(0, 1)

	plt.ylabel('Relative frequency')
	plt.xlabel("Empirical durations of %s periods (frames)" % ['off', 'on'][whichstate])
	plt.legend()

pdf.savefig(bbox_inches='tight')
#plt.show()
plt.close()
pdf.close()


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class masw:
	def __init__(self, filename, dt, fs, N, dx, x1, direction, header=6):
	    # fs - Sampling frequency
		# N  - Number of channels
		# dx - spacing beetween geophones
		# x1 - offset soure
		# direction - Forward or backward
		self.filename = filename
		self.dt       = dt
		self.header   = header
		self.data     = pd.read_csv(filename, header=self.header, delimiter="\t", skip_blank_lines=False)
		self.fs       = fs
		self.N        = N
		self.dx       = dx
		self.x1       = x1
		self.direction = direction
		self.Lu        = self.data.shape[0]
		self.Tmax      = self.Lu/fs - 1.0/fs
		self.T         = np.linspace(0,self.Tmax, self.data.shape[0])
		self.L         = (N-1)*dx
		self.x         = np.arange(start=x1, stop=self.L+x1+dx,step=dx)
		self.A         = None
		self.Aplot     = None
		self.fplot     = None
		self.cplot     = None
		self.cT        = None
		self.f         = None
		self.LcT       = None



	def plot(self, scale=0.5):
		fig, ax = plt.subplots(1,1, figsize = (8,10))
		offset  = self.x1
		for col in self.data:
			y      = scale*self.data[col]/self.data[col].abs().max()+offset
			x      = self.T

			ax.plot(x,y,'k')
			ax.fill_between(x,y,y2=offset, where=(y>offset),color='k')
			ax.set_xlabel('Tiempo [s]')
			ax.set_ylabel('Distancia [m]')
			offset = offset + self.dx

		plt.grid()
		fig.tight_layout()

	def dispersion_imaging(self, cT_min, cT_max, delta_cT):
		omega_fs = 2*np.pi*self.fs 
		U        = np.zeros_like(self.data)
		P        = np.zeros_like(self.data)
		Unorm    = np.zeros_like(self.data)

		Unp   = self.data.to_numpy()
		U     = np.fft.fft(self.data, axis = 0 )
		
		Unorm = U/abs(U)
		P     = np.exp(-1j*np.angle(U))

		omega = np.arange(self.Lu)*omega_fs/self.Lu
		self.cT    = np.arange(cT_min, cT_max+delta_cT, delta_cT)
		self.LcT   = len(self.cT)
		self.f     = omega/(2*np.pi)
		self.A     = np.zeros((self.Lu, self.LcT))

		for m, omega_test in enumerate(omega):
			for n, c_phase in enumerate(self.cT):
				delta = omega_test/c_phase
				temp = 0
				for l, x_test in enumerate(self.x):
					temp = temp + np.exp(-1j*delta*x_test)*P[m,l]
				self.A[m,n] = np.abs(temp)/self.N

		return None

	def plot_dispersion_image_2D(self, fmin, fmax, resolution, FigWidth=8, FigHeight=8, FigFontsize=12):
		no_fmin    = np.argmax(self.f >= fmin)
		no_fmax    = np.argmax(self.f >= fmax)
		self.Aplot = self.A[ no_fmin:no_fmax+1, :]
		self.fplot      = self.f[ no_fmin:no_fmax+1]
		self.cplot      = self.cT

		print("A: ", self.Aplot.shape)
		print("f: ", self.fplot.shape)
		print("c: ", self.cplot.shape)

		fig, ax = plt.subplots(1,1, figsize = (FigWidth,FigHeight))

		cntr1 = ax.contourf(self.fplot,self.cplot,self.Aplot.T,levels=resolution, cmap="RdBu_r")
		ax.set_xlabel('Frecuencia [Hz]')
		ax.set_ylabel('Velocidad de Fase [m/s]')
		fig.colorbar(cntr1, ax=ax)

	def extract_dispersion_curve(self, f_receivers, select,up_low_boundary,p, resolution=100, FigWidth=8, FigHeight=8):
		#fig, ax = plt.subplots(1,1, figsize = (FigWidth,FigHeight))
		Aabsnorm2 = np.zeros_like(self.Aplot)
		Aabsnorm2 = (self.Aplot.T/self.Aplot.max(axis=1)).T

		freq_ind, c_ind = np.where( Aabsnorm2== 1)
		fvec            = [self.fplot[fi]        for    fi in           freq_ind  if self.fplot[fi] > f_receivers]
		cvec            = [self.cplot[c_ind[m]]  for m, fi in enumerate(freq_ind) if self.fplot[fi] > f_receivers]

		return fvec, cvec







"""
@author: HuidobroMG

We read and show the frequencies present in the LA_YT.wav file.
It uses a fast fourier transformation of the Python library Scipy to extract the spectrum.
At the end of the code it is also shown how to construct a Gaussian wavepacket of frequencies.
"""

# Import the modules
import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.fft as fft

# Read the sound file
sound = wave.open('La_YT.wav', 'rb')

# Number of samples (data points) per second
sample_freq = sound.getframerate()

# Total number of samples
n_samples = sound.getnframes()

# Time of the audio
t = n_samples/sample_freq
time = np.linspace(0, t, n_samples)
Nt = len(time)
dt = time[1] - time[0]

# The channels are different directions from which the sound is recorded
n_channels = sound.getnchannels()

# Read numerically the sampling
signal_wave = np.frombuffer(sound.readframes(n_samples), dtype = np.int16)
if n_channels == 2:
    l_channel = signal_wave[0::2]
    r_channel = signal_wave[1::2]

# Plot the wave
fig = plt.figure(figsize = (13, 6.5))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Now decompose in modes with a FFT splitting the left and right partial waves
# In this case this is irrelevant
spec_l = np.abs(fft.rfft(l_channel))
nu_l = fft.rfftfreq(Nt, d = dt)
spec_r = np.abs(fft.rfft(r_channel))
nu_r = fft.rfftfreq(Nt, d = dt)

ax1.plot(time, l_channel, 'b')
ax2.plot(time, r_channel, 'r')

ax3.plot(nu_l, spec_l/max(spec_l), 'b')
ax4.plot(nu_r, spec_r/max(spec_r), 'r')

# Create now a Gaussian wavepacket with a continous spectrum of frequencies
dt = 0.01
t = np.arange(-2, 2, dt)
Nt = len(t)

# Create a Gaussian wavepacket
Nfreqs = 100
nu = np.linspace(0, 30, Nfreqs)

central_nu = 10
dispersion = 0.5
amplitudes = np.exp(-(nu-central_nu)**2/(2*dispersion))

partial_waves = np.zeros((Nfreqs, Nt))
wave = np.zeros(Nt)
for i in range(Nfreqs):
    partial_waves[i] = amplitudes[i]*np.sin(2*np.pi*nu[i]*t)
    wave += partial_waves[i]

# Another simpler wave
#wave = 2*np.sin(2*np.pi*10*t) + 0.1*np.sin(2*np.pi*3*t) + np.sin(2*np.pi*1.5*t)

# Now decompose in modes
y = fft.rfft(wave)
y = np.abs(y)
nu_y = fft.rfftfreq(Nt, d = dt)

fig = plt.figure(figsize = (13, 6.5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(t, wave, 'b-')
ax2.plot(nu, amplitudes, 'b.')
ax2.plot(nu_y, y/np.max(y), 'b-')

plt.show()
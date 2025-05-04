import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# Load the noisy audio
y, sr = librosa.load('noisy_audio.wav')
print(y.shape)
D = librosa.stft(y)

# Estimate the magnitude spectrogram
magnitude = np.abs(D)
# Estimate noise level from the first few frames
noise_level = np.mean(magnitude[:, :1000])
# Spectral subtraction to suppress noise
cleaned_magnitude = np.maximum(magnitude - noise_level, 0)
# Reconstruct the cleaned audio signal
cleaned_D = cleaned_magnitude * np.exp(1j * np.angle(D))
cleaned_audio = librosa.istft(cleaned_D)
# Save the cleaned audio
sf.write('cleaned_audio.wav', cleaned_audio, sr)
# Read both original and cleaned signals for plotting
r, _ = sf.read('cleaned_audio.wav')
# Plot the original and cleaned signals
plt.subplot(2, 1, 1)
plt.plot(y)
plt.title("Original Signal")
plt.subplot(2, 1, 2)
plt.plot(r)
plt.title("Enhanced Signal")

plt.show()

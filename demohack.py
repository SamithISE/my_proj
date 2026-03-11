import librosa
import matplotlib.pyplot as plt
path="audio.wav"
waveform,sample_rate=librosa.load(path,sr=None,mono=False)
print(waveform,sample_rate)
plt.figure(figsize=(10,4))
librosa.display.waveshow(waveform,sr=sample_rate)

plt.title('WaveForm')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
import librosa
import winsound
import numpy as np
import soundfile as sf
import wave
import sounddevice as sd
import matplotlib.pyplot as plt


Filepath = "Audio - Raw.Wav" # Path to the audio file
sound = wave.open(Filepath, 'rb')   # Open the audio file in "read-binary" mode
# get some sound attributes.....
print("Number of Channels: ", sound.getnchannels()) # Number of channels (1 for mono, 2 for stereo)
print("Sample Width: ", sound.getsampwidth()) # Sample width in bytes (2 for 16-bit PCM)
print("Frame Rate: ", sound.getframerate()) # Sample rate (number of samples per second)
print("Number of Frames: ", sound.getnframes()) # Total number of frames (samples) in the audio file
print("Parameters: ", sound.getparams()) # Get all parameters of the audio file
print("Compression Type: ", sound.getcomptype()) # No Compression type cuz it is a .wav file
Duration = sound.getnframes() / sound.getframerate() # Duration in seconds
frames = sound.readframes(sound.getnframes()) # Read all frames from the audio file
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

sound_copy = wave.open("Audio - Copy.wav", 'wb') # Create a new audio file in "write-binary" mode
sound_copy.setnchannels(sound.getnchannels()) # Set the number of channels same as the file we read
sound_copy.setsampwidth(sound.getsampwidth()) # Set the sample width same as the file we read
sound_copy.setframerate(sound.getframerate()) # Set the sample rate same as the file we read
sound_copy.setnframes(sound.getnframes()) # Set the number of frames same as the file we read
sound_copy.writeframes(frames) # Write the frames to the new audio file
sound_copy.close() # Close the new audio file
sound.close() # Close the audio file
print("Audio - Copy.wav created successfully")
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

fq = 44100 # Sampling frequency
time = 6 # Duration in seconds
print("talking....")
new_sound = sd.rec(int(time * fq), samplerate=fq, channels=1) # Record audio for the specified duration
sd.wait() # Wait until the recording is finished
print("done....")
sf.write("Audio - Recorded.wav", new_sound, fq) # Save the recorded audio to a file
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

filename = "Audio - copy.wav" # Path to the audio file
print("Playing audio file...")
winsound.PlaySound(filename, winsound.SND_FILENAME) # Play the audio file using winsound
print("done....")
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

print("Playing audio file using sounddevice...")
data, fs = sf.read(filename, dtype='float32') # Read the audio file using soundfile
sd.play(data, fs) # Play the audio file using sounddevice
print(data) # Print the audio data
print(fs) # Print the sample rate
sd.wait() # Wait until the playback is finished
print("done....")
print("-------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------

print("write data using soundfile...")
data2, fs2 = sf.read("Audio - Copy.wav",stop =-44100, dtype='float32') # Read the audio file using soundfile
sd.play(data2, fs2) # Play the audio file using sounddevice
print(data2) # Print the audio data
print(fs2) # Print the sample rate
status = sd.wait() # Wait until the playback is finished
print("done.... with" ,status, " Errors") # Print the status of the playback
sf.write("Audio - Copy.wav", data2, fs2) # Save the audio data to a file
print("-------------------------------------------------------")
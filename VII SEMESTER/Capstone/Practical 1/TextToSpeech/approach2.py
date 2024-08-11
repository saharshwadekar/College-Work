import wave
import os

# Define a simple phoneme dictionary for demonstration purposes
phoneme_dict = {
    chr(p): chr(p) + '.wav' for p in range(ord('a'), ord('z') + 1)
}

def text_to_phonemes(text):
    # Convert text to phonemes
    # This is a very simplified version and may not cover all cases
    phonemes = []
    for char in text.lower():
        if char in phoneme_dict:
            phonemes.append(phoneme_dict[char])
    return phonemes

def concatenate_audio(phoneme_files, output_file):
    with wave.open(output_file, 'wb') as output:
        for phoneme_file in phoneme_files:
            with wave.open(phoneme_file, 'rb') as phoneme_wave:
                if not output.getnchannels():
                    output.setparams(phoneme_wave.getparams())
                output.writeframes(phoneme_wave.readframes(phoneme_wave.getnframes()))

def text_to_speech(text, phoneme_dir='phonemes', output_file='output.wav'):
    phonemes = text_to_phonemes(text)
    phoneme_files = [os.path.join(phoneme_dir, phoneme) for phoneme in phonemes]
    concatenate_audio(phoneme_files, output_file)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
    print("Speech saved to output.wav")

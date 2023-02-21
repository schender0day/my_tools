from pydub import AudioSegment
import os


def split_mp3(input_file, output_dir, split_time):
    # Load the MP3 file
    audio = AudioSegment.from_file(input_file, format="mp3")

    # Get the length of the audio in milliseconds
    length_ms = len(audio)

    # Calculate the number of splits needed
    num_splits = length_ms // split_time + 1

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Split the audio and save each segment
    for i in range(num_splits):
        start_time = i * split_time
        end_time = start_time + split_time
        split_audio = audio[start_time:end_time]
        output_file = os.path.join(output_dir, f"{i + 1 +5}.mp3")
        split_audio.export(output_file, format="mp3")
minuteTotal = int(input("Input number of minute you want to divide: "))
split_mp3("/Users/xinchen/Documents/AWS_DevOps/2.mp3", "output", 1000 * 60 * minuteTotal)

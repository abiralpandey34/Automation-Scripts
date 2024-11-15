import moviepy.config as config
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Set the path to the ImageMagick binary
config.IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

def add_text_overlay(video, output_video_path, text, position=('center', 'top'), fontsize=50, color='white'):
    # Create a TextClip object with the desired text
    text_clip = TextClip(text, fontsize=fontsize, color=color, size=video.size)

    # Set the position and duration of the text clip
    text_clip = text_clip.set_position(position).set_duration(video.duration)

    # Overlay the text on the video
    video_with_text = CompositeVideoClip([video, text_clip], use_bgclip=True)

    # Write the result to the output file
    video_with_text.write_videofile(output_video_path, codec="h264_nvenc", audio_codec="aac", fps=24, threads=32, progress_bar = False)

# Load the video clip
input_video_path = "kasari.mp4"  # Path to your input video
video = VideoFileClip(input_video_path)

# Get user input for start and end times
# start_time = int(input("Enter the start time in seconds: "))
# end_time = int(input("Enter the end time in seconds: "))
start_time = 0
end_time = 5

# Get the subclip based on user input
clipped_video = video.subclip(start_time, end_time)

# Define output paths and overlay text
output_video_path = "output_video_with_text.mp4"  # Path to save the output video
overlay_text = "Day 10 of Finding"  # Text to overlay

# Add text overlay to the clipped video
add_text_overlay(clipped_video, output_video_path, overlay_text, position=('center', 'top'), fontsize=50, color='white')

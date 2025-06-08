# 🧪 Practice Task: Media Player App
# 🎬 Problem Statement:
# You're building a simple Media Player app that
#  can play Audio and Video files.

# 🔐 Use Abstraction:
# Create an abstract base class called MediaFile 
# with the following abstract methods:

# play()

# pause()

# stop()

# ✅ Create Two Classes that Inherit from It:
# AudioFile

# VideoFile

# Each class should:

# Implement play, pause, and stop with different
#  print messages (like "Playing audio: 🎵" or "Playing video: 🎥")

# 🧪 Example Output:
# python
# Copy
# Edit
# audio = AudioFile()
# video = VideoFile()

# audio.play()     # Output: Playing audio: 🎵
# video.play()     # Output: Playing video: 🎥

# audio.pause()    # Output: Audio paused ⏸️
# video.stop()     # Output: Video stopped ⏹️
# 🔁 Bonus Challenge:
# Add a method called file_type() in each class to
#  return "Audio" or "Video".

from abc import ABC, abstractmethod
class MediaFile(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def pause(self):
        pass
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def file_type(self):
        pass

class AudioFile(MediaFile):
    def play(self):
        print("plays audio")
    def stop(self):
        print("audio stopped")
    def pause(self):
        print("audio paused")
    
    def file_type(self):
        print("Audio")


class VideoFile(MediaFile):
    def play(self):
        print("plays video")
    def stop(self):
        print("video stopped")
    def pause(self):
        print("video paused")
    
    def file_type(self):
        print("video")


audio = AudioFile()
video = VideoFile()

audio.play()     # Output: Playing audio: 🎵
video.play()     # Output: Playing video: 🎥

audio.pause()    # Output: Audio paused ⏸️
video.stop()     # Output: Video stopped ⏹️
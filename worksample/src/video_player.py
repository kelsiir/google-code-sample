"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        # 0 Stopped
        # 1 Playing
        # 2 Paused
        self.video_status = 0
        self.current_video = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print(f"Here's a list of all available videos:")
        video_list = self._video_library.get_all_videos()
        new_list = []
        for i in video_list:
            tags = "["
            for x in i.tags:
                tags = tags + x + " "
            tags = tags + "]"
            if tags == "[]":
                new_list += [f"{i.title} ({i.video_id}) {tags}"]
            else:
                tags = tags[0:len(tags)-2] + "]"
                new_list += [f"{i.title} ({i.video_id}) {tags}"]
        sorted_list = sorted(new_list)
        for n in sorted_list:
            print(f" ", n)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            print("Cannot play video: Video does not exist")
        else:
            if self.video_status == 1 or self.video_status == 2:
                print(f"Stopping video:", self.current_video.title)
                print(f"Playing video: {video.title}")
                self.video_status = 1
                self.current_video = video
            else:
                print(f"Playing video: {video.title}")
                self.video_status = 1
                self.current_video = video

    def stop_video(self):
        """Stops the current video."""
        if self.video_status == 0:
            print("Cannot stop video: No video is currently playing")
        elif self.video_status == 1:
            print("Stopping video:", self.current_video.title)
            self.video_status = 0
            self.current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        if self.video_status == 1:
            print(f"Stopping video:", self.current_video.title)
        random_vid = random.choice(video_list)
        print(f"Playing video: {random_vid.title}")
        self.current_video = random_vid
        self.video_status = 1

    def pause_video(self):
        """Pauses the current video."""
        if self.video_status == 0:
            print("Cannot pause video: No video is currently playing")
        else:
            if self.video_status == 2:
                print("Video already paused:", self.current_video.title)
            else:
                print("Pausing video:", self.current_video.title)
                self.video_status = 2

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_status == 0:
            print(f"Cannot continue video: No video is currently playing")
        else:
            if self.video_status == 2:
                print(f"Continuing video:", self.current_video.title)
                self.video_status = 1
            else:
                print(f"Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        new_list = []
        if self.video_status == 0:
            print("No video is currently playing")
        else:
            tags = "["
            for x in self.current_video.tags:
                tags = tags + x + " "
            tags = tags + "]"
            if tags == "[]":
                new_list += [f"{self.current_video.title} ({self.current_video.video_id}) {tags}"]
            else:
                tags = tags[0:len(tags) - 2] + "]"
                new_list += [f"{self.current_video.title} ({self.current_video.video_id}) {tags}"]
        if self.video_status == 1:
            print("Currently playing: ", end="")
            for i in new_list: print(i)
        elif self.video_status == 2:
            print("Currently playing: ", end="")
            for i in new_list: print(i, end=""), print(" - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

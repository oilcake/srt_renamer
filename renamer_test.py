import unittest
from unittest.mock import patch
from renamer import construct_subs_name, find_matching_subs
from fs_mock import subs_files


class TestRenamer(unittest.TestCase):
    def test_construct_name(self) -> None:
        ep_name = "good_episode.mp4"
        expected = "good_episode.srt"
        subs = construct_subs_name(ep_name)
        self.assertEqual(subs, expected)

    def test_find_matching_subs(self):
        with patch("os.listdir") as patched_os:
            patched_os.return_value = subs_files
            movie_file = (
                "Community.S03E14 Pillows and Blankets 1080p WEB-DL.by.AKTEP.mkv"
            )
            path = "whatever/function_is_mocked"
            expected_result = "Community.S03E14.480p.HDTV.x264-SM.srt"
            self.assertEqual(find_matching_subs(movie_file, path), expected_result)


if __name__ == "__main__":
    unittest.main()

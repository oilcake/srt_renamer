import logging
import os
import re
import sys

logging.basicConfig(level=logging.INFO)


class NoMatch(Exception):
    pass


class NotAnEpisode(Exception):
    pass


def construct_subs_name(episode_name: str):
    name = os.path.splitext(episode_name)[0] + ".srt"
    return name


def find_matching_subs(episode_name, subs_path: str) -> str:
    """looks in a given path for a match of
    standard tv show enumeration mark like 'S02E12'
    and returns corresponding subtitiles file"""
    ep_mark = re.match(r".*(S\d{2}E\d{2})", episode_name, re.IGNORECASE)
    if not ep_mark:
        raise NotAnEpisode("No episode pattern found")
    ep_mark = ep_mark.group(1)
    for subs in os.listdir(subs_path):
        if ep_mark.lower() in subs.lower():
            return subs
    raise NoMatch(f"no matching subtitles for {episode_name}")


def rename(episodes_path, subtitles_path: str) -> None:
    files = map(
        lambda file: os.path.join(episodes_path, file), os.listdir(episodes_path)
    )
    for episode in filter(os.path.isfile, files):
        try:
            sub_name = os.path.join(
                subtitles_path, find_matching_subs(episode, subtitles_path)
            )
            sub_new_name = construct_subs_name(episode)
            logging.info(f"{sub_name} renamed to {sub_new_name}")
            os.rename(sub_name, sub_new_name)
        except (NotAnEpisode, NoMatch) as e:
            logging.warning(f"something is wrong, {e.args[0]} for {episode}")


if __name__ == "__main__":
    rename(sys.argv[1], sys.argv[2])
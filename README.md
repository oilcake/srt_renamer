# subtitle renamer

##### dead simple python script to rename a bunch of .srt files that don't match your favourite tv show episodes' name

When subtitles are placed right next to video and matches video's name mpv can attach it automatically on the fly. There's a [very nice subs downloading script for mpv]([GitHub - davidde/mpv-autosub: Fully automatic subtitle downloading for the MPV media player](https://github.com/davidde/mpv-autosub)), but for me it doesn't work sometimes, so i found myself downloading zips manually and wrote this script to avoid boring renaming by hand.

**only requires python3**

usage

```bash
python3 renamer.py path/to/videos path/to/subtitles
```

test

```bash
python3 renamer_test.py -v
```

Warning! By default all files in subtitles folder will be renamed AND <u>**moved permanently**</u> to episodes' folder. So make a backup if you need originals.



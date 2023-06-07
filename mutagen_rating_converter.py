from pathlib import Path

import mutagen
import mutagen.flac

PATH_TO_MUSIC_FILES = "~/Music/"
DEFAULT_RATING = "0.0"
OLD_RATING_NAME = "RATING"
NEW_RATING_NAME = "FMPS_RATING"
RATING_CONVERSION = {
    "0": "0.0",
    "128": "0.6",
    "192": "0.8",
    "196": "0.8",
    "255": "1.0"
}


def new_rating(data):
    try:
        old_rating = str(data["RATING"][0])
        new_rating = RATING_CONVERSION.get(old_rating)
        return new_rating if new_rating is not None else DEFAULT_RATING
    except:
        return DEFAULT_RATING


def edit_rating(path: Path):
    if not path.is_file():
        return

    try:
        if str(path).endswith(".flac"):
            metadata = mutagen.flac.Open(path)
            l = metadata.get("FMPS_RATING")
            if l is None:
                metadata["FMPS_RATING"] = new_rating(metadata)
                metadata.save()
    except:
        print(f"Some error with {path}")


def main():
    paths = Path(PATH_TO_MUSIC_FILES).glob('**/*')
    for p in paths:
        edit_rating(p)


if __name__ == "__main__":
    main()

import shutil
from datetime import datetime
from pathlib import Path


class MoveFileError(Exception):
    """Custom Exception for error when moving files."""

    pass


def move_file_adding_timestmap(src: Path | str, dest: Path | str = "") -> Path:
    try:
        src = Path(src)
        dest = Path(dest) if dest else Path.cwd()

        # Verify file exists
        if not src.exists():
            raise FileNotFoundError(f"File does not exists: {src}")

        # Verify src is file and not a folder
        if not src.is_file():
            raise ValueError(f"Route is not valid: {src}")

        # Name and extension
        file_name = src.stem
        ext = src.suffix

        file_name_splitted = file_name.split("-")

        # Verify file name has the correct structure
        if len(file_name_splitted) < 5:
            raise ValueError(
                "File name does not have the expected format."
                "It shoul be: \{account_name\}_tipo_\{traxs_types\}_\{month_name\}_\{year\}"
            )

        # Build partition folder structure
        partition = (
            Path(file_name_splitted[0]) / file_name_splitted[4] / file_name_splitted[3]
        )

        # Final folder with partition
        dest = dest / partition

        # Create final folder if it doesn't already exists
        dest.mkdir(parents=True, exist_ok=True)

        # now Timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # New file name
        new_name = f"{file_name}_{timestamp}{ext}"

        dest = dest / new_name

        # Move file to final route. dest is returned
        return shutil.copy2(src, dest)

    except FileNotFoundError as e:
        raise MoveFileError(f"File not found: {e}") from e

    except PermissionError as e:
        raise MoveFileError(f"Denied permissions: {e}") from e

    except OSError as e:
        raise MoveFileError(f"OS error: {e}") from e

    except Exception as e:
        raise MoveFileError(f"Error when processing file: {e}") from e

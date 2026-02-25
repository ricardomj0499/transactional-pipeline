"""
Docstring for basic_pipeline.utils.change_encoding_csv
"""

from pathlib import Path
import csv
import logging
logger = logging.getLogger(__name__)


# Cambiar encoding usando csv reader. Enco
def change_csv_encoding(
    input_path: Path,
    output_path: Path,
    input_encoding: str = "iso-8859-1",
    output_encoding: str = "utf-8",
) -> None:
    with open(input_path, mode="r", encoding=input_encoding, newline="") as f_in:
        reader = csv.reader(f_in, delimiter=",")

        with open(output_path, mode="w", encoding=output_encoding, newline="") as f_out:
            writer = csv.writer(f_out, delimiter=",")

            for row in reader:
                writer.writerow(row)


from pathlib import Path
import csv
import logging




def change_csv_encoding(
    input_path: Path,
    output_path: Path,
    input_encoding: str = "iso-8859-1",
    output_encoding: str = "utf-8",
    delimiter: str = ",",
    encoding_errors: str = "strict",  # "strict" | "replace" | "ignore"
) -> None:
    input_path = Path(input_path)
    output_path = Path(output_path)

    # ---- Validation ----
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    if not input_path.is_file():
        raise ValueError(f"Input path is not a file: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(
        "Converting CSV encoding from %s to %s: %s → %s",
        input_encoding,
        output_encoding,
        input_path,
        output_path,
    )

    # ---- Processing ----
    row_count = 0

    with open(
        input_path,
        "r",
        encoding=input_encoding,
        errors=encoding_errors,
        newline="",
    ) as f_in:
        reader = csv.reader(f_in, delimiter=delimiter)

        with open(
            output_path,
            "w",
            encoding=output_encoding,
            errors=encoding_errors,
            newline="",
        ) as f_out:
            writer = csv.writer(f_out, delimiter=delimiter)

            for row in reader:
                writer.writerow(row)
                row_count += 1

    logger.info("Finished processing %d rows", row_count)

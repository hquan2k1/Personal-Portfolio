# Conversion of kindle clippings to CSV

This script, `kindleClippingExtractor.py`, is designed to take in a `MyClippings.txt` file extracted from a Kindle device and convert it into a CSV file. The resulting CSV file will have the following columns:

- Author: The author of the book from which the clipping was made.
- Book: The title of the book.
- Location/Page Number: The location or page number of the clipping within the book.
- Quote/Note: The actual text of the clipping, which can be a quote or a note.

To use the script, simply provide the path to the `MyClippings.txt` file as an input. The script will then parse the file and generate a CSV file with the extracted information.

Please note that this script assumes the `MyClippings.txt` file follows the standard format used by Kindle devices. If the file format differs, the script may not work as expected.

The CSV file can then be uploaded onto a Google Sheets where a simple JavaScript that can send daily emails about the highlights/notes

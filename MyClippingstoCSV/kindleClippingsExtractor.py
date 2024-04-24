def extract_clippings():
    """
    Extracts clippings from a Kindle clippings file and stores them in a CSV file.

    Reads a text file containing clippings from a Kindle device, extracts the title, author, page/location, and clippings,
    and stores them in a CSV file. The CSV file will have the following columns: Title, Author, Page/Location, Clippings.

    Args:
        None

    Returns:
        None
    """

    # Variables to keep persisted: title, author, clippings
    titleforChapter = ""
    title = ""
    chapter = ""
    tempChapter = ""
    author = ""
    pageNumber = ""
    clippings = ""
    counter = 0
    note = False
    location = False

    # First open the .txt file that contains all the clippings from the Kindle
    # Open the file in read mode
    clippingsFile = open('My Clippings.txt', 'r')
    errorFile = open('errorFile.txt', 'w')

    # Create a .csv file to store the clippings
    # Open the file in write mode
    # The column headers are: Title, Author, Page/Location, Clippings
    clippingsCSV = open('clippings.csv', 'w')
    clippingsCSV.write("Title, Author, Page/Location, Clippings\n")

    for line in clippingsFile:
        try:
            if counter == 0:
                # Extract the title, before the first parantheses
                title = "\"" + line.split("(")[0].strip() + "\""
                # Extract the author, after the first parantheses
                author = line.split("(")[1].split(")")[0].strip()
                clippingsCSV.write(title + ", " + author)
                counter += 1
                continue
            elif counter == 1:
                # If line has 2 "|", then extract the page number
                if line.count("|") == 2:
                    # If line contains "Note"
                    if "Note" in line:
                        pageNumber = line.split("- Your Note on page ")[1].split("|")[0].strip()
                        note = True
                    else:
                        # Extract the page number, after the second "|", and disregard the rest of the line
                        pageNumber = line.split("- Your Highlight on page ")[1].split("|")[0].strip()
                else:
                    if "Location" in line:
                        if "Note" in line:
                            pageNumber = line.split("- Your Note on Location ")[1].split("|")[0].strip()
                            note = True
                            location = True
                        else:
                            pageNumber = line.split("- Your Highlight on Location ")[1].split("|")[0].strip()
                    else:
                        pageNumber = line.split("- Your Highlight on page ")[1].split("|")[0].strip()

                # If page number is "*-*", remove the contents after the hyphen, store the first part before the hyphen as integer
                if "-" in pageNumber:
                    pageNumber = pageNumber.split("-")[0]

                clippingsCSV.write(", " + pageNumber)

                counter += 1

                continue
            elif counter == 2:
                # Third line is always empty, skip and move to the next line
                counter += 1
                continue
            elif counter == 3:
                # Extract the clippings
                if line.strip() == "==========":
                    counter = 0
                    title = ""
                    author = ""
                    pageNumber = 0
                    clippings = ""
                    clippingsCSV.write("\n")
                else:
                    if note:
                        clippings += "Personal Note: "
                        note = False
                    clippings += line
                    clippingsCSV.write(", \"" + clippings.strip() + "\"")
                    continue
        except IndexError:
            errorFile.write("IndexError at line: " + line + "\n") 
            continue

    # Close the file
    clippingsFile.close()
    clippingsCSV.close()

extract_clippings()
import requests

# Called on original Telegram message
def isValid(message):
    command = message.split(" ")
    # Check arguments fit the form
    if len(command) != 1:
        if len(command) != 2:
            return False
        # Ensure flags are valid
        if command[1] != "—website" and command[1] != "—mirror":
            # Telegram autocorrects to em dash, but just in case
            if command[1] != "--website" and command[1] != "--mirror":
                return False
    return True



# Here, we know that the message is valid
def manageMessage(message):
    command = message.split(" ")
    URL = command[0]
    webpageText = requests.get(URL).text

    # Open file in append mode
    myFile = open("toDownload.txt", "w+")

    # Check if a special website

    # Check file extension for image
    extension = URL.split(".")[-1].lower()
    if extension == "jpg" or extension == "png" or extension == "gif" or extension == "jpeg":
        myFile.write("wget \"" + URL + "\"")

    # Check if document
    elif extension == "pdf" or extension == "docx":
        myFile.write("wget \"" + URL + "\"")

    # Search for a stylesheet
    elif "stylesheet" not in webpageText:
        myFile.write("wget -e robots=off -r -nc -np \"" + URL + "\"")

    # Default assumption
    else:
        # Deal with 2nd argument if exists
        if len(command) is 2:
            # If mirroring, add to file
            if "mirror" in command[1]:
                myFile2 = open("mirroredSites.txt", "w+")
                myFile2.write(URL + "\n")
                myFile2.close()
            # Either way, download it now
            myFile.write("wget -mkEpnp \"" + URL + "\"")
        else:
            # Download as article
            myFile.write("python3 article.py \"" + URL + "\"")

    myFile.write("\n")
    myFile.close()

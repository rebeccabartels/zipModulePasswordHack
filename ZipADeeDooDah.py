# Import the zipfile module into the application
import zipfile

lockedZip = zipfile.ZipFile("MusicSheets.zip")
password = "ComicSans"
lockedZip.extractall(pwd=password.encode())


# Create another reference, this time to a locked ZIP file


# Variable used to store the password string


# Run the `.extractall()` function with a password

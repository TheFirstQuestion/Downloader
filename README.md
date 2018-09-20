# Downloader

## Dependencies
* [virtualenv](https://github.com/pypa/virtualenv): `sudo pip3 install virtualenv`; `virtualenv ENVdownloader`; `source ENVdownloader/bin/activate`
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): `pip install python-telegram-bot`
* [requests](http://docs.python-requests.org/en/latest/): `pip install requests`
* [newspaper](https://github.com/codelucas/newspaper): `pip install newspaper3k`
* [Set up a bot with BotFather](https://core.telegram.org/bots#6-botfather): put token in new file `token.txt`


## Installation
* Move downloaderWrapper.sh to  /usr/bin/downloaderWrapper: `mv downloaderWrapper.sh /usr/bin/downloaderWrapper`
* Make the script executabl: `sudo chmod +x /usr/bin/downloaderWrapper`
* Move the service file: `mv downloader.service /usr/lib/systemd/system/my.service`
* Reload all systemd service files: `sudo systemctl daemon-reload`
* Check that it is working by starting the service: `sudo systemctl start downloader`


## Usage
_All commands are sent to the Telegram bot. By default, Telegram autocorrects `--` to `—`. Either is acceptable._

`https://example.com/my-url-here`
* If a file (mp4, png, etc.): downloaded
* If an open directory: download recursively down, preserving directory structure
* If a special website: downloaded according to rules
* Otherwise: Downloaded as an article

`https://example.com/my-url-here --website`
* One-time download of website for offline viewing

`https://example.com/my-url-here --mirror`
* Download website once, add to watchlist; will redownload when website is updated

---

## Design Info
**Use Case:** Take a link to a file, website, or webpage and send it via Telegram/Signal. The server downloads the file, adds appropriate metadata to a database, and tweets that the download was successful.

**End Result:** Depends on what and how you want it downloaded:
* Image/Video/PDF: download just the file, guess a filename, add to folder for manual sorting, attempt OCR
* YouTube: download video or playlist
* Open Directory: Download all files recursively, same structure and naming
* Article: Copy just main text of page; ignore header, footer, ads, etc.
* Website (Static): Copy the website so that it can be viewed from server as if live, one-time download
* Website (Mirror): Watch the website for any updates, re-download as above to keep copy in sync, option to keep old versions around

**Metadata:**
* URL downloaded from
* Dates and times: request download, download start, download end
* Number of files and size of each
* Possible tags
* OCR results, if applicable


## Outline
* Parse URL and any flags from Telegram, pass to Downloader service on server
* Add URL and arguments to text file for downloading at appropriate time
* Call `wget` on each URL with appropriate arguments
* If download fails, skip and come back to it
* Pass resulting file to applicable other programs for OCR, cleaning, etc.
* Remove URL from text file
* Move metadata and file to To Be Sorted folder

---

## Example Links
* Image: https://i.pinimg.com/736x/72/77/86/7277863f8d5bdfe85fe792610a6716c7--fandom-quotes-dont-worry.jpg
* PDF: https://www.nchs.cc/wp-content/uploads/2018/08/SNC-Guidanc18080712200.pdf
* Article: https://www.evilmadscientist.com/2008/how-to-organize-your-lego-bricks-for-efficient-building/
* Open Directory: http://avadl.uploadt.com/Movie/250/
* Website (Static): https://www.cs.iupui.edu/~ajharris/230/
* Website (Mirror): https://jither.net/


## Special Websites
* Archive of Our Own: https://archiveofourown.org/works/12167772/chapters/27616923
* Buzzfeed: https://www.buzzfeed.com/amphtml/eleanorbate/shes-beauty-shes-grace-she-punched-malfoy-in-the-face
* Fanfiction.net
* Musescore
* YouTube

---

# TODO
* Articles: retain styles
* Articles: download images and use relative path
* Edge cases for identifying file type
* Useful options for `wget` (-c?)
* Sending files directly
* Ability to define special websites

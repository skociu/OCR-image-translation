# Requirements: Make sure the following modules are installed
<code>
pytesseract, googletrans
</code>

# Background on the script
The script uses a text image (i.e. French) from an open source such as Gutenberg and then uses pytesseract to extract its text using OCR and feeds this text into google translate for translation from the French language into English.
Once the translation is done, it can be viewed in your text editor (i.e. SublimeText)
Note: The script will check all the files ending with ".png" and attempt to extract the text from them


# Sample Images
<img src="extract01.png" width="500px">
<img src="extract02.png" width="500px">
<img src="extract03.png" width="500px">

# Translated Image Texts
translated_extract01.txt
translated_extract02.txt
translated_extract03.txt

# Sources
Gutenberg http://www.gutenberg.org/files/41211/41211-h/41211-h.htm
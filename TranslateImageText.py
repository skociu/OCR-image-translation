from PIL import Image
import pytesseract
import os
import subprocess
from googletrans import Translator

class Translation:
    '''The script uses a text image (i.e. French) from an open source such as Gutenberg and then uses pytesseract to extract its text using OCR and feeds this text into google translate for translation from the French language into English.
    Once the translation is done, it can be viewed in your text editor (i.e. SublimeText)'''
    def __init__(self, *a):
        self.pytesseract_image_language = pytesseract_image_language
        self.from_language = from_language
        self.to_language = to_language
        self.extract_img = extract_img
        self.extract_file = extract_file
        self.translate_file = translate_file

    def extract_image_text(self):
        #https://github.com/tesseract-ocr/tesseract/wiki/Data-Files
        #The link above will give you language codes to use 
        #i.e. code 'fra' = French; 'sqi' = Albanian; 'eng' = English
        pytesseract_image_language = self.pytesseract_image_language
        img = Image.open(self.extract_img)
        text = pytesseract.image_to_string(img, lang=pytesseract_image_language).encode('utf-8')
        text = text.replace('\n', '\n ')
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
        text = text.replace('!', '!\n')
        text = text.replace('?', '?\n')
        return text

    def translate_image_text(self, text):
        #for more information on googletrans
        #http://py-googletrans.readthedocs.io/en/latest/
        #Note: type print(googletrans.LANGUAGES) to see supported languages
        # i.e. 'fr' = French; 'sq' = Albanian; 'en' = English
        translator = Translator()
        from_language = self.from_language
        to_language = self.to_language
        translation = translator.translate(text, 
            src=from_language, dest=to_language).text.encode("utf-8")
        return translation

    def write_image_text(self):
        f = open(self.extract_file, 'w')
        f.write(self.extract_image_text())
        f.close()

    def remove_extract_file(self):
        os.remove(self.extract_file)


    def write_translation(self):
        f1 = open(self.extract_file, 'r')
        with open(self.translate_file, 'w') as f:
            for i, line in enumerate(f1, 1):
                f.write(str(i) + ') ' + line)
                f.write(str(i) + ') ' + self.translate_image_text(line)+ '\n\n')
        f.close()

    def view_translation(self):
        subprocess.Popen(['subl', self.translate_file])

    
if __name__ == "__main__":
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.endswith(".png"):
            pytesseract_image_language = 'fra'
            from_language = 'fr'
            to_language = 'en'
            extract_img = "{}".format(f)
            extract_file = "{}.txt".format(os.path.splitext(f)[0])
            translate_file = "translated_{}.txt".format(os.path.splitext(f)[0])
            t=Translation()
            t.extract_image_text()
            t.write_image_text()
            t.write_translation()
            t.remove_extract_file()
            #t.view_translation()
            print('done')
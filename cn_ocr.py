'''
steps to run code : 
pip install cnocr
pip install onnxruntime

python3 cn_ocr.py

'''

from cnocr import CnOcr
import re


ocr = CnOcr()
res = ocr.ocr_for_single_line('./helloworld.jpg')
t = res['text']
print("Predicted Chars:", t)
words = re.split(r'[\s,!.?]+', t)
words = [word for word in words if word]
print(words)

chinese_words = []
english_words = []
for word in words:
    if any(ord(char) > 127 for char in word):
        chinese_words.append(word)
    else:
        english_words.append(word)

print("Chinese words:", chinese_words)
print("English words:", english_words)

import os
import easyocr
from PIL import Image

folder = r'd:\Mahesh\Code Library\Ethans-set\Nexgen\Python\Task -2\aws-console-&-linux'
reader = easyocr.Reader(['en'], gpu=False)

for filename in sorted(os.listdir(folder)):
    if not filename.lower().endswith('.png'):
        continue
    img_path = os.path.join(folder, filename)
    print('===', filename, '===')
    try:
        result = reader.readtext(img_path, detail=0, paragraph=True)
        text = '\n'.join(result[:80])
        print(text[:5000])
    except Exception as e:
        print('OCR_ERROR:', e)
    print('\n')

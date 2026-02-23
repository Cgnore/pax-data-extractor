import re

def extract_pax_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # 1. Grup (PAX...) ve 2. Grup (BÜYÜK HARFLİ isimler) 
        # Aradaki .*? sembolü ile gereksiz küçük harfli yazıları dahil etmiyoruz.
        pattern = re.compile(r'(PAX\d{9}).*?([A-ZÇĞİÖŞÜ]+(?:\s+[A-ZÇĞİÖŞÜ]+)*)')
        matches = pattern.finditer(content)
        
        for match in matches:
            # Sadece 1. ve 2. grupları yan yana yazdırarak aradaki kelimeleri eliyoruz!
            print(f"{match.group(1)} {match.group(2)}")

if __name__ == '__main__':
    extract_pax_data('testing.txt')
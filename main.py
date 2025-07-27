import os
from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(image):
    """Görsel kalitesini artıran fonksiyon"""
    # Kontrast artırma
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)
    
    # Keskinlik artırma (hafif)
    image = image.filter(ImageFilter.SHARPEN)
    
    # Renk doygunluğunu artırma
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.1)
    
    return image

def create_mipmap_folders():
    folders = {
        'mipmap-mdpi': (48, 48),
        'mipmap-hdpi': (72, 72),
        'mipmap-xhdpi': (96, 96),
        'mipmap-xxhdpi': (144, 144),
        'mipmap-xxxhdpi': (192, 192)
    }
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    return folders

def process_image(input_path, output_folders):
    try:
        original_img = Image.open(input_path)
        print(f"Orijinal resim yüklendi: {original_img.size}")
        
        # Orijinal resmi iyileştir
        enhanced_img = enhance_image(original_img)
        
        for folder, size in output_folders.items():
            # Yüksek kaliteli yeniden boyutlandırma
            resized_img = enhanced_img.resize(size, Image.LANCZOS)
            
            # Kenar yumuşatma (anti-aliasing)
            resized_img = resized_img.filter(ImageFilter.SMOOTH)
            
            # PNG optimizasyonu
            output_path = os.path.join(folder, 'ic_launcher.png')
            resized_img.save(output_path, optimize=True, quality=95)
            
            print(f"✓ {size[0]}x{size[1]} | {output_path}")
            
        print("\n✔ Tüm ikonlar başarıyla oluşturuldu!")
        print("📁 Klasör yapısı:")
        for folder in output_folders:
            print(f"- {folder}/ic_launcher.png")
        
    except Exception as e:
        print(f"❌ Hata: {str(e)}")

if __name__ == "__main__":
    input_image = 'image.png'
    mipmap_folders = create_mipmap_folders()
    
    if os.path.exists(input_image):
        print("✨ Resim iyileştirme ve boyutlandırma başlıyor...\n")
        process_image(input_image, mipmap_folders)
    else:
        print(f"❌ Hata: '{input_image}' bulunamadı!")
        print("Lütfen script ile aynı dizine 'tcdd.png' dosyasını yerleştirin.")

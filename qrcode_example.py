import qrcode
from PIL import Image

logo_aptrg = 'aptrg1.png'

logo = Image.open(logo_aptrg)

#lebar base
lebar_base = 100

#atur ukuran gambar

lebar_persentase = (lebar_base/float(logo.size[0]))
ukuran_tinggi = int((float(logo.size[1])*float(lebar_persentase)))
logo = logo.resize((lebar_base, ukuran_tinggi), Image.ANTIALIAS)
koreksi_error = qrcode.constants.ERROR_CORRECT_H
kode_QR = qrcode.QRCode(error_correction = koreksi_error)

url = 'https://linktr.ee/APTRG'

kode_QR.add_data(url)

kode_QR.make()

QRcolor = 'Red'

gambar_qr = kode_QR.make_image(fill_color=QRcolor, back_color = 'white').convert('RGB')

pos = ((gambar_qr.size[0] - logo.size[0]) // 2,
    (gambar_qr.size[1] - logo.size[1]) // 2)

gambar_qr.paste(logo, pos)

gambar_qr.save('image.png')

print('QR generated')



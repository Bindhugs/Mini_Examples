import qrcode

data = input("Enter the text or URL: ").strip() #strip is used to remove any whitespaces from the input
file =input("Enter the filename(save using jpg): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file)
print(f'QR code saved as {file}')
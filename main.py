import qrcode
import qrcode.image.pil

ssid = input("Enter the Wi-Fi network name (SSID): ")
password = input("Enter the Wi-Fi network password: ")
encryption = input("Enter the encryption type (WPA, WEP, or leave empty if no password): ")

wifi_info = f"WIFI:S:{ssid};T:{encryption};P:{password};;"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_info)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("wifi_qrcode.png")

print("QR code generated and saved as 'wifi_qrcode.png'")

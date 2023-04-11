import qrcode

# img = qrcode.make('https://www.itgenius.co.th')
# type(img)
# img.save('product_qrcode/qrcode.png')

print("QRCode Generator Program")
print("Please type 'quit' to exit program")

while True:
    product_data = input("Please type product code: ")
    if product_data == 'quit':
        print("Thank you for using QRCode Generator Program")
        break
    if len(product_data) == 5:
        # print(product_data)
        img = qrcode.make(product_data)
        type(img)
        img.save(f"product_qrcode/{product_data}.png")
    else:
        print("Please type 5 digits product code")

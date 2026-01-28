import segno

url = "https://kimiecozy.github.io/portofolio3/"
qr = segno.make(url, error='h') 
qr.save("images/qrcode-portfolio.png", scale=10) 



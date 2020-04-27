from sec_edgar_downloader import Downloader

f = open('companies.txt', 'r')
stickers = f.read().splitlines()
f.close()

dl = Downloader(".")

after_date = "20090101"
before_date = "20200427"

for sticker in stickers:
  dl.get("10-K", sticker, after_date="20100101", before_date="20200325")


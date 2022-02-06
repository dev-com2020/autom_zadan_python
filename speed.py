import speedtest

speed = speedtest.Speedtest()
download = speed.download()
upload = speed.upload()
print(f'Download: {download}')
print(f'Upload: {upload}')

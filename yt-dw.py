from pytube import YouTube

link = input("Lütfen İndireceğiniz Vidio Linkini girin")
yt = YouTube(link)
yr = yt.streams.get_highest_resolution()

print("vidio iniyo bekleyin")
wait = 1
for i in range(3):
    print("{}/3".format(wait))
    wait += 1
yr.download()
print("vidio indi")
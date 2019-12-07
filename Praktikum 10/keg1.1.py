import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ""
kamus = {"nama":"Rahmad Nur Sulistyawan",
         "NIM":"L200190194",
         "alamat":"Maaf, perintah ini tidak dimengerti",
         "keluar":"siapppp!!!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, perintah ini tidak dimengerti")

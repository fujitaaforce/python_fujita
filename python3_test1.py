# 課題1~6

class MP3Player :
    def play_music(self) :
        print("音楽を再生します。")
    def next_song(self) :
        print("次の曲を再生します。")
    def previous_song(self) :
        print("前の曲を再生します。")
    def stop_music(self) :
        print("音楽を止めます。")

mp3player = MP3Player()
mp3player.play_music()
mp3player.next_song()
mp3player.previous_song()
mp3player.stop_music()

class CellPhone :
    def __init__(self, tel_number, mail_address) :
        self.tel_number = tel_number
        self.mail_address = mail_address
    def call(self):
        print("{}から発信します。".format(self.tel_number))
    def send_mail(self):
        print("{}から送信します。".format(self.mail_address))

cellphone = CellPhone("00011112222", "k.fujita@mail.ne.jp")
cellphone.call()
cellphone.send_mail() 

class SmartPhone(MP3Player,CellPhone) :
    def funcname(self):
        pass

smartPhone = SmartPhone("00011112222", "k.fujita@mail.ne.jp")
smartPhone.play_music()
smartPhone.next_song()
smartPhone.previous_song()
smartPhone.stop_music()
smartPhone.call()
smartPhone.send_mail()
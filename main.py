import requests
import telebot
import os

from pytube import YouTube
from auth_data import token




def telegram_bot(token):
    bot = telebot.TeleBot(token)



    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hi! Paste link of the video and i will download it for you! Maximum 50Mb')

    @bot.message_handler()
    def get_link(message):
        global id
        id = message.chat.id
        url = message.text
        bot.send_message(id, 'Got your link')
        download_video(url)


    def send_video(stream, path):
        bot.send_message(id, 'Downloaded!')
        bot.send_video(id, video=open('videos/video.mp4', 'rb'), supports_streaming=True)
        os.remove('videos/video.mp4')

    def download_video(url):
        try:
            video_object = YouTube(url , on_complete_callback = send_video)
            high_res = video_object.streams.filter(res = '480p', file_extension='mp4')[0]
            if high_res.filesize / 1048576 < 50:
                bot.send_message(id, 'Downloading...')
                high_res.download(output_path='C:\Projects\Python\Pycharm\Teledownload\/videos', filename='video.mp4')
            else:
                bot.send_message(id, 'Video is too big! Your maximum is 50Mb')
        except Exception as exc:
            bot.send_message(id, 'Damn, something went wrong...May be check your link!')
            print(exc)










    bot.polling()

def main():
    telegram_bot(token)





if __name__ == '__main__':
    main()



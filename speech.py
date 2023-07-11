import datetime
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
def talk(words):
 # print(words)
 # os.system("say "+words)
     engine = pyttsx3.init()
     engine.setProperty('rate', 150) # скорость речи
     engine.setProperty('volume', 0.7) # громкость (0-1)
     engine.say(words)
     engine.runAndWait()
def command():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Говорите !")
         talk("Говорите !")
         r.pause_threshold = 1 # пауза 1 сек
         r.adjust_for_ambient_noise(source, duration=1) # не слушаем шумы
         audio = r.listen(source)
     try:
         zadanie = r.recognize_google(audio, language="ru-RU").lower()
         print("Вы сказали: " + zadanie)
         talk("Вы сказали... "+ zadanie)
         r.pause_threshold = 1 # пауза 1 сек
     except sr.UnknownValueError:
         talk("Не понимаю Вас!")
         zadanie = command()
     return zadanie

def time_to_text():
     #перевод времени в текст
     dict_hours = {1: 'час', 2: 'часа', 3: 'часа', 4: 'часа', 5: 'часов', 6:
    'часов',
     7: 'часов', 8: 'часов', 9: 'часов', 10: 'часов', 11: 'часов', 12:
    'часов',
     13: 'часов', 14: 'часов', 15: 'часов', 16: 'часов', 17: 'часов',
    18: 'часов',
     19: 'часов', 20: 'часов', 21: 'час', 22: 'часа', 23: 'часа', 0:
    'часов'}
     dict_minutes = {
         'минута': [1, 21, 31, 41, 51],
         'минуты': [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54],
         'минут': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         25, 26, 27, 28, 29, 30,
         35, 36, 37, 38, 39, 40,
         45, 46, 47, 48, 49, 50,
         55, 56, 57, 58, 59] }
     now = datetime.datetime.now()
     h = now.hour
     m = now.minute
     str_time = str(h) + dict_hours[h] + ' ... '
     for minutes in dict_minutes:
         if m in dict_minutes[minutes]:
             str_time += str(m) + ' ' + minutes
             break
     return str_time
def ParseZadanie(zadanie):
     """Разбор голосового задания/команды """
     if 'открой почту' in zadanie:
         talk('Хорошо, ОТКРЫВАЮ ПОЧТУ!')
         URL='https://mail.ru'
         webbrowser.open(URL)
     elif ('сколько времени' in zadanie) or ('который час' in zadanie) or ('сколько время' in zadanie) :
         talk(time_to_text())
     elif ('как тебя зовут' in zadanie) or ('как твоё имя' in zadanie) or ('кто ты' in zadanie):
         talk('Меня зовут Татьяна! А как зовут тебя?')
     elif 'открой яндекс' in zadanie:
         talk('Хорошо, ОТКРЫВАЮ ЯНДЕКС!')
         URL='https://ya.ru'
         webbrowser.open(URL)
     elif 'стоп' in zadanie:
         talk('Хорошо, заканчиваем разговор... До встречи !')
         sys.exit()
# узнаем какие голоса есть в системе
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices: # голоса и параметры каждого
    print('------')
    print(f'Имя: {voice.name}')
    print(f'ID: {voice.id}')
    print(f'Язык(и): {voice.languages}')
    print(f'Пол: {voice.gender}')
    print(f'Возраст: {voice.age}')
    # Задать голос по умолчанию
    # Попробовать установить предпочтительный голос
for voice in voices:
    if 'Tatyana' in voice.name :
        engine.setProperty('voice', voice.id)
talk('Привет, меня зовут Татьяна! Давай поговорим!')
while True:
    ParseZadanie(command())
    talk("Поговорим еще ?")

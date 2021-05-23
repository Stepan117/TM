#from translate import Translator
from deep_translator import GoogleTranslator
import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

flag = 1

def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите:")
		print("-----------------------------------------------")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Русский:")
		print(zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

print("---Перевод с русского на французский---")
print(" ")
while(flag == 1):
    zadanie = command()

    #translator= Translator(from_lang="russian",to_lang="spanish")
    #translation = translator.translate(zadanie)
    translator = GoogleTranslator(source='russian', target='french')
    translation = translator.translate(zadanie)
    print("-----------------------------------------------")
    print("Французский:")
    print(translation)
    print("-----------------------------------------------")

    engine = pyttsx3.init()     # инициализация движка

    # зададим свойства
    engine.setProperty('rate', 150)     # скорость речи
    engine.setProperty('volume', 0.9)   # громкость (0-1)

    es_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
    engine.setProperty('voice', es_voice_id)
    engine.say(translation)
    engine.runAndWait()
    print("Продолжить? (y/n)")
    k = input()
    if (k == 'y'):
        flag = 1
    else:
        flag = 0


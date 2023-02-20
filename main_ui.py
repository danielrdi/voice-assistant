import pyttsx3

# Instânciando o mecanismo de síntese de fala
engine = pyttsx3.init()

# Defina a string que você deseja reproduzir em áudio
#texto = "Olá, mundo!"

# Adiciona a fila de reprodução
#engine.say(texto)

# reproduzir a fila
#engine.runAndWait()

def voice_now(texto):
    engine.say(texto)
    engine.runAndWait()
    
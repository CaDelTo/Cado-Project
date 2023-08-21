import pygame
import time
import numpy as np

# Inicializa pygame y el reproductor de audio
pygame.init()
pygame.mixer.init()

# Frecuencia del tono
frequency = 440  # Frecuencia de la nota A4

# Duración del tono en milisegundos
tone_duration = 300

# Genera la forma de onda del tono utilizando numpy
tone_wave = np.sin(2 * np.pi * frequency * np.arange(44100 * tone_duration // 1000) / 44100)

# Aplica un decaimiento exponencial para hacerlo más suave
decay = np.exp(-np.arange(44100 * tone_duration // 1000) / (44100 * tone_duration // 1000 / 5))
tone_wave *= decay

# Normaliza la onda
tone_wave /= np.max(np.abs(tone_wave))
tone_wave = (tone_wave * 32767).astype(np.int16)

# Crea un objeto de sonido de pygame
sound = pygame.sndarray.make_sound(np.column_stack((tone_wave, tone_wave)))

# Ajusta el volumen del sonido (0.0 a 1.0)
sound.set_volume(0.2)  # Cambia este valor para ajustar el volumen

# Reproduce el tono
sound.play()

# Espera hasta que termine el tono
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(30)

# Detén pygame
pygame.quit()


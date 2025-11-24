# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()

# #Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Meet!"
# # text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# from elevenlabs import ElevenLabs
# from elevenlabs import play

# ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

#     # NEW METHOD
#     audio = client.text_to_speech.convert(
#         voice_id="EXAVITQu4vr4xnSDxMaL",   # Rachel (official voice ID)
#         model_id="eleven_multilingual_v2",
#         text=input_text,
#         output_format="mp3_22050_32"
#     )


#     # Save MP3
#     with open(output_filepath, "wb") as f:
#         for chunk in audio:
#             f.write(chunk)

# # text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")
# # print("Saved:", output_filepath)

# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Meet, autoplay testing!"
# # text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")



# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS
import subprocess
import platform
from elevenlabs import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

# -------------------------------
# gTTS FUNCTION (OLD + WORKING)
# -------------------------------
def text_to_speech_with_gtts(input_text, output_filepath):
    audioobj = gTTS(text=input_text, lang="en", slow=False)
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c',
                f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print("Audio playback error:", e)



# ---------------------------------------------
# NEW FIXED ELEVENLABS SDK – FINAL WORKING CODE
# ---------------------------------------------
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # NEW SDK FORMAT (REQUIRED — generate() NO LONGER EXISTS)
    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",        # Rachel (official ElevenLabs voice)
        model_id="eleven_turbo_v2",
        text=input_text,
        output_format="mp3_22050_32"
    )

    # Save audio file (required in new SDK)
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    # Auto-play audio (same logic)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c',
                f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print("Audio playback error:", e)



# -------------------------------
# TEST CALL
# -------------------------------
input_text = "Hi this is Ai with Meet, autoplay test using ElevenLabs!"
text_to_speech_with_elevenlabs(
    input_text,
    output_filepath="elevenlabs_testing_autoplay.mp3"
)

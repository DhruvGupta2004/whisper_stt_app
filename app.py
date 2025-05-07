import streamlit as st
import whisper
import tempfile
from pydub import AudioSegment

st.title("🎙️ Whisper Speech-to-Text App")

st.write("Upload an mp3 audio file, and the Whisper model will transcribe it to text.")

uploaded_file = st.file_uploader("Choose an audio file (mp3)", type=["mp3"])

if uploaded_file is not None:
    # Save the uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    # Convert mp3 to wav using pydub
    audio = AudioSegment.from_mp3(temp_audio_path)
    wav_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(wav_temp.name, format="wav")

    st.info("Loading Whisper model... This might take a moment.")

    # Load Whisper model
    model = whisper.load_model("base")

    st.success("Model loaded! Starting transcription...")

    # Transcribe
    result = model.transcribe(wav_temp.name)
    st.subheader("📝 Transcribed Text")
    st.write(result["text"])

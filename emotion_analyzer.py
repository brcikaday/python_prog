# from pysentimiento import create_analyzer
# analyzer = create_analyzer(task = "emotion" , lang = "en")

# result = analyzer.predict("the boy is happy")

# print(result.output)

from transformers import pipeline
import gradio as gr


emotion_model = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")


def detect_emotion(text):
    results = emotion_model(text)
    primary_emotion = results[0]["label"]
    return primary_emotion


interface = gr.Interface(
    fn=detect_emotion,
    inputs=gr.Textbox(lines=5, placeholder="Enter your comment here..."),
    outputs=gr.Textbox(label="Emotion Detection Results"),
    title="Emotion Detection App",
    description="Enter a comment to detect the emotion."
)

interface.launch(share = True)

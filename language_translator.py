from translate import Translator
import gradio as gr
import pyttsx3 



def translater(text,language):
    translator= Translator(to_lang=language)
    translation = translator.translate(text)
    
    return translation
    

interface = gr.Interface(fn = translater , inputs= ["textbox","textbox"],outputs="textbox")
interface.launch()
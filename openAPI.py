import openai
import gtts
import pyttsx3

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

completion = openai.Completion.create(engine="text-davinci-003",prompt="small motivation story", max_tokens=1000)


if(completion.choices):
    print(completion.choices[0].text)
    mytext = completion.choices[0].text
    engine = pyttsx3.init()
    engine.setProperty('volume',1.0)
    engine.save_to_file(mytext, 'test1.mp3')
    engine.runAndWait()
    audio = gtts.gTTS(text=mytext, lang="en", tld="co.in", slow=False)
    audio.save('hello.mp3')
    print("---- Completed ---")
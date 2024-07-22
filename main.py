import os
import yt_dlp
import whisper
from moviepy.editor import VideoFileClip
from openai import OpenAI
from pydub import AudioSegment
import time
import google.generativeai as genai
from prompt import interview_assistant_prompt

genai.configure(api_key="AIzaSyCymMKHaT3YaD1q0GFL3EM1icoKFEem4aM")
groq = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

class text_extraction_from_video:
    def __init__(self,video_url, file_name):
        self.video_url = video_url
        self.video_path = r"video/"
        self.audio_path = r"audio/"
        self.file_name = file_name
        
    def download_video(self, url, download_path):
        ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_path, self.file_name+'.mp4') #'%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)
        return video_file_path
        
    def extract_audio(self, video_file_path, audio_file_path):
        print(video_file_path+self.file_name+'.mp4', audio_file_path+self.file_name+'.mp3')
        video_clip = VideoFileClip(video_file_path+self.file_name+'.mp4')
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file_path+self.file_name+'.mp3')
        return audio_file_path+self.file_name+'.mp3'
    
    def compress_audio_file(self, audio_path, bitrate="64k"):
        audio = AudioSegment.from_file(audio_path)
        audio.export(audio_path, format="mp3", bitrate=bitrate)
        print(f"Compressed audio saved at: {audio_path}")
        return 0
    
    def audio_to_text(self, audio_path):
        model = whisper.load_model("base")
        extracted_text = model.transcribe(audio_path)
        return extracted_text
    
    def audio_to_text_grooq(self, audio_path):
        with open(audio_path, "rb") as audio_file:
            transcript = groq.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                response_format="text"
            )
        return transcript
    def text_extraction_from_video_main(self):
        downloaded_video = self.download_video(self.video_url, self.video_path)
        print(downloaded_video)
        extracted_audio = self.extract_audio(self.video_path, self.audio_path)
        print(extracted_audio)
        extracted_audio = "audio/sample1.mp3"
        print(extracted_audio)
        # self.compress_audio_file(extracted_audio,bitrate="64k")
        extracted_text = self.audio_to_text(extracted_audio)
        print(extracted_text)
        with open("extracted_text/extracted_text.txt", "w") as f:
            f.write(extracted_text["text"])
        return extracted_text
   
class ai_suggestion:
    def __init__(self, domain, question):
        self.domain = domain
        self.question = question
        
    def get_gemini_response(self, prompt):
        model = genai.GenerativeModel("gemini-1.5-flash",  generation_config =  {
                                                            "temperature": 0.1,
                                                            "max_output_tokens": 8192,
                                                            "response_mime_type": "application/json"
                                                            })
        response = model.generate_content(prompt)
        # return self.response_formatter(response.text)
        return response.text
    
    def ai_suggestion_main(self):
        with open("extracted_text/extracted_text.txt", "r") as f:
            data = f.read()
        prompt = interview_assistant_prompt(data, self.domain, self.question)
        raw_response = self.get_gemini_response(prompt)
        print(raw_response)
        return 0
 
start = time.time()    

# class_obj = text_extraction_from_video("https://www.youtube.com/watch?v=KIA9_9RPETg&t=2672s", "sample1")
# res = class_obj.text_extraction_from_video_main()

ai_suggestion_object = ai_suggestion("data science", "what is the difference between vectors and scalar?")
ai_suggestion_response = ai_suggestion_object.ai_suggestion_main()
end = time.time()
print(end-start)
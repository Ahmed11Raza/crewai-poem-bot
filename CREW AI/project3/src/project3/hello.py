from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyDX12WEBy2ZQQav-SLfGqckw3VjKuIuq7s"


def  call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
    )
    print(response['choices'][0]['message']['content'])

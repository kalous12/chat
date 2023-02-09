import openai
import pyttsx3
import time

# Set the API key
openai.api_key = ""




people = "You: \n"
ai = "openai: \n"

def chat_init() :
    flag=1
    mode=0
    while flag :
        mode = input("选择你的模式\n1.对话\n2.翻译(英翻中)\n3.翻译(中翻英)\n0.退出\n")
        if mode == "1":
            flag = 0
            front =  ""
            return front
        elif mode == "2":
            flag = 0
            front = "translate to chinese :"
            return front
        elif mode == "3":
            flag = 0
            front = "translate to english :"
            return front
        elif mode == "0":
            exit()
        else:
            print("重新选择")

def get_time() :
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return local_time

def chat_robot(prompt) :
    # Generate text
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Print the generated text
    message = completion.choices[0].text
    str = message[2:]

    return str

def log(prompt,str,local_time) :
    f = open("openai.log", "a+")
    f.write("------------------------------")
    f.write("\n" + local_time + "\n")
    f.write(people + prompt + "\n")
    f.write(ai + str +"\n")
    f.close() 

def speak(str,rate=150) :
    #initialize the engine 
    engine = pyttsx3.init() 
    #set the rate 
    engine.setProperty('rate', rate) 
    #speak 
    engine.say(str) 
    #run and wait for completion 
    engine.runAndWait()

def chat(prompt) :

    while True:    
        try:    
        #获取交流结果
            str = chat_robot(prompt)
        except openai.error.RateLimitError :
            print("RateLimit speak , please wait some time ")
            time.sleep(5)
            continue

        return str

def main() :
    front = chat_init() 
    while True:

        # Define the prompt
        str = input("You：\n")
        prompt = front + str
        
        str = chat(prompt)

        #显示回答
        print( ai + str)
        #获取时间
        local_time = get_time()

        log(prompt , str , local_time)

 
main()


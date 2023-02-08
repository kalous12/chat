import openai
import pyttsx3
import time

# Set the API key
openai.api_key = "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"

people = "You: \n"
ai = "openai: \n"
log_name = "openai.log"

#talk type to choose the best model to use
talk_type = "text"

def chat_init() :
    flag=1
    mode=0
    global talk_type
    while flag :
        mode = input("选择你的模式\n0.退出\n1.对话\n2.翻译(+语言:)\n3.编程(+语言:)code\n4.编程(+语言:)\n")
        if mode == "1":
            flag = 0
            front =  ""
            return front
        elif mode == "2":
            flag = 0
            front = "translate to "
            return front
        elif mode == "3":
            flag = 0
            front = "write "
            talk_type = "code"
            return front
        elif mode == "4":
            flag = 0
            front = "write "
            return front
        elif mode == "0":
            exit()
        else:
            print("重新选择")

def get_time() :
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return local_time

def chat_robot(prompt) :

    #for code "code-davinci-002" is best
    if talk_type == "code" :
        model_engine = "code-davinci-002"

    #for text "text-davinci-003" is best
    elif talk_type == "text":
        model_engine = "text-davinci-003" 

    #you can use ada
    else :
        model_engine = "text-davinci-003"


    # Generate text
    completion = openai.Completion.create(
        engine=model_engine,
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
    f = open(log_name, "a+")
    f.write("\n------------------------------")
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

def main() :
    front = chat_init() 

    while True:
        # Define the prompt
        str = input("You: \n")
        prompt = front + str
        #获取交流结果
        str = chat_robot(prompt)
        #显示回答
        print( ai + str)
        #获取时间
        local_time = get_time()
        #记录log
        log(prompt , str , local_time)

        # speak(str,100)
        # 
        # 
def image(str):
    response = openai.Image.create(
        prompt=str,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url'] 
    return image_url

image_url = image("Straight green hair, red eyebrows, yellow eyes, black lips, a Chinese face, and a white-skinned girl.")
print(image_url)
main()

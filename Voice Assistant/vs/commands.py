from imports import *
from passwordgui import *
def takecommand(voice_data):
    if 'I am Iron Man ' in voice_data:
        speak("shall I activate your armour sir")
    elif "what's up" in voice_data:
        wishme()
    elif "what's your name" in voice_data:
        speak('my name is jarvis')
    elif "what time" in voice_data:
        Time = datetime.datetime.now().strftime("%I:%M")
        speak(Time)
    elif "who made you" in voice_data or "who created you" in voice_data:
        speak("I have been created by Nickhil Earla.")
    elif 'tell me a joke' in voice_data:
        speak(pyjokes.get_joke())
    elif 'open Chrome' in voice_data:
        appli = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(appli)
    elif 'open fortnite' in voice_data:
        appli = r"C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping.exe"
        os.startfile(appli)
        speak("opening fortnite, sir!")
    elif 'testing' in voice_data:
        takevoice()
    elif "what's the weather" in voice_data:
        api_key = "93d2c1b8cf6096171682f3e90b6a8780"  # Enter the API key you got from the OpenWeatherMap website
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        voice_data = takevoice()
        city_name = voice_data
        complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        weather_description = z[0]["description"]

        speak(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
                "\n looks like a " +
                        str(weather_description))

    elif "open Youtube" in voice_data:
        webbrowser.open_new_tab('http://www.youtube.com')
    elif "what's the temperature" in voice_data or "temperature" in voice_data:
        search = voice_data.replace("what's", '')
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        print(temp)
        speak(f"{search} is {temp}")
    elif 'play' in voice_data:
        song = voice_data.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'feed my unicorn unicorn food'in voice_data:
        speak("nice try eeshae baby, thats not happening anytime soon. HAHHAHAHAH. tick, tick, tick, tock,,,,, BOOOMMMMMMMMMM.....jkjkjkjk I will feed your unicorn some food")
    elif 'Execute Order 66' in voice_data:
        speak("the jedi shall be destroyed, I have the high ground anekan")
    elif 'open Roblox' in voice_data:
        appli = r"C:\Users\Nickh\Desktop\Roblox Player"
        os.startfile(appli)
        speak("opening roblox sir")
    elif "kick your Founders ass" in  voice_data:
        speak("i'm sorry, I can't do that because he is god")
    elif 'search'  in voice_data:
        voice_data = voice_data.replace("search", "")
        webbrowser.open_new_tab(voice_data)
    elif 'Wikipedia' in voice_data:
        speak('Searching Wikipedia')
        voice_data =voice_data.replace("Wikipedia", "")
        voice_data=voice_data.replace("on",'')
        results = wikipedia.summary(voice_data, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "what's the date" in voice_data:
        search = voice_data.replace("what's", '')
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        print(temp)
        speak(f"{search} is {temp}")
    elif "Panda Express" in voice_data:
        speak("getting orange chicken, sir")
        webbrowser.open_new_tab("https://www.pandaexpress.com/")
    elif "Jarvis find my phone now" in voice_data:
        speak("locating samsung device through samsung data bases, sir. locating. firewall surpassed, locating device now sir. ringing phone imediatly")
        webbrowser.open_new_tab("https://findmymobile.samsung.com/#home")
        speak("please log in and click ring sir")
    elif "Youtube" in voice_data:
        ytvid = voice_data.replace("Youtube", '')
        ytvid1 = ytvid.replace("on",'')
        ytvid2 = ytvid1.replace("Play",'')
        
        pywhatkit.playonyt(ytvid2)
    elif "Disney Plus" in voice_data:
        speak("opening disney plus right now, sir")
        webbrowser.open_new_tab("https://www.disneyplus.com/home")
        speak("disney plus has been opened")
    elif "Netflix" in voice_data:
        speak("opening netflix, sir")
        webbrowser.open_new_tab("https://www.Netflix.com")
    elif "Amazon" in voice_data:
        speak("opening amazon now")
        webbrowser.open_new_tab("https://www.Amazon.com")
        speak("amazon launched, sir")
    elif "school Portal" in voice_data:
        speak("the good one or the trash one?")
        ans=input("type good or bad school: ")
        if ans=="good":
            speak("opening the real school Portal")
            webbrowser.open_new_tab("https://portal.srvusd.net/")
        else:
            speak("good one hahahahaha, that dump of a school can't afford one hahahaha.")
        
    elif "Caillou" in voice_data:
        speak("playing Caillou theme song on youtube, cough the awesome one, yass")
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=H8u6gON8X6E")
    elif "add" in voice_data:
          speak("the first and second number please")
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          print(num1, "+", num2, "=", add(num1, num2))
          x = add(num1, num2)
          speak("the answer is")
          speak(x)
    elif "subtract" in voice_data:
          speak("the first and second number please")
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          print(num1, "-", num2, "=", subtract(num1, num2))
          x = subtract(num1, num2)
          speak("the answer is")
          speak(x)
    elif "multiply" in voice_data:
          speak("the first and second number please")
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          print(num1, "x", num2, "=", multiply(num1, num2))
          x = multiply(num1, num2)
          speak("the answer is")
          speak(x)
    elif "divide" in voice_data:
          speak("the first and second number please")
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          print(num1, "÷", num2, "=", divide(num1, num2))
          x = divide(num1, num2)
          speak("the answer is")
          speak(x)
    elif "shut down computer" in voice_data:
        res = input("are you sure, everything will be lost if not saved:")
        if res == "no":
            exit()
        else:
            os.system("shutdown /s /t 1")
    elif "Spanish project" in voice_data:
        speak("running spanish project for you sir, changing language and speed...")
        sp_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
        engine.setProperty('voice', sp_voice_id)
        engine.setProperty("rate", 120)
        speak("Me gusta el pan tostado. Me encanta como el pan todos los días. No me gusta las salchichas. Yo como la pizza con mi familia Yo bebo la leche todos los días. A veces bebo los refrescos en la cena. Yo comparto las galletas con mi familia. Yo bebo el jugo de mananza con el almuerzo Nunca bebo refrescos en el desayuno, pero son buenos. Siempre como pan tostado. isha es un bebé grande y gordo, gracias")
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        engine.setProperty('voice', en_voice_id)
    elif "take photo" in voice_data:
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv2.imshow("Camera", image)
  
            cv2.imwrite("Untitled.png", image)
            if "Camera" == None:
                cv2.waitKey(0)
                cv2.destroyWindow("Camera")
            else:
                if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
                    speak("user closed window")
        
        else:
            speak("No image detected. Please! try again")

    elif "graph slope" in voice_data:
        x = np.linspace(-5,5,100)
        y = 2*x+1
        plt.plot(x, y, '-r', label='y=2x+1')
        plt.title('Graph of y=2x+1')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()
    elif "oci status" in voice_data:
        speak("checking OCI status now")
        webbrowser.open_new_tab("https://ociservices.gov.in/statusEnqury")
    elif "work time" in voice_data:
        
        random_iron=random.randint(1,4)
        if random_iron == 1:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=UkSr9Lw5Gm8&t")
        elif random_iron ==2:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=bcyvZIoQp9A&t")
        elif random_iron==3:
            webbrowser.open_new_tab("https://youtu.be/UkSr9Lw5Gm8")
        elif random_iron==4:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=WNlFFKNKkvw")
    elif "convert money" in voice_data:
        speak("how much money would you like to convert")
        value = int(input("type $"))
        rvem = requests.get(f"https://www.x-rates.com/table/?from=USD&amount={value}") 

        soup = BeautifulSoup(rvem.content, 'html.parser') 
        ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")

        for tableVal in ratelist:
            trList = tableVal.findAll('tr')
            for trVal in trList[:6]:
                print(trVal.text)
    elif "play angry birds theme" in voice_data:
        speak("playing angry birds theme now")
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=DehK_Y0TUbE")
    elif "read dataframe" in voice_data:
        data = pd.read_csv(r"C:/Users/Nickh/downloads/Python scripts/CLI-data-1-_1_.csv")
        data.head()
    elif "repeat after me" in voice_data:
        vid = voice_data.replace("repeat", '')
        vid2 = vid.replace("after", '')
        yid3 = vid2.replace("me", '')    
        speak(yid3)
    elif "heads or tails" in voice_data:
        
        random33=random.randint(1,2)
        print(random33)
        if random33==2:
            speak("heads")
        else:
            speak("tails")
    elif "open Discord" in voice_data:
        speak("opening discord")
        webbrowser.open_new_tab("https://discord.com/channels/@me")
    elif "stop" in voice_data:
        quit()
    elif "^" in voice_data:
        vv= voice_data.replace("what's", '')
        vvv=vv.replace("^",'')
        vvvv=vvv[1]
        yy=int(vvvv)
        vvv2=vvv[4]
        yyy=int(vvv2)
        xx=pow(yy,yyy)
        speak(xx)
    elif "close" in voice_data:
        dfh = voice_data.replace("close", '')
        xz=dfh+".exe"
        xzz=xz.lower()
        xzzz=xzz.strip()
        jhh=["taskkill","/F","/IM",xzzz]
        subprocess.call(jhh)
    elif "audio" in voice_data:
        speak("recording in 3 seconds")
        speak("how long should I record in seconds")
        cv=takevoice()
        re.sub('\D', '',cv)
        fs = 44100 
        seconds = int(cv)

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write('output.mp3', fs, myrecording)
    elif "generate picture" in voice_data:
        openai.api_key = "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"
        speak("what would you like to generate")
        gener=takevoice()
        response = openai.Image.create(
            prompt=gener,
            n=1,
            size="1024x1024"
           )
        image_url = response['data'][0]['url']
        url = image_url
        file_name = "generated_image.png"

        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print('Image sucessfully Downloaded: ',file_name)
                
        else:
            speak('Image Couldn\'t be retrieved')
    elif "rock paper scissors" in voice_data:
        import rock_jarvis
    elif "open system" in voice_data:
        tkWindow.mainloop()
    elif "note" in voice_data or "write down" in voice_data:
        s = voice_data.replace("note ", '')
        s = s.replace("write down ", '')
        import time
        import tempfile
        fi, filename = tempfile.mkstemp(prefix='note_', suffix='.txt', dir=r'C:\Users\Nickh\Downloads\JARVIS\vs\notes')
        print(filename)
        x=filename

    
        os.startfile(x)

        time.sleep(1)
        pyautogui.write(s)
    elif "open Schoology" in voice_data:
        user_id = "NSE7993"
        password = "Nine87gold#sai@"
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://accounts.coppellisd.com/')
        user_box = browser.find_element_by_id("input placeholder-input ember-view ember-text-field")
        user_box.send_keys(user_id)
        password_box = browser.find_element_by_id("ember479")
        password_box.send_keys(password)
        login_box = browser.find_element_by_name("authn-go-button")      
        login_box.click()
    elif "I have a question" in voice_data:
        speak("what is your question")
        question=takevoice()
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
    elif "scan the room" in voice_data:

        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break

            elif k%256 == 32:
                # SPACE pressed
                img_name = r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\image.jpg"
                cv2.imwrite(img_name, frame)
                print("{} written!".format("image"))
                img_counter += 1
                break
        
        cam.release()

        cv2.destroyAllWindows()
        exec(open(r"C:\Users\Nickh\Downloads\JARVIS\vs\obrec\objdet.py").read())
    else:
        pass



    


        
        
        
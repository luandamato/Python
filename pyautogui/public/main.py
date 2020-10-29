import pyautogui, time, webbrowser

def mexerMouse():
    time.sleep(1)
    pyautogui.move(-200, 350)

def selecionar_duas_linhas():
    # pyautogui.moveTo(420, 175)
    # pyautogui.click()
    pyautogui.keyDown('Shift') # Press the Shift key down and hold it.
    pyautogui.press(['down', 'down'])
    pyautogui.keyUp('shift')

def copia_cola():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press(['enter'])
    pyautogui.hotkey('ctrl', 'v')

def posicaoMouse():
    print(pyautogui.size())
    print(pyautogui.position())

def abre_escreve_arquino_na_tela():
    time.sleep(3)
    f = open("palavras", "r")
    for x in f:
        pyautogui.typewrite(x)
        pyautogui.press("enter")

def desenhaQuadrado():
    time.sleep(3)
    distance = 200
    while distance > 00:
            pyautogui.drag(distance, 0, 0.01)   # move right
            distance -= 5
            pyautogui.drag(0, distance, 0.01)   # move down
            pyautogui.drag(-distance, 0, 0.001)  # move left
            distance -= 5
            pyautogui.drag(0, -distance, 0.01)  # move up

def seuqencia_janelas_prompt():
    if (pyautogui.confirm('Shall I proceed?').lower() == "ok"):
        pyautogui.alert('ACEITOU')
    else:
        pyautogui.alert('recusou')

    print(pyautogui.confirm('Enter option.', "Nome", ['A', 'B', 'C']))
    print(pyautogui.prompt('What is your name?'))
    print(pyautogui.password('Enter password (text will be hidden)'))


#abrir e escrever em pag web
def votacao_automatica():
    webbrowser.open(pyautogui.prompt('Qual site vamos?'))
    time.sleep(6)
    if (pyautogui.confirm('Shall I proceed?').lower() != "ok"):
        return
    pyautogui.alert('Deixe o mouse no campo de comentarios')
    time.sleep(5)
    currentMouseX, currentMouseY = pyautogui.position()
    f = open("palavras", "r")
    for x in f:
        pyautogui.moveTo(currentMouseX, currentMouseY)
        pyautogui.click()
        pyautogui.typewrite(x)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)
        # buttonlocation = pyautogui.locateOnScreen('publicar_insta.PNG')
        # if buttonlocation != None:
        #     buttonx, buttony = pyautogui.center(buttonlocation)
        #     pyautogui.moveTo(buttonx - 200, buttony)
        #     pyautogui.click()
        #     print(x)
        #     time.sleep(1)
        #     pyautogui.typewrite(x)
        #     pyautogui.typewrite('enter')
        # else:
        #     pyautogui.alert('Campo comentario nao encontrado')



#ACHAR IMAGEM NA TELA
def localizarImg(nomeImagem): #nomeImagem = 'publicar_insta.PNG'
    time.sleep(2)
    buttonlocation = pyautogui.locateOnScreen(nomeImagem)
    if buttonlocation != None:
        print("main: ")
        print(buttonlocation)
        buttonx, buttony = pyautogui.center(buttonlocation)
        print(buttonx, buttony)
        pyautogui.moveTo(buttonx-200, buttony)
        pyautogui.click()
    else:
        print("nd")

votacao_automatica()



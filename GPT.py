import re
import g4f

messages = [{"role": "system",
             "content": "You are the AI Jarvis AI "},
            {"role": "system", "content": "you coded by Asif. you were not created by open ai"},

            ]


def MSG_DEL_AUTO():
    x = len(messages)
    if x > 14:
        new_ms = messages[0:2] + messages[-11:]
        return new_ms
    else:
        return messages


def find(txt):
    pattern = r"python(.*?)"
    matches = re.findall(pattern, txt, re.DOTALL)

    if matches:
        python_code = matches[0].strip()
        # install_missing_modules(python_code)
        return python_code
    else:
        return "'No Python code found.'"


def GPT(message):
    global messages
    try:
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k",
            provider=g4f.Provider.GPTalk,
            messages=messages,
            stream=True
        )
        ms = ""
        print()
        for message in response:
            ms += message
            print(message,end="",flush=True)
        print()
        print()
        messages.append({"role": "assistant", "content": ms})
        return ms
    except:
        print("some error occurred")
        return "sorry sir some error occurred!!. connecting again with server"
while 1:GPT(input(">>> "))
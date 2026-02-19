import ollama
messages = []
while True:
  user_input = input("You:")
  if user_input == "exit":
    break
  messages.append({"role":"user", "content":"user input"})
  response = ollama.chat(
  model = "gemma3:1b",
  messages = messages )
  reply = response['message']['content']
  print("Bot:",reply)
  messages.append({"role":"user","content":reply})
  
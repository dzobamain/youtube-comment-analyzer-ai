def save_chat_file(current_speaker, message, file_path):
    with open(file_path, "a", encoding="utf-8") as chat_file:
        chat_file.write(f"{current_speaker}: {message}\n")
        
def clear_chat_file(file_path):
    with open(file_path, "w", encoding="utf-8") as chat_file:
        chat_file.write("")

def read_chat_file(file_path):
    with open(file_path, "r", encoding="utf-8") as chat_file:
        return chat_file.read()
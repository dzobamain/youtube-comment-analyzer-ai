def save_chat_to_file(message, file_path, current_speaker=""):
    with open(file_path, "a", encoding="utf-8") as chat_file:
        chat_file.write(f"{current_speaker}{message}\n")
        
def clear_file(file_path):
    with open(file_path, "w", encoding="utf-8") as chat_file:
        chat_file.write("")

def read_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as chat_file:
        return chat_file.read()
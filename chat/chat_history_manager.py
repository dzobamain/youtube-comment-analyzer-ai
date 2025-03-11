from chat.file import read_from_file
from config import max_sumbol_for_chat_history

def find_message_end(file_path):
    lines = read_from_file(file_path)

    for i in range(len(lines) - 2):
        current_line = lines[i].strip()
        next_line = lines[i + 1].strip()
        
        if current_line == "" and next_line == "":
            for j in range(i + 2, len(lines)):
                if lines[j].strip() != "":
                    return j

            return None
    return None

def clear_message(file_path, last_empty_index):
    lines = read_from_file(file_path)

    if last_empty_index is not None:
        lines = lines[last_empty_index:]

        with open(file_path, "w", encoding="utf-8") as chat_file:
            chat_file.writelines(lines)


def chat_history_manager(text_length, file_path, number_of_symbols=max_sumbol_for_chat_history):
    if text_length > number_of_symbols:
        index = find_message_end(file_path)
        
        if index is not None:
            clear_message(file_path, index)

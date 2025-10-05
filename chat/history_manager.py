# chat/history_manager.py

from chat.file import read_from_file
from appconfig import config


def find_message_end(file_path):
    """
    Finds the index of the start of the next message in the chat history file.
    It looks for two consecutive empty lines (separator between messages).
    Returns the index of the first non-empty line after the separator.
    """
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
    """
    Clears the oldest part of the chat history up to the given index.
    Effectively trims the file, keeping only the newer part of the history.
    """
    lines = read_from_file(file_path)

    if last_empty_index is not None:
        # Keep only the part of the chat starting from last_empty_index
        lines = lines[last_empty_index:]

        with open(file_path, "w", encoding="utf-8") as chat_file:
            chat_file.writelines(lines)


def chat_history_manager(text_length, file_path, number_of_symbols=config.max_symbol_for_chat_history):
    """
    Manages chat history file:
    - If the text length exceeds the max allowed characters,
      it finds the next message index and clears the old history.
    """
    if text_length > number_of_symbols:
        index = find_message_end(file_path)
        
        if index is not None:
            clear_message(file_path, index)

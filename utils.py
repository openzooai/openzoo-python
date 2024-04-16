def chat_completion_to_dict(chat_completion):
    """
    Converts a ChatCompletion object and its nested structures to a dictionary.

    :param chat_completion: The ChatCompletion object to convert.
    :return: A dictionary representation of the chat completion.
    """
    completion_dict = {
        "id": getattr(chat_completion, "id", None),
        "created": getattr(chat_completion, "created", None),
        "model": getattr(chat_completion, "model", None),
        "object": getattr(chat_completion, "object", None),
        "system_fingerprint": getattr(chat_completion, "system_fingerprint", None),
        "usage": {
            "completion_tokens": getattr(chat_completion.usage, "completion_tokens", None),
            "prompt_tokens": getattr(chat_completion.usage, "prompt_tokens", None),
            "total_tokens": getattr(chat_completion.usage, "total_tokens", None),
        } if hasattr(chat_completion, "usage") else None,
        "prompt": getattr(chat_completion, "prompt", []),
        "choices": []
    }

    if hasattr(chat_completion, "choices"):
        for choice in chat_completion.choices:
            choice_dict = {
                "finish_reason": getattr(choice, "finish_reason", None),
                "index": getattr(choice, "index", None),
                "logprobs": getattr(choice, "logprobs", None),
                "message": {
                    "content": getattr(choice.message, "content", None),
                    "role": getattr(choice.message, "role", None),
                    "function_call": getattr(choice.message, "function_call", None),
                    "tool_calls": getattr(choice.message, "tool_calls", None),
                } if hasattr(choice, "message") else None
            }
            completion_dict["choices"].append(choice_dict)

    return completion_dict


def chat_completion_chunk_to_dict(chat_completion_chunk):
    """
    Converts a ChatCompletionChunk object and its nested structures to a dictionary.

    :param chat_completion_chunk: The ChatCompletionChunk object to convert.
    :return: A dictionary representation of the ChatCompletionChunk.
    """
    completion_chunk_dict = {
        "id": getattr(chat_completion_chunk, "id", None),
        "created": getattr(chat_completion_chunk, "created", None),
        "model": getattr(chat_completion_chunk, "model", None),
        "object": getattr(chat_completion_chunk, "object", None),
        "system_fingerprint": getattr(chat_completion_chunk, "system_fingerprint", None),
        "usage": getattr(chat_completion_chunk, "usage", None),  # Directly use the 'usage' if it's already a dict
        "choices": []
    }

    if hasattr(chat_completion_chunk, "choices"):
        for choice in chat_completion_chunk.choices:
            choice_dict = {
                "delta": getattr(choice, "delta", None),
                "finish_reason": getattr(choice, "finish_reason", None),
                "index": getattr(choice, "index", None),
                "logprobs": getattr(choice, "logprobs", None),
                "token_id": getattr(choice, "token_id", None),
                "text": getattr(choice, "text", None)
            }
            completion_chunk_dict["choices"].append(choice_dict)

    return completion_chunk_dict

# Example usage:
# Assuming 'chat_completion_chunk' is your ChatCompletionChunk object:
# chat_completion_chunk_dict = chat_completion_chunk_to_dict(chat_completion_chunk)
# print(chat_completion_chunk_dict)




from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("\n\n\n\n=========== Sending Messages ============\n\n")

        for m in messages[0]:
            if m.type == "system":
                boxen_print(m.content, title=m.type, color="yellow")

            elif m.type == "ai" and "function_call" in m.additional_kwargs:
                call = m.additional_kwargs["function_call"]
                text = f"Running tool {call['name']} with args {call['arguments']}"
                boxen_print(text, title=m.type, color="cyan")

            elif m.type == "ai":
                boxen_print(m.content, title=m.type, color="blue")

            elif m.type == "human":
                boxen_print(m.content, title=m.type, color="green")

            elif m.type == "function":
                boxen_print(m.content, title=m.type, color="purple")

            else:
                boxen_print(m.content, title=m.type)

# chatbot.py
import requests
from typing import List, Dict
import config


class SimpleBot:
    def __init__(self):
        self.token = config.OPENROUTER_TOKEN
        self.messages: List[Dict] = []
        self._init_system()

    def _init_system(self):
        self.messages.append({
            "role": "system",
            "content": config.SYSTEM_TEXT
        })

    def add_user_text(self, text: str):
        self.messages.append({
            "role": "user",
            "content": text
        })
        self.trim_memory()

    def add_bot_text(self, text: str):
        self.messages.append({
            "role": "assistant",
            "content": text
        })
        self.trim_memory()

    def build_payload_messages(self):
        return [{"role": m["role"], "content": m["content"]} for m in self.messages]

    def trim_memory(self):
        if not self.messages:
            return
        system_msg = self.messages[0]
        rest = self.messages[1:]
        if len(rest) > config.MAX_TURNS:
            rest = rest[-config.MAX_TURNS:]
        self.messages = [system_msg] + rest

    def fetch_reply(self) -> str:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        payload = {
        "model": config.MODEL_ID,
        "messages": self.build_payload_messages(),
        "temperature": config.TEMP,
        "max_tokens": config.MAX_REPLY_TOKENS,
    }

    try:
        resp = requests.post(
            config.CHAT_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=30,
        )

        if resp.status_code != 200:
            return f"HTTP {resp.status_code} - {resp.text}"

        data = resp.json()
        text = data["choices"][0]["message"]["content"]

        self.add_bot_text(text)
        return text

    except requests.exceptions.Timeout:
        return "Error: timeout"
    except requests.exceptions.ConnectionError:
        return "Error: connection"
    except Exception as ex:
        return f"Error: {str(ex)}"
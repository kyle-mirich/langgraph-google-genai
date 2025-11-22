"""Utility & helper functions."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage


def get_message_text(msg: BaseMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def load_chat_model(fully_specified_name: str) -> BaseChatModel:
    """Load a chat model from a fully specified name.

    Args:
        fully_specified_name (str): String in the format 'provider/model'.
    """
    provider, model = fully_specified_name.split("/", maxsplit=1)
    # LangChain expects underscores in provider names (e.g., google_genai).
    normalized_provider = provider.replace("-", "_")
    return init_chat_model(model, model_provider=normalized_provider)


def load_google_genai_model(model_name: str) -> BaseChatModel:
    """Load a Google GenAI chat model.

    Args:
        model_name (str): The name of the Google GenAI model to load.
    """
    return init_chat_model(model_name, model_provider="google_genai")

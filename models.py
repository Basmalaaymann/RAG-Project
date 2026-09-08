from typing import List , Any , Dict , List , Optional , Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    chat_history: Annotated[List , add_messages]
    query: str
    context: Optional[List[str]]
    rewritten_query: str
    response: str
    
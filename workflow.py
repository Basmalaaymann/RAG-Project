from models import State
from agents import *
from langgraph.graph import StateGraph , START , END


class workflow:
    def __init__(self):
        self.rewrite_query = rewritten_query
        self.retrieve_agent = retriever_agent
        self.response_agent = response_agent
    
    def build_graph(self):
        graph= StateGraph(State)
        graph.add_node("rewritten_query_agent" , self.rewritten_query)
        graph.add_node("retriever_agent" , self.retriever_agent)
        graph.add_node("response_agent" , self.response_agent)
        
        
        graph.add_edge(START ,"rewritten_query_agent")
        graph.add_edge("rewritten_query_agent" , "retriever_agent")
        graph.add_edge("retriever_agent" ,"response_agent")
        graph.add_agent("response_agent" , END)
        
        return graph.compile()
    
    def run(self , initial_state : State):
        graph =self.build_graph()
        result = graph.invoke(initial_state)
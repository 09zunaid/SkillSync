import networkx as nx

def create_career_dag():
    G = nx.DiGraph()
    
    # Core Fundamentals
    G.add_edge("Mathematics", "Statistics")
    G.add_edge("Mathematics", "Calculus")
    G.add_edge("Mathematics", "Linear Algebra")
    G.add_edge("Computer Science Basics", "Programming")
    G.add_edge("Computer Science Basics", "Data Structures")
    G.add_edge("Computer Science Basics", "Algorithms")
    
    # Programming
    G.add_edge("Programming", "Python")
    G.add_edge("Programming", "R")
    G.add_edge("Python", "Data Analysis with Python")
    
    # Data Science Path
    G.add_edge("Statistics", "Data Analysis")
    G.add_edge("Data Analysis with Python", "Data Analysis")
    G.add_edge("Data Analysis", "Machine Learning")
    G.add_edge("Calculus", "Machine Learning")
    G.add_edge("Linear Algebra", "Machine Learning")
    G.add_edge("Data Structures", "Machine Learning Engineering")
    G.add_edge("Algorithms", "Machine Learning Engineering")
    G.add_edge("Machine Learning", "Machine Learning Engineering")
    
    # Specialized ML
    G.add_edge("Machine Learning", "Deep Learning")
    G.add_edge("Machine Learning", "NLP")
    G.add_edge("Machine Learning", "Computer Vision")
    
    # Advanced / Production
    G.add_edge("Machine Learning Engineering", "MLOps")
    G.add_edge("Deep Learning", "Generative AI")
    G.add_edge("NLP", "LLMs")
    
    return G

def get_ancestors(graph, node):
    if node in graph:
        return list(nx.ancestors(graph, node))
    return []

def get_descendants(graph, node):
    if node in graph:
        return list(nx.descendants(graph, node))
    return []

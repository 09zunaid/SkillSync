import sys
import os

# Ensure we can import from local files
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from skills_trie import SkillsTrie, get_common_skills
from matcher import ResumeMatcher
from career_graph import create_career_dag, get_ancestors, get_descendants

def main():
    print("=== SkillSync Demo ===\n")

    # 1. Skills Trie
    print("--- 1. Standardized_Skills Trie ---")
    trie = SkillsTrie()
    skills = get_common_skills()
    print(f"Populating Trie with {len(skills)} skills...")
    for skill in skills:
        trie.insert(skill)
    
    search_term = "React"
    found = trie.search(search_term)
    print(f"Search for '{search_term}': {'Found' if found else 'Not Found'}")

    prefix = "Data"
    completions = trie.start_with_prefix(prefix)
    print(f"Skills starting with '{prefix}': {completions[:5]} ... (total {len(completions)})")
    print()

    # 2. Resume Matcher
    print("--- 2. Resume-Job Description Matching ---")
    try:
        matcher = ResumeMatcher()
        resume = "I am a Data Scientist with experience in Python, Machine Learning, and Statistics. I know TensorFlow."
        job_desc = "Looking for a Data Scientist skilled in Python, ML, and Deep Learning frameworks like TensorFlow or PyTorch."
        
        score = matcher.calculate_similarity(resume, job_desc)
        print(f"Resume: {resume}")
        print(f"Job Desc: {job_desc}")
        print(f"Similarity Score: {score:.4f}")
    except Exception as e:
        print(f"Error in matching: {e}")
        print("Make sure sentence-transformers is installed.")
    except ImportError:
         print("Error: sentence_transformers not installed.")

    print()

    # 3. Career Path DAG
    print("--- 3. Career Path DAG ---")
    try:
        dag = create_career_dag()
        target_node = "Machine Learning"
        parents = get_ancestors(dag, target_node)
        print(f"Ancestors (Prerequisites) of '{target_node}': {parents}")
        
        children = get_descendants(dag, target_node)
        print(f"Descendants (Future Paths) of '{target_node}': {children}")
    except Exception as e:
        print(f"Error in DAG: {e}")
        print("Make sure networkx is installed.")
    except ImportError:
        print("Error: networkx not installed.")
    print()

if __name__ == "__main__":
    main()

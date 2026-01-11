class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SkillsTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def start_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)

    def _find_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words_from_node(child_node, prefix + char))
        return words

def get_common_skills():
    # Base list of skills
    base_skills = [
        "Python", "Java", "C++", "C#", "JavaScript", "TypeScript", "React", "Angular", "Vue",
        "Node.js", "Django", "Flask", "FastAPI", "Spring Boot", "Ruby on Rails",
        "HTML", "CSS", "Sass", "Less", "Tailwind CSS", "Bootstrap",
        "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Cassandra", "Elasticsearch",
        "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Terraform", "Ansible",
        "Git", "GitHub", "GitLab", "CI/CD", "Jenkins", "CircleCI",
        "Machine Learning", "Deep Learning", "Data Science", "Artificial Intelligence",
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy", "Matplotlib",
        "NLP", "Computer Vision", "Reinforcement Learning", "OpenCV",
        "Android", "iOS", "Swift", "Kotlin", "React Native", "Flutter",
        "Linux", "Unix", "Bash", "Shell Scripting",
        "Cybersecurity", "Network Security", "Ethical Hacking",
        "Blockchain", "Smart Contracts", "Solidity", "Ethereum",
        "Agile", "Scrum", "Kanban", "Jira", "Confluence",
        "REST API", "GraphQL", "gRPC", "Microservices",
        "OOD", "Design Patterns", "Algorithms", "Data Structures"
    ]
    
    # Generate variations to reach ~1000 items for demonstration
    expanded_skills = []
    modifiers = ["Advanced", "Basic", "Intermediate", "Certified"]
    versions = ["v1", "v2", "v3", "2023", "2024", "Legacy"]
    
    for skill in base_skills:
        expanded_skills.append(skill)
        for mod in modifiers:
            expanded_skills.append(f"{mod} {skill}")
        for ver in versions:
            expanded_skills.append(f"{skill} {ver}")
            
    # Add some specific library combinations
    for i in range(100):
        expanded_skills.append(f"Custom Skill {i}")

    return sorted(list(set(expanded_skills)))[:1000]

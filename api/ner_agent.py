import spacy
from skills_trie import SkillsTrie

class NERAgent:
    def __init__(self, skills_trie: SkillsTrie):
        self.nlp = spacy.load("en_core_web_sm")
        self.skills_trie = skills_trie

    def extract_skills(self, text: str):
        # 1. Spacy NER for potential entities (ORG, PRODUCT, GPE, etc might catch some)
        # But for tech skills, direct Trie lookup or Pattern matching is often better than generic NER.
        # We will use a hybrid approach: Tokenize with Spacy, then check n-grams against Trie.
        
        doc = self.nlp(text)
        found_skills = set()

        # Check individual tokens and bi-grams/tri-grams against Trie
        # This is a simplified "NER" specific for our known skills.
        
        # Method: Iterate through tokens, check if they exist in Trie.
        # This is naive but effective if Trie is comprehensive.
        
        text_lower = text.lower() # Case insensitive match for safety, though Trie might be case sensitive.
        # Let's assume our Trie has standard casing. We should probably normalize text to match Trie.
        # For this demo, let's scan the text for known skills.
        
        # Better approach: Aho-Corasick or just iterating our skill list? 
        # Since we have a Trie, let's use it to scan the text.
        
        # Sliding window or logic to match "Machine Learning" vs "Machine".
        # We'll simple scan for Trie words.
        
        # Simplified: Check if any known skill is present in the text.
        # For 1000 skills, this is fast.
        
        # Get all skills from Trie (we don't have a get_all method exposed easily, but we have the loading list)
        # Let's rely on the Trie search.
        
        # Actually, let's use Spacy Noun Chunks to identify candidates.
        chunks = [chunk.text for chunk in doc.noun_chunks]
        
        # Also check simple tokens
        tokens = [token.text for token in doc]
        
        candidates = set(chunks + tokens)
        
        for candidate in candidates:
            # Clean candidate
            clean_cand = candidate.strip().replace("\n", " ")
            # We need to match case-insensitively potentially, or exactly.
            # Our Trie is exact.
            
            # Heuristic: Title case it or keep as is.
            if self.skills_trie.search(clean_cand):
                found_skills.add(clean_cand)
                
            # Try Title Case
            if self.skills_trie.search(clean_cand.title()):
                found_skills.add(clean_cand.title())
                
        return list(found_skills)


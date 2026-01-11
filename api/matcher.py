from sentence_transformers import SentenceTransformer, util

class ResumeMatcher:
    def __init__(self):
        # Using a small, fast model
        self.model = SentenceTransformer('all-MiniLM-L6-v2') 
        
    def calculate_similarity(self, resume_text, job_description):
        embeddings = self.model.encode([resume_text, job_description], convert_to_tensor=True)
        cosine_score = util.cos_sim(embeddings[0], embeddings[1])
        return cosine_score.item()

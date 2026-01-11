from typing import List, Dict, Any
from pdf_processor import PDFProcessor
from ner_agent import NERAgent
from skills_trie import SkillsTrie, get_common_skills
from career_graph import create_career_dag, get_ancestors
from project_recommender import ProjectRecommender

class ProcessingPipeline:
    def __init__(self):
        # Initialize components
        self.trie = SkillsTrie()
        skills = get_common_skills()
        for skill in skills:
            self.trie.insert(skill)
            
        self.ner_agent = NERAgent(self.trie)
        self.dag = create_career_dag()
        self.pdf_processor = PDFProcessor()
        self.project_recommender = ProjectRecommender()

    def process_application(self, pdf_bytes: bytes, job_description_text: str) -> Dict[str, Any]:
        # 1. Extract Text from Resume
        resume_text = self.pdf_processor.extract_text(pdf_bytes)
        
        # 2. Extract Skills from Resume
        extracted_skills = self.ner_agent.extract_skills(resume_text)
        
        # 3. Extract Skills from Job Description
        target_skills = self.ner_agent.extract_skills(job_description_text)
        
        # 4. Gap Analysis
        candidate_skill_set = set(extracted_skills)
        target_skill_set = set(target_skills)
        
        matched_skills = list(candidate_skill_set.intersection(target_skill_set))
        missing_skills = list(target_skill_set - candidate_skill_set)
        
        # Calculate Match Score
        if not target_skill_set:
            match_score = 0.0
        else:
            match_score = len(matched_skills) / len(target_skill_set)
            
        # 5. Career Path Suggestions (DAG)
        suggested_path = []
        for missing in missing_skills:
            prereqs = get_ancestors(self.dag, missing)
            if prereqs:
                suggested_path.append({
                    "skill": missing,
                    "prerequisites": prereqs
                })
                
        # 6. Project Recommendations
        project_recommendations = self.project_recommender.get_recommendations(missing_skills)
        
        return {
            "match_score": round(match_score * 100, 2),
            "extracted_skills": extracted_skills,
            "target_skills": target_skills, # Return what we found in JD
            "missing_skills": missing_skills,
            "suggested_learning_path": suggested_path,
            "project_recommendations": project_recommendations
        }

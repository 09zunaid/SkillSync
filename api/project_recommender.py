from typing import List, Dict

class ProjectRecommender:
    def __init__(self):
        # Dictionary mapping skills to specific project ideas
        self.project_ideas = {
            "Python": "Build a web scraper or automation script.",
            "React": "Create a personal portfolio with interactive components.",
            "Machine Learning": "Predict housing prices using a regression model.",
            "Deep Learning": "Build a cat vs dog image classifier using CNNs.",
            "SQL": "Design a database schema for an e-commerce store and write complex queries.",
            "Statistics": "Perform A/B testing analysis on a sample dataset.",
            "NLP": "Create a sentiment analysis tool for movie reviews.",
            "MLOps": "Deploy a machine learning model using Docker and FastAPI.",
            "Docker": "Containerize a simple Flask application.",
            "FastAPI": "Build a REST API for a To-Do list application.",
            "TensorFlow": "Train a neural network on the MNIST dataset.",
            "PyTorch": "Implement a GAN to generate handwritten digits.",
            "Data Analysis": "Analyze the Titanic dataset and visualize survival rates.",
            "Pandas": "Clean and preprocess a large dirty dataset.",
            "AWS": "Host a static website on S3 with CloudFront.",
            "Azure": "Deploy a serverless function using Azure Functions.",
            "Google Cloud": "Train a model using Vertex AI.",
            "Kubernetes": "Orchestrate a microservices application on Minikube.",
            "Git": "Contribute to an open source project or simulate a team workflow.",
            "CI/CD": "Set up a GitHub Actions workflow to run tests automatically.",
            "Terraform": "Provision infrastructure as code for a simple VPC.",
            "Ansible": "Write a playbook to configure a web server."
        }
        
    def get_recommendations(self, missing_skills: List[str]) -> List[Dict[str, str]]:
        recommendations = []
        for skill in missing_skills:
            # Check for exact match or partial match
            project = self.project_ideas.get(skill)
            if not project:
                # Fallback for generic recommendations if skill not found
                # Or try to find a key that is contained in the skill string
                for key, idea in self.project_ideas.items():
                    if key in skill or skill in key:
                        project = idea
                        break
            
            if project:
                recommendations.append({
                    "skill": skill,
                    "project": project
                })
            else:
                 recommendations.append({
                    "skill": skill,
                    "project": f"Build a small proof-of-concept using {skill} to understand the basics."
                })
                
        return recommendations

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Pre-defined career mappings for instant demo
CAREER_DATA = {
    "python_sql": {
        "career_path": "Data Analyst / Data Scientist",
        "description": "Perfect for analyzing business data and creating insights",
        "next_steps": [
            "Learn pandas and numpy for data manipulation",
            "Master data visualization with matplotlib/seaborn",
            "Study statistics and machine learning basics",
            "Practice SQL queries on real datasets",
            "Build portfolio projects with real data"
        ],
        "salary_range": "$60,000 - $120,000",
        "job_growth": "High demand (22% growth expected)"
    },
    "csharp_erp": {
        "career_path": "Backend ERP Developer",
        "description": "Specialize in enterprise resource planning systems",
        "next_steps": [
            "Master ASP.NET Core and Web APIs",
            "Learn database design and optimization",
            "Understand ERP modules (Finance, HR, Supply Chain)",
            "Practice with ERPNext customization",
            "Get familiar with cloud deployment (Azure/AWS)"
        ],
        "salary_range": "$70,000 - $130,000",
        "job_growth": "Steady demand in enterprise sector"
    },
    "react_nodejs": {
        "career_path": "Full Stack Web Developer",
        "description": "Build complete web applications from front to back",
        "next_steps": [
            "Master React hooks and state management",
            "Learn Express.js and REST API development",
            "Practice with MongoDB or PostgreSQL",
            "Understand authentication and security",
            "Deploy projects to Heroku/Netlify"
        ],
        "salary_range": "$65,000 - $125,000",
        "job_growth": "Very high demand across all industries"
    },
    "html_css_js": {
        "career_path": "Frontend Web Developer",
        "description": "Create beautiful and interactive user interfaces",
        "next_steps": [
            "Master modern CSS (Grid, Flexbox, Animations)",
            "Learn a frontend framework (React/Vue/Angular)",
            "Practice responsive design principles",
            "Understand browser developer tools",
            "Build portfolio with diverse projects"
        ],
        "salary_range": "$50,000 - $100,000",
        "job_growth": "High demand for mobile-first designs"
    },
    "java_spring": {
        "career_path": "Enterprise Java Developer",
        "description": "Build robust enterprise applications",
        "next_steps": [
            "Master Spring Boot and Spring Security",
            "Learn microservices architecture",
            "Practice with Maven/Gradle build tools",
            "Understand unit testing with JUnit",
            "Study design patterns and clean code"
        ],
        "salary_range": "$75,000 - $140,000",
        "job_growth": "Consistent demand in large enterprises"
    },
    "mobile_dev": {
        "career_path": "Mobile App Developer",
        "description": "Create apps for iOS and Android platforms",
        "next_steps": [
            "Choose: React Native, Flutter, or native development",
            "Learn mobile UI/UX design principles",
            "Practice with app store deployment",
            "Understand mobile-specific APIs and features",
            "Build 2-3 complete apps for portfolio"
        ],
        "salary_range": "$70,000 - $130,000",
        "job_growth": "Growing with mobile-first world"
    }
}

def analyze_skills(skills_input):
    """Analyze user skills and return best matching career path"""
    skills_lower = skills_input.lower()
    
    # Simple skill matching logic
    if any(skill in skills_lower for skill in ['python', 'sql', 'data', 'pandas', 'numpy']):
        return "python_sql"
    elif any(skill in skills_lower for skill in ['c#', 'erp', 'erpnext', 'enterprise']):
        return "csharp_erp"
    elif any(skill in skills_lower for skill in ['react', 'node', 'javascript', 'express']):
        return "react_nodejs"
    elif any(skill in skills_lower for skill in ['html', 'css', 'frontend', 'ui']):
        return "html_css_js"
    elif any(skill in skills_lower for skill in ['java', 'spring', 'backend']):
        return "java_spring"
    elif any(skill in skills_lower for skill in ['mobile', 'android', 'ios', 'flutter', 'react native']):
        return "mobile_dev"
    else:
        # Default recommendation for unknown skills
        return "react_nodejs"

def generate_personalized_message(career_data, user_skills):
    """Generate a personalized message based on user skills"""
    encouraging_messages = [
        f"Great choice! Your skills in {user_skills} align perfectly with this career path.",
        f"Excellent foundation! {user_skills} skills are highly valued in this field.",
        f"You're on the right track! {user_skills} will give you a competitive edge.",
        f"Perfect match! Companies are actively looking for professionals with {user_skills} skills."
    ]
    
    return random.choice(encouraging_messages)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Career Advisor API is running!",
        "endpoints": [
            "POST /recommend - Get career recommendations",
            "GET /careers - List all available career paths"
        ]
    })

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    try:
        # Get user input
        data = request.get_json()
        
        if not data or 'skills' not in data:
            return jsonify({"error": "Please provide 'skills' in request body"}), 400
        
        user_skills = data['skills'].strip()
        
        if not user_skills:
            return jsonify({"error": "Skills cannot be empty"}), 400
        
        # Analyze skills and get career recommendation
        career_key = analyze_skills(user_skills)
        career_info = CAREER_DATA[career_key]
        
        # Generate personalized response
        response = {
            "user_skills": user_skills,
            "career_path": career_info["career_path"],
            "description": career_info["description"],
            "next_steps": career_info["next_steps"],
            "salary_range": career_info["salary_range"],
            "job_growth": career_info["job_growth"],
            "personalized_message": generate_personalized_message(career_info, user_skills),
            "confidence_score": "85%",  # Mock confidence score
            "status": "success"
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/careers', methods=['GET'])
def list_careers():
    """List all available career paths"""
    careers = []
    for key, value in CAREER_DATA.items():
        careers.append({
            "id": key,
            "career_path": value["career_path"],
            "description": value["description"]
        })
    
    return jsonify({"careers": careers})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Career Advisor API is running smoothly!"})

if __name__ == '__main__':
    print("🚀 Starting Career Advisor API...")
    print("📍 Backend running at: http://127.0.0.1:5000")
    print("🔄 Endpoints available:")
    print("   POST /recommend - Get career advice")
    print("   GET /careers - List career paths")
    print("   GET /health - Health check")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Hard-coded knowledge base for employee FAQ
KNOWLEDGE_BASE = {
    "password reset": "To reset your password, please contact IT Support at ext. 1234 or email support@company.com. You can also use the self-service password reset portal on the company intranet.",
    "w-2 forms": "W-2 forms are available in your employee portal starting January 31st. You can also request a physical copy from HR by calling +1 (866)-709-5932 or visiting the HR office on the 3rd floor.",
    "w2 forms": "W-2 forms are available in your employee portal starting January 31st. You can also request a physical copy from HR by calling +1 (866)-709-5932 or visiting the HR office on the 3rd floor.",
    "vacation policy": "Full-time employees accrue 2 weeks (80 hours) of vacation time per year. Part-time employees accrue vacation time proportionally. Vacation requests must be submitted at least 2 weeks in advance through the HR portal.",
    "sick leave": "Employees are entitled to 5 days of paid sick leave per year. Sick leave does not roll over to the next year. Please notify your supervisor as soon as possible if you need to use sick leave.",
    "health insurance": "The company offers comprehensive health insurance through Blue Cross Blue Shield. Open enrollment is in November. Contact HR for plan details and enrollment information.",
    "401k": "The company offers a 401(k) retirement plan with up to 3% company matching. You can enroll after 90 days of employment. Contact our benefits administrator for more information.",
    "payroll": "Payroll is processed bi-weekly on Fridays. Direct deposit information can be updated through the employee portal. Contact HR for any payroll-related questions.",
    "dress code": "The company maintains a business casual dress code. Please refer to the employee handbook for specific guidelines or contact HR with any questions.",
    "remote work": "Remote work requests must be approved by your supervisor and HR. Please submit requests using Form RW-101 available on the company intranet.",
    "parking": "Employee parking is available in the west parking garage. Parking passes can be obtained from security at the front desk. Monthly parking fee is $50.",
    "it support": "For technical issues, contact IT Support at ext. 1234, email support@company.com, or submit a ticket through the IT portal on the company intranet.",
    "hr contact": "HR is located on the 3rd floor, room 301. Phone: +1(866)-709-5932. Email: hr@company.com. Office hours: Monday-Friday, 8:00 AM - 5:00 PM."
}

# Enhanced keyword mapping for natural language queries
KEYWORD_SYNONYMS = {
    "password": ["password", "login", "signin", "sign-in", "credentials", "account", "authentication", "forgot", "reset"],
    "w-2": ["w-2", "w2", "tax", "taxes", "forms", "1099", "tax document", "tax form", "year end", "january"],
    "vacation": ["vacation", "time off", "pto", "paid time off", "leave", "holiday", "days off", "time away", "break"],
    "sick": ["sick", "illness", "medical", "sick leave", "sick day", "sick time", "medical leave", "unwell"],
    "health": ["health", "insurance", "medical", "benefits", "healthcare", "doctor", "hospital", "coverage", "plan"],
    "401k": ["401k", "401(k)", "retirement", "pension", "savings", "matching", "contributions", "benefits"],
    "payroll": ["payroll", "pay", "salary", "wages", "direct deposit", "paycheck", "payment", "compensation"],
    "dress": ["dress", "attire", "clothing", "uniform", "appearance", "business casual", "professional", "what to wear"],
    "remote": ["remote", "work from home", "wfh", "telecommute", "home office", "virtual", "telework"],
    "parking": ["parking", "garage", "car", "vehicle", "park", "lot", "pass", "permit"],
    "it": ["it", "technical", "computer", "laptop", "software", "hardware", "tech", "system", "network"],
    "hr": ["hr", "human resources", "personnel", "contact", "office", "department", "help"]
}

def search_knowledge_base(question):
    """
    Advanced search using keyword analysis and natural language processing.
    Returns single best match or multiple matches for multi-keyword queries.
    """
    question_lower = question.lower().strip()
    
    # Remove common stop words and question words
    stop_words = {'what', 'is', 'the', 'how', 'do', 'i', 'can', 'where', 'when', 'why', 'for', 'this', 'job', 'company', 'work', 'at', 'in', 'on', 'a', 'an', 'and', 'or', 'but', 'to', 'of', 'with', 'about', 'get', 'have', 'my', 'our', 'are', 'does', 'will'}
    question_words = [word for word in question_lower.split() if word not in stop_words]
    
    # Direct exact match first
    if question_lower in KNOWLEDGE_BASE:
        return {"single": KNOWLEDGE_BASE[question_lower]}
    
    # Advanced keyword matching with scoring system
    matches = []
    
    for kb_key, answer in KNOWLEDGE_BASE.items():
        score = 0
        kb_key_lower = kb_key.lower()
        
        # Direct substring match (highest priority)
        if kb_key_lower in question_lower or any(kb_word in question_lower for kb_word in kb_key_lower.split()):
            score += 100
        
        # Synonym-based matching
        for main_keyword, synonyms in KEYWORD_SYNONYMS.items():
            if main_keyword in kb_key_lower or any(kb_word in main_keyword for kb_word in kb_key_lower.split()):
                for synonym in synonyms:
                    if synonym in question_lower:
                        score += 50
                        # Bonus for exact word match
                        if synonym in question_words:
                            score += 25
        
        # Partial word matching
        kb_words = kb_key_lower.split()
        for kb_word in kb_words:
            for q_word in question_words:
                if kb_word == q_word:
                    score += 30
                elif kb_word in q_word or q_word in kb_word:
                    score += 15
        
        # Context-based scoring for specific patterns
        if "dress" in question_lower and "code" in question_lower and "dress" in kb_key_lower:
            score += 75
        if "sick" in question_lower and "leave" in question_lower and "sick" in kb_key_lower:
            score += 75
        if "w" in question_lower and "2" in question_lower and "w-2" in kb_key_lower:
            score += 75
        if "401" in question_lower and "k" in question_lower and "401k" in kb_key_lower:
            score += 75
        
        # Add to matches if score is above threshold
        if score >= 25:
            matches.append({
                'key': kb_key,
                'answer': answer,
                'score': score
            })
    
    # Sort matches by score (highest first)
    matches.sort(key=lambda x: x['score'], reverse=True)
    
    if not matches:
        return None
    
    # If top score is significantly higher, return single answer
    if len(matches) == 1 or (len(matches) > 1 and matches[0]['score'] - matches[1]['score'] > 50):
        return {"single": matches[0]['answer']}
    
    # If multiple good matches with similar scores, return multiple answers
    if len(matches) >= 2 and matches[1]['score'] >= 50:
        return {
            "multiple": [
                {"topic": matches[0]['key'].title(), "answer": matches[0]['answer']},
                {"topic": matches[1]['key'].title(), "answer": matches[1]['answer']}
            ]
        }
    
    # Default to single best match
    return {"single": matches[0]['answer']}

@app.route('/')
def home():
    """Homepage with search form"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handle search requests and return results"""
    question = request.form.get('question', '').strip()
    
    if not question:
        return render_template('results.html', 
                             question="", 
                             answer="Please enter a question to search our FAQ database.")
    
    # Search the knowledge base
    search_result = search_knowledge_base(question)
    
    if search_result:
        if "single" in search_result:
            # Single answer
            return render_template('results.html', 
                                 question=question, 
                                 answer=search_result["single"])
        elif "multiple" in search_result:
            # Multiple answers
            return render_template('results.html', 
                                 question=question, 
                                 multiple_answers=search_result["multiple"])
    else:
        # Default AI placeholder response
        placeholder_response = ("I'm not sure about that specific question. "
                              "Would you like me to create a ServiceNow ticket for you? "
                              "You can also try rephrasing your question or contact "
                              "HR at +1 (866)-709-5932 for additional assistance.")
        return render_template('results.html', 
                             question=question, 
                             answer=placeholder_response,
                             is_placeholder=True)

if __name__ == '__main__':
    # You can change the port to any number you like:
    # port=8080 -> http://localhost:8080
    # port=3000 -> http://localhost:3000  
    # port=9999 -> http://localhost:9999
    app.run(debug=True, host='127.0.0.1', port=8080)

from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from backend.agent import MarketResearchAgent

load_dotenv()

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Get API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

print(f"DEBUG: Loaded GROQ_API_KEY='{groq_api_key}'")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize the agent
research_agent = MarketResearchAgent(api_key=groq_api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research', methods=['POST'])
def research():
    competitor_name = request.form['competitor_name']
    if not competitor_name:
        return render_template('index.html', error="Please enter a competitor name.")

    # Perform research using the agent
    swot_analysis = research_agent.get_swot_analysis(competitor_name)
    pestle_analysis = research_agent.get_pestle_analysis(competitor_name)
    five_forces_analysis = research_agent.get_five_forces_analysis(competitor_name)
    gartner_report = research_agent.get_gartner_market_report(competitor_name)

    return render_template('index.html', 
                           competitor_name=competitor_name,
                           swot_analysis=swot_analysis,
                           pestle_analysis=pestle_analysis,
                           five_forces_analysis=five_forces_analysis,
                           gartner_report=gartner_report)

if __name__ == '__main__':
    app.run(debug=True)

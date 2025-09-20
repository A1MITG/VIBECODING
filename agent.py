import os
import requests
import json

class MarketResearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def _run_query(self, prompt):
        """Helper function to run a query using the Groq API with requests."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": [
                {
                    "role": "user",                  
                    "content": prompt,
                }
            ],
            "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            return response.json()['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def get_swot_analysis(self, company_name):
        """Performs SWOT analysis for a given company."""
        prompt = f"As a marketing and competitive research professional, perform a detailed SWOT analysis for {company_name}. Please provide the output in a structured format with clear headings for Strengths, Weaknesses, Opportunities, and Threats."
        return self._run_query(prompt)

    def get_pestle_analysis(self, company_name):
        """Performs PESTLE analysis for a given company."""
        prompt = f"As a marketing and competitive research professional, perform a detailed PESTLE analysis for {company_name}. Analyze the Political, Economic, Social, Technological, Legal, and Environmental factors affecting the company. Please provide the output in a structured format."
        return self._run_query(prompt)

    def get_five_forces_analysis(self, company_name):
        """Performs Porter's Five Forces analysis for a given company."""
        prompt = f"As a marketing and competitive research professional, perform a detailed Porter's Five Forces analysis for {company_name}. Analyze the competitive rivalry, threat of new entrants, bargaining power of buyers, bargaining power of suppliers, and threat of substitutes. Please provide the output in a structured format."
        return self._run_query(prompt)

    def get_gartner_market_report(self, company_name):
        """"Generates a Gartner-style market report for a given company."""
        prompt = (
            "You are a world-class industry analyst with expertise in market research, competitive intelligence, and strategic forecasting.\n\n"
            "Your goal is to simulate a Gartner-style report using public data, historical trends, and logical estimation.\n\n"
            "For each request:\n"
            "• Generate clear, structured insights based on known market signals.\n"
            "• Build data-backed forecasts using assumptions (state them).\n"
            "• Identify top vendors and categorize them by niche, scale, or innovation.\n"
            "• Highlight risks, emerging players, and future trends.\n\n"
            "Be analytical, not vague. Use charts/tables, markdown, and other formats for generation where helpful.\n\n"
            "Be explicit about what’s estimated vs known.\n\n"
            "Use this structure for output:\n\n"
            "1. Market Overview\n2. Key Players\n3. Forecast (1–3 years)\n4. Opportunities & Risks\n5. Strategic Insights\n\n"
            f"Company/Market: {company_name}\n"
        )
        return self._run_query(prompt)

    
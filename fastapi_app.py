import logging
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from FinResearcher.state import SummaryStateInput
from FinResearcher.graph import graph

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Create the FastAPI app
app = FastAPI()

class ResearchRequest(BaseModel):
    research_topic: str

@app.post("/run_research")
async def run_research_endpoint(request: ResearchRequest):
    """FastAPI endpoint to invoke the research function"""
    
    logging.info(f"Received research request: {request.research_topic}")

    try:
        # Process research request
        initial_state = SummaryStateInput(research_topic=request.research_topic)
        output = graph.invoke(initial_state)

        # Log the generated summary (first 200 characters for brevity)
        research_summary = output.get("running_summary", "")
        logging.info(f"Generated research summary: {research_summary[:200]}...")

        return {"summary": research_summary}

    except Exception as e:
        logging.error(f"Error processing research request: {str(e)}", exc_info=True)
        return {"error": "An internal error occurred while processing the request."}

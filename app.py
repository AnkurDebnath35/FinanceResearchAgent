import chainlit as cl
import os
import asyncio  # ✅ For smooth streaming
from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from FinResearcher.configuration import Configuration
from FinResearcher.state import SummaryStateInput
from FinResearcher.graph import graph  # Import the compiled LangGraph

# Load environment variables
load_dotenv()

# Function to run the research assistant
def run_research(research_topic: str):

    # Define input for the graph
    initial_state = SummaryStateInput(research_topic=research_topic)

    # Run the graph
    output = graph.invoke(initial_state)

    return output["running_summary"]

@cl.on_message
async def on_message(message: cl.Message):
    """Handles user input and streams structured AI response word by word with correct formatting."""
    user_query = message.content

    # ✅ Show "Generating response..." with an AI author name
    msg = cl.Message(content="🔍 Researching... Please wait...")
    await msg.send()

    # Get research summary
    research_summary = run_research(user_query).strip()

    # ✅ Remove repeated query if it appears at the start
    if research_summary.lower().startswith(user_query.lower()):
        research_summary = research_summary[len(user_query):].strip()

    # ✅ Remove "Summary" if present
    research_summary = research_summary.replace("## Summary", "").strip()

    # ✅ Split into "Key Insights" and "Sources"
    if "### Sources:" in research_summary:
        insights, sources = research_summary.split("### Sources:", 1)
    else:
        insights = research_summary
        sources = ""

    # ✅ Remove redundant intros like "Here are the updated key insights..."
    intro_phrases = [
        "Here are the updated key insights on",
        "Updated insights on",
        "Key insights on",
        "The latest insights on"
    ]
    for phrase in intro_phrases:
        if insights.startswith(phrase):
            insights = insights[len(phrase):].strip()

    # ✅ Remove extra bullet points (`•`)
    insights = insights.replace("•", "").strip()

    # ✅ Format "Key Insights" properly (smooth word streaming)
    msg.content = "## Key Insights\n\n"
    await msg.update()

    for line in insights.strip().split("\n"):
        if line.strip():  # Avoid empty lines
            words = line.strip().split()
            msg.content += "- "  # ✅ Ensure bullet points appear correctly
            for word in words:
                msg.content += word + " "
                await msg.update()
                await asyncio.sleep(0.1)  # ✅ Smooth streaming effect
            
            msg.content += "\n"  # ✅ Newline after each bullet point
            await msg.update()

    # ✅ Format "Sources" properly (Fix double bullets & make clickable)
    if sources.strip():
        msg.content += "\n\n---\n\n## Sources\n\n"
        await msg.update()

        for line in sources.strip().split("\n"):
            line = line.strip().lstrip("*").strip()  # ✅ Remove extra `*` from bullet points

            if line.startswith("http"):  
                msg.content += f"- [{line}]({line})\n"  # ✅ Format as a clickable link
            else:
                msg.content += f"- {line}\n"  # ✅ Keep non-URL text
            await msg.update()
            await asyncio.sleep(0.1)  # ✅ Smooth streaming

    await msg.update()

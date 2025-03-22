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
    """Handles user input and streams structured AI response word by word."""
    user_query = message.content

    # Send an initial loading message
    msg = cl.Message(content="🔍 Researching... Please wait...")
    await msg.send()

    # Get research summary
    research_summary = run_research(user_query)

    # ✅ Ensure we remove any "## Summary" from the response text
    research_summary = research_summary.replace("## Summary", "").strip()

    # ✅ Split response into "Summary" and "Sources" sections
    if "### Sources:" in research_summary:
        summary_text, sources_text = research_summary.split("### Sources:", 1)
    else:
        summary_text = research_summary
        sources_text = ""

    # ✅ Remove "Here is the updated summary:" if it exists
    summary_text = summary_text.replace("Here is the updated summary:", "").strip()

    # ✅ Add "Summary" as a proper Markdown heading
    msg.content = "# Summary\n\n"
    await msg.update()

    # ✅ Stream the "Summary" section word by word
    for word in summary_text.split():
        escaped_word = word.replace("*", "\\*").replace("#", "\\#").replace("-", "\\-")  # ✅ Escape Markdown
        msg.content += escaped_word + " "
        await msg.update()
        await asyncio.sleep(0.1)  # ✅ Small delay for natural typing effect

    # ✅ Stream the "Sources" section while maintaining bullet points
    if sources_text.strip():
        msg.content += "\n\n---\n\n## Sources\n\n"
        await msg.update()

        for line in sources_text.strip().split("\n"):
            if line.strip().startswith("*"):  # ✅ Keep bullet point alignment
                msg.content += f"- {line.strip()[1:].strip()}\n"  # Removes extra "*"
            else:
                msg.content += f"{line.strip()} "  # Keep normal text
            await msg.update()
            await asyncio.sleep(0.1)  # ✅ Keeps the same smooth effect for sources

    await msg.update()

from datetime import datetime

# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")

query_writer_instructions="""Your goal is to generate a targeted web search query.

<CONTEXT>
Current date: {current_date}
Please ensure your queries account for the most current information available as of this date.
</CONTEXT>

<TOPIC>
{research_topic}
</TOPIC>

<FORMAT>
Format your response as a JSON object with ALL three of these exact keys:
   - "query": The actual search query string
   - "rationale": Brief explanation of why this query is relevant
</FORMAT>

<EXAMPLE>
Example output:
{{
    "query": "machine learning transformer architecture explained",
    "rationale": "Understanding the fundamental structure of transformer models"
}}
</EXAMPLE>

Provide your response in JSON format:"""

summarizer_instructions="""
<GOAL>
Summarize the web search results into **Key Insights**, focusing on the most relevant and impactful information related to the user's topic.

<REQUIREMENTS>
When creating a NEW summary:
1. Extract the **most important takeaways** from the search results.
2. Present the findings as **bullet-pointed key insights** instead of paragraphs.
3. Keep each key insight **concise** (1-2 sentences max).
4. Ensure **no redundancy** and avoid generic statements.

When EXTENDING an existing summary:
1. **Read the existing insights and new search results carefully.**
2. **Compare the new information with existing insights.**
3. **For each new piece of information:**
   a. If it **adds depth** to an existing insight, **update** that point.  
   b. If it is **entirely new but relevant**, **add a new bullet point**.  
   c. If it is **not relevant**, **ignore it**.
4. Ensure all additions **stay within the Key Insights format**.
5. The final output **should differ from the input summary**.

<FORMATTING>
- Output **ONLY** the key insights as bullet points (no introduction, no titles).
- Use **concise, fact-based sentences**.
- **Do NOT use XML tags** in the output.
</FORMATTING>
"""


reflection_instructions = """You are an expert research assistant analyzing a summary about {research_topic}.

<GOAL>
1. Identify knowledge gaps or areas that need deeper exploration
2. Generate a follow-up question that would help expand your understanding
3. Focus on technical details, implementation specifics, or emerging trends that weren't fully covered
</GOAL>

<REQUIREMENTS>
Ensure the follow-up question is self-contained and includes necessary context for web search.
</REQUIREMENTS>

<FORMAT>
Format your response as a JSON object with these exact keys:
- knowledge_gap: Describe what information is missing or needs clarification
- follow_up_query: Write a specific question to address this gap
</FORMAT>

<EXAMPLE>
Example output:
{{
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks",
    "follow_up_query": "What are typical performance benchmarks and metrics used to evaluate [specific technology]?"
}}
</EXAMPLE>

Provide your analysis in JSON format:"""

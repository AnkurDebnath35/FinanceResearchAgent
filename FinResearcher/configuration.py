import os
from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, Optional, Literal
from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig

load_dotenv()

class SearchAPI(Enum):
    PERPLEXITY = "perplexity"
    TAVILY = "tavily"
    DUCKDUCKGO = "duckduckgo"
    SEARXNG = "searxng"

class Configuration(BaseModel):
    """The configurable fields for the research assistant."""

    max_web_research_loops: int = Field(
        default=int(os.getenv("MAX_WEB_RESEARCH_LOOPS", 3)),
        title="Research Depth",
        description="Number of research iterations to perform"
    )
    local_llm: str = Field(
        default="llama3.2",
        title="LLM Model Name",
        description="Name of the LLM model to use"
    )
    llm: str = Field(
        default=os.getenv("LLM"),
        title="LLM Model Name",
        description="Name of the LLM model to use"
    )
    llm_provider: Literal["ollama", "groq"] = Field(
        default=os.getenv("LLM_PROVIDER", "ollama"),
        title="LLM Provider",
        description="Provider for the LLM (Ollama, LMStudio, or Groq)"
    )
    search_api: Literal["perplexity", "tavily", "duckduckgo"] = Field(
        default=os.getenv("SEARCH_API", "duckduckgo"),
        title="Search API",
        description="Web search API to use"
    )
    fetch_full_page: bool = Field(
        default=os.getenv("FETCH_FULL_PAGE", "True").lower() == "true",
        title="Fetch Full Page",
        description="Include the full page content in the search results"
    )
    ollama_base_url: str = Field(
        default="http://localhost:11434/",
        title="Ollama Base URL",
        description="Base URL for Ollama API"
    )
    groq_api_key: Optional[str] = Field(
        default=os.getenv("GROQ_API_KEY"),
        title="Groq API Key",
        description="API key for Groq LLM service"
    )
    strip_thinking_tokens: bool = Field(
        default=True,
        title="Strip Thinking Tokens",
        description="Whether to strip <think> tokens from model responses"
    )
    include_domains: list[str] = Field(
        default=os.getenv("INCLUDE_DOMAINS", "").split(","),
        title="Include Domains",
        description="List of domains to prioritize in search results"
    )

    @classmethod
    def from_runnable_config(cls) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        return cls()

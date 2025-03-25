# 📊 Finance Research Agent 🚀

A powerful **AI-driven research assistant** that automates financial research using **LangGraph, Chainlit, and LLMs** (Groq/Ollama). It fetches and summarizes the latest financial news, trends, and reports from the web in real time.

---

## 🌟 Features

✅ **Automated Financial Research** – Fetches real-time data from top sources  
✅ **LLM-Powered Summarization** – Uses Groq/Ollama for structured insights  
✅ **User-Friendly** - Deployable as a Chanilit UI for conversational applications  
✅ **Real-Time Streaming** – Word-by-word response rendering for natural typing  
✅ **Web Search APIs** – Supports Tavily, Perplexity, and DuckDuckGo  
✅ **Docker Support** – Easily deployable using Docker  

---

## 📁 Project Structure
```bash
FinanceResearchAgent/
│── Dockerfile
│── .env
│── requirements.txt
│── README.md
│── app.py
│── docker-compose.yml
│── FinResearcher/
│   │── __init__.py
│   │── graph.py
│   │── configuration.py
│   │── state.py
│   │── prompts.py
│   │── utils.py
```


---

## 🔧 Setup Instructions

### **1️⃣ Clone the Repository**
```shell
git clone https://github.com/AnkurDebnath35/FinanceResearchAgent.git
cd FinanceResearchAgent
```

---

**2️⃣ Install Dependencies**  
Ensure you have Python 3.10+ installed.

```shell
pip install -r requirements.txt
```
---

**3️⃣ Set Up Environment Variables**  
Create a .env file in the root directory with:

```ini
# Web Search API Keys
TAVILY_API_KEY=your-tavily-api-key
PERPLEXITY_API_KEY=your-perplexity-api-key

# LLM Configuration
LLM_PROVIDER=groq
GROQ_API_KEY=your-groq-api-key
OLLAMA_BASE_URL=http://localhost:11434
```
---
**4️⃣ Run the FastAPI Server**  
Start the FastAPI server to expose the research endpoint:
```bash
uvicorn fastapi_app:app --host 0.0.0.0 --port 8500 --reload

```
**Access the FastAPI Documentation:** 
Once the server is running, 
navigate to http://localhost:8500/docs to view the interactive API documentation provided by FastAPI.

**5️⃣ Run the Chainlit App**
```shell
chainlit run app.py --host 0.0.0.0 --port 8000
```
Access it at http://localhost:8000 🚀

**6️⃣ Using the FastAPI Endpoint**  
The FastAPI server provides an endpoint to perform financial research.

Endpoint: ```/run_research```

Method: ```POST```

Request Body:

```json
{
  "research_topic": "Your research topic here"
}
```
Response:

```json

{
  "summary": "Generated research summary..."
}
```

Example using curl:

```bash

curl -X POST "http://localhost:8500/run_research" \
     -H "Content-Type: application/json" \
     -d '{"research_topic": "Latest stock market trends"}'
```

Example using PowerShell:

```powershell

Invoke-RestMethod -Uri "http://localhost:8000/run_research" `
  -Method Post `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"research_topic": "Latest stock market trends"}'
```
---
## 🐳 Running with Docker  
**7️⃣ Build the Docker Image**
```bash
docker build -t finance-research-agent .
```
---

**8️⃣ Run the Container**

```bash
docker run -p 8500:8500 -p 8000:8000 --env-file .env finance-research-agent
Now, visit http://localhost:8000 🎯
```
**9️⃣ Build & Run the Container using ```docker-compose.yml```**
```bash
docker-compose build
docker-compose up
```

## 🛠️ Configuration Options

Modify FinResearcher/configuration.py to customize:

    - LLM Provider (Groq, Ollama)
    
    - Search API (Tavily, Perplexity, DuckDuckGo)
    
    - Max Research Loops

    - Search Domains (INCLUDE_DOMAINS)

## 📌 Example Usage
💬 User: "Analyze the impact of AI on finance"
🤖 AI Response:

```yaml
# Summary
AI is transforming the finance industry by enhancing risk management, fraud detection, and algorithmic trading. Banks and hedge funds increasingly rely on machine learning for predictive analytics...

---
## Sources
- AI in Finance - Bloomberg: https://bloomberg.com/ai-finance
- Machine Learning for Risk - MIT Tech Review: https://technologyreview.com/ml-risk
```

## 🎯 Roadmap  
## 🚀 Upcoming Features:

      

    - Works good for local LLMs but with Provider hosted LLM, it makes too many calls (controled by ```MAX_WEB_RESEARCH_LOOPS```)
    
    - Conversation Memory with LangChain
    
    - Financial QA
    
    - Customizable Report Generation


## 🤝 Contributing

We welcome contributions! Fork the repo, create a new branch, and submit a pull request.

## 📝 License

This project is licensed under MIT License.

## 📞 Contact
For questions, reach out via:  
📧 Email: ankurdebnath35@gmail.com  
🐦 Twitter: @yourhandle

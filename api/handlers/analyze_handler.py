from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os

router = APIRouter()

class CodeRequest(BaseModel):
    language: str
    code: str

# LLM API interaction
def analyze_with_llm(code: str):
    prompt = f"Analyze the following code and provide recommendations for security, performance, and code quality improvements:\n{code}"
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}", "Content-Type": "application/json"},
        json={
            "model": "gpt-4",
            "prompt": prompt,
            "max_tokens": 500
        }
    )
    return response.json()

@router.post("/analyze")
async def analyze_code(request: CodeRequest):
    try:
        if request.language not in ["python", "javascript", "java", "go", "typescript"]:
            raise HTTPException(status_code=400, detail="Unsupported language")
        
        # Analyze code with LLM
        analysis_result = analyze_with_llm(request.code)
        
        # Log the result
        with open("/logs/deepcode_api.log", "a") as log_file:
            log_file.write(f"Analysis result for {request.language}: {analysis_result}\n")
        
        return {"status": "Analysis complete", "result": analysis_result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from recommendation_ai_agent.prompt import instruction_prompt
import json

from config import settings

def get_recomendation(final_score,frame_level_output):
    """Get response from Gemini model with error handling and logging"""
    try:
        
        
        # Initialize LangChain-compatible Gemini model
        try:
            print("==============================================")
            # print("settings.GOOGLE_API_KEY",settings.GOOGLE_API_KEY)
            model = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                api_key="AIzaSyB0m-jA_y459bjEG18kdhNtjBHmxFxqViY"
            )
        except Exception as e:
            print(f"Failed to initialize Gemini model: {e}")
            return "I'm having trouble connecting to the AI service. Please try again later."
    
        # Create prompt with conversation history
        try:
            prompt_template = PromptTemplate(
                input_variables=["final_score","frame_level_output"],
                template=instruction_prompt
            )
            
            # Get response from the model
            chain = prompt_template | model
            response = chain.invoke({
                "final_score": final_score,
                "frame_level_output":frame_level_output
            })
            print("response",response.content)
            result = {"recommendation":response.content}
            with open("output/recomendation.json", "w") as f:
                json.dump(result, f, indent=2)
            print("Successfully received response from Gemini model")
            
            return response.content
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I encountered an error while processing your request. Please try again."
            
    except Exception as e:
        print(f"Unexpected error in get_gemini_response: {e}")
        return "I'm sorry, something went wrong. Our team has been notified. Please try again later."
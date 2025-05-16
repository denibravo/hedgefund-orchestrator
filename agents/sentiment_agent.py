import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import os

def create_sentiment_agent(kernel: sk.Kernel):
    kernel.add_service(
        OpenAIChatCompletion(
            ai_model_id="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY"),
        )
    )

    prompt = "Is the sentiment Bullish or Bearish?\nTicker: {{ticker}}\nHeadlines: {{headlines}}"

    return kernel.create_function_from_prompt(
        function_name="SentimentAgent",
        plugin_name="Sentiment",
        prompt_template=prompt,
    )

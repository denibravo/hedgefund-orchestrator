import semantic_kernel as sk
from agents.sentiment_agent import create_sentiment_agent

def main():
    kernel = sk.Kernel()
    sentiment = create_sentiment_agent(kernel)

    result = sentiment.invoke(kernel, input={"ticker": "AAPL", "headlines": "Apple stock surges after strong iPhone sales."})
    print(result.output)

if __name__ == "__main__":
    main()

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "anthropic"  # Use a different model
config["backend_url"] = "https://api.anthropic.com"  # Use a different backend
config["deep_think_llm"] = "claude-3-5-sonnet-20240620"  # Use a different model
config["quick_think_llm"] = "claude-3-5-haiku-20241022"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("LEU", "2025-07-28")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns

import os
import litellm

os.environ["OPENROUTER_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["OPENROUTER_API_KEY"] = "sk-or-v1-test"

for model in ["openrouter/owl-alpha", "deepseek/deepseek-v4-flash"]:
    try:
        # litellm usually resolves base_url using get_api_base
        api_base = litellm.get_api_base(model=model, optional_params={})
        print(f"model={model} api_base={api_base}")
    except Exception as e:
        print(f"model={model} error={e}")

    try:
        provider = litellm.utils.get_llm_provider(model)[1]
        print(f"model={model} provider={provider}")
    except Exception as e:
        print(f"model={model} provider_error={e}")

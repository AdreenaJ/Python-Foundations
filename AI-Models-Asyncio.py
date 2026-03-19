import asyncio
import random

async def call_ai_model(model_name, delay):
    print(f"Sending request to {model_name} (est. {delay:.1f}s)...")
    await asyncio.sleep(delay) 
    return f"[{model_name}] Success!"

async def main():
    # We set a strict limit: no model can take longer than 2 seconds
    TIMEOUT_LIMIT = 2.0
    
    models = [
        ("Gemini-4", random.uniform(0.5, 3.5)),
        ("Local-Llama", random.uniform(0.5, 3.5)),
        ("Vision-Pro", random.uniform(0.5, 3.5))
    ]

    tasks = []
    for name, delay in models:
        # Wrap each call in a wait_for coroutine
        tasks.append(asyncio.wait_for(call_ai_model(name, delay), timeout=TIMEOUT_LIMIT))

    print(f"Starting Multi-AI Request (Max wait: {TIMEOUT_LIMIT}s)...")
    
    # Using return_exceptions=True allows the script to continue 
    # even if some models hit the timeout
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    print("\n--- Final Results ---")
    for i, res in enumerate(results):
        model_name = models[i][0]
        if isinstance(res, asyncio.TimeoutError):
            print(f"{model_name}: Request timed out!")
        else:
            print(f"{res}")

if __name__ == "__main__":
    asyncio.run(main())
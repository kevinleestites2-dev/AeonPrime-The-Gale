import asyncio
import time

class FastAgent:
    def __init__(self, agent_id):
        self.start = time.perf_counter_ns()
        self.id = agent_id
        self.init_time = time.perf_counter_ns() - self.start

async def burst_test(count):
    start_test = time.perf_counter()
    agents = [FastAgent(i) for i in range(count)]
    end_test = time.perf_counter()
    
    total_time_ms = (end_test - start_test) * 1000
    avg_init_us = (total_time_ms * 1000) / count
    
    print(f"🌬️ GALE BURST: {count} Agents Manifested")
    print(f"⚡ Total Time: {total_time_ms:.4f}ms")
    print(f"🔥 Avg Init Speed: {avg_init_us:.4f}μs per agent")

if __name__ == "__main__":
    asyncio.run(burst_test(1000))

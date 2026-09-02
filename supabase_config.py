import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Supabase configuration - use environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://your-project.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-anon-key-here")

def get_supabase_config():
    return {
        "url": SUPABASE_URL,
        "key": SUPABASE_KEY
    }

if __name__ == "__main__":
    config = get_supabase_config()
    print(f"Supabase URL: {config['url']}")
    print(f"Supabase Key: {config['key'][:30]}...")
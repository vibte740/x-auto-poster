import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Supabase configuration
SUPABASE_URL = "https://psupntfqbnyawrzugaeu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBzdXBudGZxYm55YXdyenVnYWV1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NzMyOTQwMCwiZXhwIjoyMTAyOTA1NDAwfQ.Bs2h2lmMjjpmDPLoU-KY_HR7OAr0-y9aNnC-G15T02s"

def get_supabase_config():
    return {
        "url": SUPABASE_URL,
        "key": SUPABASE_KEY
    }

if __name__ == "__main__":
    config = get_supabase_config()
    print(f"Supabase URL: {config['url']}")
    print(f"Supabase Key: {config['key'][:30]}...")

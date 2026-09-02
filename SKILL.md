# Skill: X.com Auto-Poster

Posts breaking war and financial news to X.com with research-first approach and unique content rewriting.

## Features

- Research-first approach: Search X.com for trending posts before creating content
- Fetches war and financial news from Google News RSS
- **Unique content rewriting**: Paraphrases news to avoid X blocking (no exact phrases)
- **No source names**: Removes "- BBC", "- CNN", "- NPR" from tweets
- Generates hashtags based on news content
- **Images required**: Every post includes image for 2-3x impressions
- Supabase duplicate checking before posting
- Logs to JSON, Supabase, and Notion

## Usage

### Post Now
```bash
python C:\Users\K1\.claude\skills\x-auto-poster\auto_post.py
```

## Posting Workflow

1. **Search X.com** for high-impression war/finance posts
2. **Grab subject** from top posts
3. **Research topic** on web for detailed info
4. **Rewrite content uniquely** - paraphrase, don't copy exact phrases
5. **Add relevant image** from Unsplash (required for impressions)
6. **Check Supabase** for duplicates
7. **Post and log** to JSON + Supabase + Notion

## Hashtag Logic

- **War news**: #Iran, #Ukraine, #Russia, #NATO, #Missiles + #War #Breaking
- **Finance news**: #Stocks, #Crypto, #Oil, #Fed + #Finance #Breaking
- **General**: #News #Breaking #Trending

## Requirements

- browser-use CLI
- Chrome with remote debugging
- Logged into X.com
- Notion integration connected
- Supabase project with x_posts table

## Supabase Table: x_posts

Columns: id, tweet_content, category, news_title, image_path, status, created_at, tweeted

## Notion Logging

All posts are logged to Notion page `x_com_posts` with:
- Timestamp
- Tweet content
- Category
- Status

## Anti-Blocking Rules

- ❌ Never post exact news headlines
- ❌ Never include source names (BBC, CNN, NPR, etc.)
- ✅ Rewrite in unique voice with templates
- ✅ Use images for every post
- ✅ Check Supabase for duplicates before posting
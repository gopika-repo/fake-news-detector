from duckduckgo_search import DDGS

class FactChecker:
    def __init__(self):
        # Trusted domains whitelist
        self.trusted_domains = [
            "reuters.com", "apnews.com", "bbc.com", "npr.org", 
            "snopes.com", "politifact.com", "factcheck.org", "cnn.com", 
            "nytimes.com", "washingtonpost.com", "theguardian.com"
        ]
        
    def verify_news(self, headline):
        print(f"🔎 Searching DuckDuckGo for: {headline}...")
        
        fact_check_hits = 0
        trusted_hits = 0
        results_data = []
        
        try:
            # Use DuckDuckGo (DDGS) to search
            # max_results=5 gets the top 5 links
            results = DDGS().text(headline, max_results=5)
            
            # If DDGS returns nothing (rare), return unverified
            if not results:
                return "❓ UNVERIFIED: No relevant news found.", []

            for result in results:
                # DuckDuckGo returns keys: 'title', 'href', 'body'
                url = result['href']
                title = result['title']
                description = result['body']
                
                # Extract domain (e.g., 'https://www.bbc.com/news' -> 'bbc.com')
                try:
                    domain = url.split("/")[2]
                except:
                    domain = "unknown"

                # Check for Keywords
                text_to_check = (title + " " + description).lower()
                is_fact_check = any(word in text_to_check 
                                  for word in ["fact check", "debunked", "hoax", "false claim", "fake news"])
                
                is_trusted = any(trusted in domain for trusted in self.trusted_domains)
                
                if is_fact_check:
                    fact_check_hits += 1
                if is_trusted:
                    trusted_hits += 1
                    
                results_data.append({
                    "title": title,
                    "url": url,
                    "domain": domain,
                    "is_trusted": is_trusted,
                    "is_fact_check": is_fact_check
                })
                
            # LOGIC: Determine Verdict
            if fact_check_hits > 0:
                verdict = "⚠️ CAUTION: This topic has been flagged by fact-checkers."
            elif trusted_hits > 0:
                verdict = "✅ VERIFIED: Reported by trusted sources."
            elif len(results_data) == 0:
                verdict = "❓ UNVERIFIED: No relevant news found."
            else:
                verdict = "ℹ️ NEUTRAL: Sources found, but not in trusted list."
                
            return verdict, results_data

        except Exception as e:
            print(f"Error details: {e}")
            return f"❌ Error searching web: {str(e)}", []
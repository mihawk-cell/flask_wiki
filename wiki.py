import wikipedia

def get_wikipedia_page(query):
    """
    Use the Wikipedia API to search pages and return the title, summary, and URL.
    """
    try:
        page = wikipedia.page(query, auto_suggest=False)
        return {
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        }
    except wikipedia.DisambiguationError as e:
        return {
            "error": "disambiguation",
            "options": e.options
        }
    except wikipedia.PageError:
        return {
            "error": "not_found"
        }

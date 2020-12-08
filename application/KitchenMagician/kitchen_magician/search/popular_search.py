from search.models import SearchKeyword

def popular_search(n=3):
    # Return top n search, default set is top 3 search
    search_keywords = SearchKeyword.objects.order_by("-count")[:n]
    popular_search_keywords = [search_keyword.keyword for search_keyword in search_keywords]
    # print(popular_search_keywords)
    return popular_search_keywords

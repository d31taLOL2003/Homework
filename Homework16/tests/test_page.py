def test_page(main_page):
    """
    The function tests the navigation on the site. It selects a category, a subcategory,
    and an article and scrolls the page to the subtitle of the article.
    Args:
        main_page: an instance of the MainPage class used to navigate the website

    Returns:
        None
    """
    main_page.choose_category("Стрічка")
    article_list = main_page.choose_sub_category("📊 Аналітика")
    article = article_list.choose_article()
    article.scroll_to_title("Портрет учасників опитування")

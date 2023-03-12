def test_page(main_page):
    """
    Test of choosing a category and subcategory, selecting an article,
    scrolling to a particular section, and clicking a button.

    Args:
        main_page: The MainPage object representing the main page of the website.

    Returns:
        None
    """
    main_page.choose_category("Стрічка")
    article_list = main_page.choose_sub_category("📊 Аналітика")
    article = article_list.choose_article()
    article.scroll_to_title("Медіанні зарплати")
    element = article.click_button("Київ")
    
    assert element.is_enabled() and element.is_displayed()

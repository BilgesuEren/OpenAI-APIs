class Prompts:
    
    zero_shot_prompt = lambda video_titles: f"""
        The video title will be separated by a new line character. Do not write anything else and only specify one category for per channel.
        {video_titles}"""
        
    certanty_one_shot_prompt = lambda video_titles: f"""
        Given a list of video titles, classify them into one of the categories. 
        Reply with the category and your certainty level. Only specify one category and certainty level in the format: category, certainty level. Do not write anything else.
        **Example:**
        Video Titles: Reviewing EVERY Samsung Galaxy S Ever!, Small Phones are Dead and We Killed Them
        Tech, 99

        Video Titles: {video_titles}
    """
        
    one_shot_prompt = lambda video_titles: f"""
        Given the video titles below, provide the most appropriate category.
        Do not write anything else and only specify one category for per channel.
        Categories:
        Auto & Vehicles, 
        Sports Editorial Content, 
        Entertainment, 
        Kids Content, 
        Family,
        News,
        Politics & Information, 
        Gaming, 
        Tech,
        Education & Science,
        Food & Drinks, 
        Corporate Channels, 
        Lifestyle & Hobbies, 
        Health & Fitness.
        
        Example:
        Video Titles: BMW N47 N57 Schaden Hochdruckpumpe günstig selber reparieren,
        VW Audi Seat Skoda 2.0 TDI startet schlecht | Drosselklappe + Sicherung (TUTORIAL),
        Legal besser Sehen!  Von Halogen auf LED  umrüsten,
        Total legal mit 15 Jahren Auto Fahren,
        
        Auto & Vehicles
        
        Video Titles:
        {video_titles}
        
        (Your Answer)
    """
    
    two_shot_prompt =  lambda video_titles: f"""
        Classify the following video titles into one of these categories.
        Do not write anything else and only specify one category for per channel.
        Examples:
        Video Titles:
        "FREE: GEMMAF Qualifiers #2", "Auch das noch: NÃ¤chster Top-Star verlÃ¤sst Bayern?!"
        Sports Editorial Content
         "5-Minuten Wraps, die immer & Ã¼berall funktionieren!", "Noch GemÃ¼se zuhause? Dann mach dir dieses Quiche Rezept!"
         
        Food & Drinks

        Video Titles:
        {video_titles}
        
        (Your Answer)
        """
    simple_zero_shot_prompt = lambda video_titles: f"""
        The following are video titles from a single YouTube channel. Determine the vertical category of the channel based on these titles. 
        The possible categories are: 
        Auto & Vehicles, 
        Sports Editorial Content, 
        Entertainment, 
        Kids Content, 
        Family,
        News,
        Politics & Information, 
        Gaming, 
        Tech,
        Education & Science,
        Food & Drinks, 
        Corporate Channels, 
        Lifestyle & Hobbies, 
        Health & Fitness.

        Video Titles:
        {video_titles}

        Do not write anything else and only specify one category for per channel.
    """
    
    reference_text_prompt = lambda video_titles: f"""
        Here are examples of video titles and their corresponding categories. Use these examples to classify the provided video titles accurately. Only specify one category for each channel.

        Reference Examples:
        - "Ohaaa der ERSTE FENTY BEAUTY Adventskalender 2023 top oder flop?", "Tierkommunikation - Wie Molly plÃ¶tzlich geheilt wurde"
          Lifestyle & Hobbies
        - "5-Minuten Wraps, die immer & Ã¼berall funktionieren!", "Noch GemÃ¼se zuhause? Dann mach dir dieses Quiche Rezept!"
           Food & Drinks
        - "FREE: GEMMAF Qualifiers #2", "Auch das noch: NÃ¤chster Top-Star verlÃ¤sst Bayern?!"
          Sports Editorial Content
        - "Das letzte Video von GIGA Android!!", "Honor 7 - Test - Deutsch - GIGA.DE"
          Tech

        Video Titles:
        {video_titles}

        (Your Answer)
    """
    
    
    step_by_step_prompt = lambda video_titles: f"""
        Follow the steps below to determine the correct category for the provided video titles. Only specify one category for each channel.

        Step-by-Step Instructions:
        1. Carefully read each video title provided.
        2. Compare the content of the video titles with the predefined categories.
        3. Identify the common theme or subject matter that best describes the majority of the video titles.
        4. Select the most appropriate category from the predefined list based on your analysis.
        5. Do not include any extra words or sentences in your response; only provide the category.

        The predefined categories are: Auto & Vehicles, Sports Editorial Content, Entertainment, Kids Content, Family, News Politics, & Information, Gaming, Tech, Education & Science, Food & Drinks, Corporate Channels, Lifestyle & Hobbies, Health & Fitness.

        Example:
        Video Titles: 
        Manueller WeiÃŸabgleich I Fotografie Grundlagen, Was ist der RAW Converter - Teil 3 I Gradationskurven I TUTORIAL, BeFunky - App der Woche - Bildbearbeitung Easy, Froschperspektive,
        Was ist der RAW Converter - Teil 4 I Fotos schÃ¤rfen I TUTORIAL, Outschied und Abtakes - GIGA FOTO sagt DANKE, Unscharfe Fotos durch die BeugungsunschÃ¤rfe I Fotografie  Grundlagen, Was ist der RAW Converter - Teil 6 I Teiltonung I TUTORIAL, Apple iPhone 12 (Pro) Clear Case Review 

        Auto & Vehicles

        Now, classify the following video titles:

        Video Titles:
        {video_titles}

        (Your Answer)
    """

from typing import Dict, Union

from ..enums.categories import FunCategory, FapCategory
from ..enums.site import SITE

fun_category_keys: Dict[str, FunCategory] = {
    "0_0": FunCategory.ALL_CATEGORIES,
    
    "1_0": FunCategory.ANIME,
    "1_1": FunCategory.ANIME_AMV,
    "1_2": FunCategory.ANIME_ENGLISH_TRANSLATED,
    "1_3": FunCategory.ANIME_NON_ENGLISH_TRANSLATED,
    "1_4": FunCategory.ANIME_RAW,
    
    "2_0": FunCategory.AUDIO,
    "2_1": FunCategory.AUDIO_LOSSLESS,
    "2_3": FunCategory.AUDIO_LOSSY,
    
    "3_0": FunCategory.LITERATURE,
    "3_1": FunCategory.LITERATURE_ENGLISH_TRANSLATED,
    "3_2": FunCategory.LITERATURE_NON_ENGLISH_TRANSLATED,
    "3_3": FunCategory.LITERATURE_RAW,
    
    "4_0": FunCategory.LIVE_ACTION,
    "4_1": FunCategory.LIVE_ACTION_ENGLISH_TRANSLATED,
    "4_2": FunCategory.LIVE_ACTION_IDOL_PROMOTIONAL_VIDEO,
    "4_3": FunCategory.LIVE_ACTION_NON_ENGLISH_TRANSLATED,
    "4_4": FunCategory.LIVE_ACTION_RAW,
    
    "5_0": FunCategory.PICTURES,
    "5_1": FunCategory.PICTURES_GRAPHICS,
    "5_2": FunCategory.PICTURES_PHOTOS,
    
    "6_0": FunCategory.SOFTWARE,
    "6_1": FunCategory.SOFTWARE_APPLICATIONS,
    "6_2": FunCategory.SOFTWARE_GAMES
}

fap_category_keys: Dict[str, FapCategory] = {
    "0_0": FapCategory.ALL_CATEGORIES,
    
    "1_0": FapCategory.ART,
    "1_1": FapCategory.ART_ANIME,
    "1_2": FapCategory.ART_DOUJINSHI,
    "1_3": FapCategory.ART_GAMES,
    "1_4": FapCategory.ART_MANGA,
    "1_5": FapCategory.ART_PICTURES,
    
    "2_0": FapCategory.REAL_LIFE,
    "2_1": FapCategory.REAL_LIFE_PHOTOBOOKS_AND_PICTURES,
    "2_2": FapCategory.REAL_LIFE_VIDEOS
}

fun_category_titles: Dict[str, str] = {
    "0_0": "All Categories",
    
    "1_0": "Anime",
    "1_1": "Anime - Anime Music Video",
    "1_2": "Anime - English-Translated",
    "1_3": "Anime - Non-English-Translated",
    "1_4": "Anime - Raw",
    
    "2_0": "Audio",
    "2_1": "Audio - Lossless",
    "2_2": "Audio - Lossy",
    
    "3_0": "Literature",
    "3_1": "Literature - English-Translated",
    "3_2": "Literature - Non-English-Translated",
    "3_3": "Literature - Raw",
    
    "4_0": "Live Action",
    "4_1": "Live Action - English-Translated",
    "4_2": "Live Action - Idol/Promotional Video",
    "4_3": "Live Action - Non-English-Translated",
    "4_4": "Live Action - Raw",
    
    "5_0": "Pictures",
    "5_1": "Pictures - Graphics",
    "5_2": "Pictures - Photos",
    
    "6_0": "Software",
    "6_1": "Software - Applications",
    "6_2": "Software - Games"
}

fap_category_titles: Dict[str, str] = {
    "0_0": "All Categories",
    
    "1_0": "Art",
    "1_1": "Art - Anime",
    "1_2": "Art - Doujinshi",
    "1_3": "Art - Games",
    "1_4": "Art - Manga",
    "1_5": "Art - Pictures",
    
    "2_0": "Real Life",
    "2_1": "Real Life - Photobooks And Pictures",
    "2_2": "Real Life - Videos"
}

def get_category_by_key(site: SITE, key: str) -> Union[FunCategory, FapCategory]:
    if site == SITE.FUN:
        return fun_category_keys[key]
    elif site == SITE.FAP:
        return fap_category_keys[key]
    else:
        raise ValueError(f"Unknown site: {site}")

def get_category_title_by_key(site: SITE, key: str) -> str:
    if site == SITE.FUN:
        return fun_category_titles[key]
    elif site == SITE.FAP:
        return fap_category_titles[key]
    else:
        raise ValueError(f"Unknown site: {site}")
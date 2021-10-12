# Project ai


## Data set structure
### steam_games.json
publisher: string<br>
genres: list \<string\><br>
app_name: string<br>
title: string<br>
url: string<br>
release_date: date<br>
tags: list \<string\><br>
discount_price: float<br>
reviews_url: string<br>
specs: list \<string\> (ook een soort tag)<br>
price: float<br>
developr: string<br>
sentiment: string (mostly positive, ..)<br>
metascore: int of float
### australian_users_items.json
user_id: int<br>
items_count: int<br>
steam_id: int<br>
user_url: string<br>
items: list \<dict{item_id, item_name, playtime_forever, playtime_2weeks}\>
### australian_user_reviews.json
user_id: int<br>
user_url: string<br>
reviews: list\<dict{funny, posted (string), last_edited, item_id, helpful (string), recommend, review (string)}\>
### bundle_data.json
bundle_final_price: string<br>
budle_url: string<br>
bundle_price: string<br>
bundle_name: string<br>
bundle_id: int<br>
items: list\<dict{genre, item_id, discounted_price, item_url, item_name}\><br>
bundle_discount: string
### steam_reviews.json
username: string<br>
product_id: int<br>
page_order: int<br>
text: string<br>
hours: float<br>
recommended: bool<br>
produccts: float<br>
date: date<br>
early_access: bool<br>
page: int<br>
compensation: string<br>
found_funny: ?<br>
user_id: int

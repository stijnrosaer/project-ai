# Project artificial intelligence

This repository is created to contain all jupyter notebooks and other files for the course **Project artificial
intelligence** at the University of Antwerp. The notebooks can be found in the notebooks directory.

The goal of this project was to implement a paper, describing a method for a recommendation systems. We chose
the [Efficient Adaptive-Support Association Rule Mining for Recommender Systems](https://link.springer.com/content/pdf/10.1023/A:1013284820704.pdf)
paper because it tackles an interesting problem, which is the fixed support that has to be defined. Unfortunately, we
quickly noticed some problems with their method which will be described later.

## Data source

All data used for this project is from a steam dataset that can be found
at [this link](http://deepx.ucsd.edu/public/jmcauley/steam/). Information about this dataset (and several other) is
present on the website of Julian McAuley at UCSD https://cseweb.ucsd.edu/~jmcauley/datasets.html

### Data set structure

We made an overview of the datasets that are available from steam, including the datatype of the different columns. This
made it easier for us to evaluate the data and see what could possibly be used.

#### steam_games.json

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

#### australian_users_items.json

user_id: int<br>
items_count: int<br>
steam_id: int<br>
user_url: string<br>
items: list \<dict{item_id, item_name, playtime_forever, playtime_2weeks}\>

#### australian_user_reviews.json

user_id: int<br>
user_url: string<br>
reviews: list\<dict{funny, posted (string), last_edited, item_id, helpful (string), recommend, review (string)}\>

#### bundle_data.json

bundle_final_price: string<br>
budle_url: string<br>
bundle_price: string<br>
bundle_name: string<br>
bundle_id: int<br>
items: list\<dict{genre, item_id, discounted_price, item_url, item_name}\><br>
bundle_discount: string

#### steam_reviews.json

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

### Used dataset

We first started by using the steam_reviews dataset because this is the largest available. Containing over 7M reviews,
2M users and 15K items, we expected this one to be the most useful available. We did this because we expected a large
enough amount of interactions per item. Unfortunately this was not the case.

We observed an average amount of interactions per user of just over 2 items. This is of course not enough to build
decent association rules. This setup only yielded in a hitrate of 0.06%. This is an awful result, knowing that a
popularity recommender offers a hitrate of about 6%.

Another issue we had with is dataset is that we were not able to apply the necessary preprocessing as described int the
paper.

This is why we decided to discontinue the uses of this dataset and started using the australian_users_items. This
dataset contains all the games that users have in their library. Even though the amount of interactions is lower in this
dataset, the data is much denser and the amount of interactions per user was higher.

## Implementation

We implemented everything in jupyter notebooks because this allowed us to do more testing without having to rerun all
the previous functions. We separated it into 4 files: dataloading, preprocessing, building of association rules, and
recommender. This allowed us to focus on one specific part, without having to cope with a larger codebase. After each
notebook, we stored the generated data using `pickle`for further use in other notebooks.

### Paper

We were unable to implement the specific implementation as described in the paper because special C++ and custom
datastructures are required for an efficient and effective result. This is why we decided to not continue this thought
process, but instead used éclat for generating association rules with an as low as possible support, in order to
simulate the results achieved in the paper.

The preprocessing done in the paper is very optimistic, but we were able to recreate the similar conditions with our
dataset. For training, we only used the first 1000 users in the dataset that have a at least 100 interactions. We know
that this is often not feasible in real-world scenarios. This is why we believe that the proposed method is not very
usable in this case.

A train/test split was created based on a user split i.e. a split where the users present in the test set, are not
contained in the training set. The advantage of this method over a session based split is that more interactions pre
user last after doing the split.

We did use both user association rules and article association rules in the way described in the paper. This did indeed
improve the hitrate of +- 30%, which is over basic article association rules. This was achieved using a 4-fold cross
validation on the test set.
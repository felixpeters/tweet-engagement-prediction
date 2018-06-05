# Tweet Engagement Prediction

This work is building on my masters thesis at the [Information Systems](https://www.is.tu-darmstadt.de/fachgebiet_is/index.en.jsp) chair
of TU Darmstadt.
It applies deep learning techniques to the problem of tweet engagement prediction.

## Objective

Build increasingly complex deep neural networks for predicting retweet counts.
An emphasis is put on the development of models suitable for production settings,
i.e., capable of making real-time predictions.
In other words, preprocessing should be kept at a minimum and all input data should
stem from tweet objects as fetched from the public Twitter API.

Two specific tasks will be examined:
* Regression task: predict positive, real-valued number for eventual retweet count
* Classification task: predict certain range for eventual retweet count

Classes for classification task: `0, 1-9, 10-99, 100-999, >=1,000`

**Assumption:** All examined tweets are at least one month old at the time of
collection, s.th. the retweet process can be seen as exhausted (based on observations by [Kwak et al. 2010](https://www.cs.bgu.ac.il/~snean151/wiki.files/22-WhatisTwitterASocialNetworkOrANewsMedia.pdf)).

## Data

Tweets come from a variety of user groups, namely:
* corporations (Fortune 500 and startups)
* politicians (US senators and governors)
* celebrities (athletes, musicians, actors,...)
* journalists (political, pop culture,...)

For the assembled accounts, all tweets from March 2016 to March 2018 were collected,
leaving out retweets without a quote.
The final data set contains a total of around **1.3 million tweets**.

## Setup

Valid Twitter credentials are needed in order establish an API connection.
Credentials should be stored in an `.env` file and will be loaded in the
respective modules.

All results can be reproduced using notebooks in the `nbs` directory.

## Contact

For further questions regarding this work, contact the repository owner:
* [Github](https://github.com/felixpeters)
* [Twitter](https://twitter.com/_fpeters)
* [LinkedIn](https://www.linkedin.com/in/petersfelix/)

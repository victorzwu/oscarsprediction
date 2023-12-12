# Predicting Oscar Nominees: A Multi-Labelling Approach

**Authors:**
- Victor Wu, wu.victo@northeastern.edu
- Macarious Kin Fung Hui, hui.mac@northeastern.edu
- Tianyi Zhang, zhang.tianyi9@northeastern.edu

## Abstract

The allure of an Oscar nomination is a pinnacle achievement in the film industry, representing artistic and technical excellence. In this study, we present a meticulous exploration of predicting Oscar nominations across 13 major categories using machine learning techniques. Our multi-label classification approach considers diverse features such as awards, movie attributes, and critical acclaim. We deploy logistic regression, neural networks, and a random forest model to predict the likelihood of nominations. The evaluation, instead of traditional accuracy, encompasses balanced accuracy, precision, recall, and F1-score, to address challenges posed by class imbalances. Additionally, we unravel feature importance, offering insights into the factors influencing nominations. Model interpretability is achieved through visualizations and decision trees. Our work not only contributes to predicting Oscar nominations but also sheds light on the complex interplay of factors in the film industry.

## Introduction

The Oscars highlight a film's artistic and technical merits in the movie industry. Each year, the excitement and speculation around the nominations demonstrate the importance of the awards that go beyond the screen. Campaigning for nominations is a high-stakes effort for studios and filmmakers, given the prestige, opportunities, and lucrative media coverage the award show offers. However, the journey to securing a nomination is often opaque and subject to a great deal of uncertainty. As a result, forecasting Oscar nominations can be challenging and difficult due to the weight of cultural, economic, and political factors that contribute to them.

The consumption and recognition of cinema have long defined cultural production and reflected the zeitgeist. Unraveling the features influencing the Academy Awards offers insights into societal consciousness. Notably, age dynamics in actor and actress recognition hint at societal attitudes and power structures within award bodies. Exploring the significance of features like genre or box office in Oscar nominations raises critical questions about cultural prestige. Our machine learning-driven approach seeks to tackle these issues, shedding light on audience preferences and economic structures shaping the perceived artistic meritocracy of awards. In an era of concerns about technology misuse, our project showcases the constructive use of machine learning to diagnose cultural patterns, offering a pathway to progressive change.

Our machine learning approach aims to enhance the transparency of the Oscar nomination process. By employing algorithms to predict nominations across categories, we adopt a multi-label strategy, analyzing diverse factors contributing to a movie's likelihood of receiving recognition. This endeavor aligns with our broader goal of leveraging machine learning to gain deeper insights into the intricacies of the Oscar nomination landscape.

## Related Work

During our research, we encountered numerous articles that tried to predict Oscar winners, each embracing a different set of features and methodologies [GitHub Project](github_project), [Preferential ML](preferential_ml), [Social Network ML](social_network_ml). Our project diverges from the aforementioned works by focusing on predicting nominations rather than winners. By doing that, we will have more balanced dataset since only a few movie win Oscar, but more will be nominated.

## Method

### Resources

Our approach focuses on using a range of movie-related information, starting from the development stage to the final Oscar nomination announcements. We've identified key factors that we believe play a significant role in determining a movie's nomination prospects. These features include:

- Golden Globe nominations
- Screen Actors Guild (SAG) Nominations
- Release year and release month
- Movie genre (up to 3)
- Budget and revenue
- Movie run time
- Studio and production companies
- Age of actors, actresses, directors, and writers, and
- Ratings and number of votes on IMDb (Internet Movie Database)

The features are extracted by leveraging dataset sourced from reputable platforms like Kaggle and IMDb, which provide a comprehensive view of the movies, their performance metrics, and awards history. Specifically, the dataset we utilized include:

- The Movies Dataset [movies_dataset]
- IMDb datasets [imdb_datasets]
- Golden Globe nominations dataset [kaggle_golden_globes]
- Oscar nominations dataset [kaggle_oscars]
- SAG Award nominations dataset [kaggle_sag]

The goal is to identify the key features that contribute to a movie's likelihood of being nominated across the 13 major Oscar categories:

- Best Picture
- Actor in a Leading Role
- Actress in a Leading Role
- Cinematography
- Directing
- Film Editing
- Actor in a Supporting Role
- Actress in a Supporting Role
- Costume Design
- Visual Effects
- Animated Feature Film
- Production Design

It is worth to note that one movie can win multiple nominations, so rather than a multi-class classification (choosing one class amongst many), it is a multi-labelling problem (each class can either be chosen or not chosen).

### Train/Validation/Test Split

The dataset spans from 1927 to 2017, with movies from 2013 to 2017 isolated as the test set. The remaining data is divided into training and validation sets, as summarized in Table below:

| Data Split   | Years                    | Movie Count |
|--------------|--------------------------|-------------|
| Training     | 1927--2010 (inclusive)   | 33514       |
| Validation   | 2011--2012 (inclusive)   | 3395        |
| Test         | 2013--2017 (inclusive)   | 7912        |

Utilizing recent years for validation and test sets serves two key purposes. Firstly, it ensures the model is assessed on data that closely reflects the current landscape of the film industry. This is crucial for predicting nominations in the near future as industry trends and audience preferences evolve over time. Secondly, by training the model on historical data up to 2010 and validating and testing on subsequent years, we establish a robust evaluation framework. This approach simulates real-world scenarios where the model must generalize from past trends to make predictions for contemporary films. The focus on recent years enhances the model's adaptability to the dynamic nature of the film industry. This meticulous split strategy enables the model to learn from established patterns while fine-tuning its predictions to align with the ever-changing landscape of Oscar nominations.

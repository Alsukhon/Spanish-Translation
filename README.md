To view the project [click here!](https://github.com/Alsukhon/Spanish-Translation/blob/master/AB%20testing%20-%20Spanish%20translation.ipynb)

# Spanish-Translation
A/B Testing introduction for a Spanish Translation website

### The problem
An e-commerce website is looking into purchases of Spanish-speaking countries. They want to know whether implementing standardized Spanish translation versus localized translation -i.e, Mexican Spanish for Mexico- has any effect on sales.
Managers noticed that Spain-based users have a conversion rate higher than any other Spanish-speaking country. They suggested that one reason could be translation. All Spanish- speaking countries originally had the same translation of the site which was written by a translator from Spain.

### Proposed Solution
They agreed to try a test where each country would have its one translation written by a local (Argentinian users would see a translation written by an Argentinian, Mexican users by a Mexican, and so on), replicating what happened with Spanish users. As for users from Spain, they would have no change since their translation is already localized to Spanish.

##### A. Hypothesis
Including a localized Spanish translation for each country's dialect will increase conversions for Spanish-speaking countries other than Spain.

##### B. Metric
We will be using conversion as the metric to test our hypothesis. Conversion is defined as the number of customers who sign up for the company's website, given they have been exposed to the translation.

##### C. Experiment
Our goal from this experiment is to understand the effect of having local translation from each country on user conversion, which is done by randomly dividing visitors into equal groups for each country, and having one group (control group) exposed to the original Spanish translation, and the other (treatment group) exposed to a more localized Spanish translation. We want to measure conversion for each group after having been exposed to respective translations, and see whether having a localized translation results in a significant difference between conversions coming from users viewing the control version versus the treatment version.


## The Project

It is estimated that about 80,000 shoppers from Spanish-speaking countries visit the website daily, and the company would want enough time to negotiate contracts before the holiday season if the result turns out favorable towards local translations. Therefore, the experiment will run for 5 days to allow for a sizeable sample, which is from the 30th of November to December 4th, giving enough time for the company to act on findings before the holidays.
First, the conversion ratio will be explored for both groups in order to have an idea of the effects of localizing translations. Then, a two-tailed statistical t-test will determine whether statistically significant difference exists, and whether it is worth introducing to the website. The two-tailed test will be used because we do not know which translation is likely to perform better, and therefore can use testing in two directions.



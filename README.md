# pizzaparty

A while ago, a friend of mine called me to ask if there was any data sources to answer a pressing question:

## If you added together the gross floor area of all the Italian restaurants in the world, would they be able to cover the land area of Italy?

Initially, I thought we might never know. After some more thought, however, I realized we might be able to find at least a partial answer.

Thanks to graduate school, I had access to two large datasets:
1. Crowdsourced data used from a business review site for a handful of cities. This data obviously wasn't comprehensive, but it usefully tagged businesses by their type of cuisine.
2. A comprehensive dataset of US businesses, with fields for economic sector (NAICS codes), square footage, number of employees, etc. Federally defined economic sectors don't tell you anything about types of cuisine, so this dataset is unhelpful in its current state.

I realized if we brough these two datasets into conversation with one another, we could begin to answer our question with insights from the US. To do this, we used machine learning to understand the naming conventions of Italian restaurants within the first dataset, and applied lessons from that analysis to determine whether businesses in the second dataset were Italian or not.

Our method in detail:
- Select all restaurants and specialty food stores in dataset one.
- Mark each business Italian or Not Italian (based on the presence of an 'Italian' or 'Pizza' tag)
- Run an n-gram analysis on the names of the businesses to determine the letter combinations that best signal whether a business is Italian or Not Italian. (We use a sci-kit learn's LinearSVC classifier.)

- Select all businesses in dataset two with NAICS codes 44 (retail trade) and 72 (accommodation and food service)
- Assess the names of businesses in that selection, searching for letter combinations found to be significant in our n-gram analysis. Mark each business as Italian or Not Italian on that basis.
- Sum the square footage of the businesses marked 'Italian' and compare to that of Italy.


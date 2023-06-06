# Portfolio Project #1: U.S. Medical Insurance Costs

## insurance.csv
Source data file.

## medical_insurance_1.py
* A preliminary exploration using Python lists. The pandas and numpy libraries will be much more efficient, but they are not the focus of this exercise and will be reflected in future analyses instead. 
* This exploration seeks to examime the difference in medical costs between female and male participants, i.e., the question of interest is whether being a female means one needs to spend more or less in medical insurance, compared to the other sex.
* Preliminary findings:
	* When looking at non-smokers alone and removing the smoking factor, a factor that significantly impacts medical insurance cost, the average cost for a female is 8% higher than that of a male, contrary to the general average cost comparison where a male's insurance cost is 10% higher.
	* For non-smokers with children, the average cost for a female is still 13% higher than that of a male.
	* For non-smokers, for females, the specification of having children results in a 9% increase in insurance cost on average, whereas a male only sees 5% increase on average.
* Caveats and potential biases:
	* The findings are by no means causal. Even just within the scope of the source data, other variables included have impact on the insurance cost.
	* To examine the impact of sex variable alone and lessen the influence of other variables, some efforts were made to make the female samples and male samples more similar, e.g., only looking at non-smokers, checking if sample sizes and average ages are similar, and so on. That said, these simple measures are not rigorous enough, and the other variables are not sufficently controlled.
	* More sophisticated statistical analyses, such as regression analysis, will help quantify the relationships more accurately.

## us_medical_insurance_costs.ipynb
Presentation of more comprehensive version of the analysis. To be added later.
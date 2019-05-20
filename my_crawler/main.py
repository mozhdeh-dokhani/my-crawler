#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/04/12
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
from scrapy import cmdline
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
#Huffington
# cmdline.execute("scrapy crawl huffington_lifestyle -o huffington_lifestyle.csv -t csv".split()) #HuffingtonPost_Lifestyle
# cmdline.execute("scrapy crawl huffington_food -o huffington_food.csv -t csv".split()) #HuffingtonPost_Food
# cmdline.execute("scrapy crawl huffington_environment -o huffington_environment.csv -t csv".split()) #HuffingtonPost_Environment
# cmdline.execute("scrapy crawl huffington_health -o huffington_health.csv -t csv".split()) #HuffingtonPost_Health
# cmdline.execute("scrapy crawl huffington_parenting -o huffington_parenting.csv -t csv".split()) #HuffingtonPost_Parenting

#Guardian
# cmdline.execute("scrapy crawl guardian_food -o guardian_food.csv -t csv".split()) #Guardian_Food
cmdline.execute("scrapy crawl guardian_sport -o guardian_sport.csv -t csv".split()) #Guardian_Sport
# cmdline.execute("scrapy crawl guardian_health -o guardian_health.csv -t csv".split()) #Guardian_Health
# cmdline.execute("scrapy crawl guardian_lifestyle -o guardian_lifestyle.csv -t csv".split()) #Guardian_Lifestyle
# cmdline.execute("scrapy crawl guardian_science -o guardian_science.csv -t csv".split()) #Guardian_Science
# cmdline.execute("scrapy crawl guardian_technology -o guardian_technology.csv -t csv".split()) #Guardian_Technology
# cmdline.execute("scrapy crawl guardian_environment -o guardian_environment.csv -t csv".split()) #Guardian_Environment
# cmdline.execute("scrapy crawl guardian_wildlife -o guardian_wildlife.csv -t csv".split()) #Guardian_Wildlife

#CNBC
# cmdline.execute("scrapy crawl cnbc_food -o cnbc_food.csv -t csv".split()) #CNBC_Food
# cmdline.execute("scrapy crawl cnbc_technology -o cnbc_technology.csv -t csv".split()) #CNBC_Technology
# cmdline.execute("scrapy crawl cnbc_health -o cnbc_health.csv -t csv".split()) #CNBC_Health
# cmdline.execute("scrapy crawl cnbc_lifestyle -o cnbc_lifestyle.csv -t csv".split()) #CNBC_Lifestyle
# cmdline.execute("scrapy crawl cnbc_sport -o cnbc_sport.csv -t csv".split()) #CNBC_Sport
# cmdline.execute("scrapy crawl cnbc_science -o cnbc_science.csv -t csv".split()) #CNBC_Science
#---------------------------------------------------------------------------------
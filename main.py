import pydytuesday
import pandas as pd
import plotly.express as px
df = px.data.gapminder()


px.scatter(
    df, x="gdpPercap", y="lifeExp",
    animation_frame="year", animation_group="country",
    size="pop", color="continent", hover_name="country",
    facet_col="continent", log_x=True, size_max=45,
    range_x=[100,100000], range_y=[25,90]
)

px.area(
    df, x="year", y="pop",
    color="continent", line_group="country"
)

px.line(
    df, x="year", y="lifeExp",
    color="continent", line_group="country"
)


# pydytuesday.get_date('2026-09-29')

health = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-09-29/health.csv')

print(health.head())
print(health.shape)
print(health.columns)
health.info()

health = health.rename(columns={
        "GC_UCN_MAI_2025": "city",
    "GC_CNT_GAD_2025": "country",
    "GC_UCA_KM2_2025": "area_km2",
    "GC_POP_TOT_2025": "population",
    "GC_DEV_WIG_2025": "income_group",
    "HL_FCL_HOS_2024": "hospitals",
    "HL_FCL_PHA_2024": "pharmacies",
    "HL_FPC_HOS_2025": "hospitals_per_capita",
    "HL_FPC_PHA_2025": "pharmacies_per_capita",
})

usa = health[health["country"] == "United states"]
usa.head()
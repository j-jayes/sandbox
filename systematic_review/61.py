from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Union

class HistoricalLaborDisplacementStudy(BaseModel):
    """
    Schema for extracting data on historical labor displacement due to technology.
    """
    # Study Metadata
    authors: Optional[List[str]] = Field(None, description="List of authors' names.")
    title: Optional[str] = Field(None, description="Full title of the study.")
    year_of_publication: Optional[int] = Field(None, description="The year the study was published.")
    journal_or_publisher: Optional[str] = Field(None, description="Name of the journal or publication outlet (e.g., journal name, 'Working Paper', publisher).")

    # Inclusion
    include_in_extraction: bool = Field(..., description="Should this study be included in the extraction based on relevance? (True/False)")

    # Study Relevance (Only fill if include_in_extraction is True)
    topic: Optional[str] = Field(None, description="Brief description of the study's main topic related to technology and labor.")
    relevance_assessment: Optional[str] = Field(None, description="Brief justification for inclusion/exclusion based on the review's scope (historical, pre-1980 tech, empirical labor impact).")
    technologies: Optional[List[str]] = Field(None, description="Specific technologies or technological changes examined.")

    # Study Design Characteristics (Only fill if include_in_extraction is True)
    study_type: Optional[str] = Field(None, description="Type of study (e.g., Quantitative, Qualitative, Mixed-Methods).")
    methodology: Optional[str] = Field(None, description="Description of the research method used (e.g., historical analysis, econometric modeling, case study).")
    occupations: Optional[List[str]] = Field(None, description="Specific occupation(s) studied.")
    occupation_types: Optional[str] = Field(None, description="Type of occupation (e.g., Main, Supplementary, Seasonal).")
    occupation_classifications: Optional[List[str]] = Field(None, description="Occupational classification codes used, if any (e.g., HISCO, ISCO, PSTI).")
    gross_vs_net: Optional[str] = Field(None, description="Focus of displacement measurement (Gross, Net, Both).")
    sample_size: Optional[Union[int, str]] = Field(None, description="Number of workers/entities studied, or description if number not available.")
    sample_characteristics: Optional[str] = Field(None, description="Demographic or other characteristics of the sample (e.g., age, gender, location, industry).")
    time_period_covered: Optional[str] = Field(None, description="The historical timeframe covered by the study (e.g., '1880-1900', '19th Century').")
    time_period_start: Optional[int] = Field(None, description="Start year of the period covered.")
    time_period_end: Optional[int] = Field(None, description="End year of the period covered.")
    geographical_focus: Optional[str] = Field(None, description="Region, country, or specific location of the study.")

    # Key Variables of Interest (Only fill if include_in_extraction is True)
    independent_variables_technologies: Optional[str] = Field(None, description="Description of the independent variable(s) representing technology.")
    displaced_description: Optional[str] = Field(None, description="Qualitative description of worker displacement.")
    displaced_number: Optional[Union[float, str]] = Field(None, description="Number or share (%) of workers displaced.")
    unemployment_underemployment_description: Optional[str] = Field(None, description="Qualitative description of unemployment or underemployment following displacement.")
    unemployment_underemployment_number: Optional[Union[float, str]] = Field(None, description="Number or share (%) of workers unemployed/underemployed or exiting the labor market after displacement.")
    duration_of_unemployment: Optional[str] = Field(None, description="Reported duration of unemployment or underemployment after displacement.")
    wage_changes_description: Optional[str] = Field(None, description="Description of wage changes for displaced workers upon re-employment.")
    wage_changes_percent: Optional[Union[float, str]] = Field(None, description="Percentage change in wages for displaced workers (e.g., -10% or +5%).")

    # Quantitative Data (Fill if applicable and include_in_extraction is True)
    moderators: Optional[List[str]] = Field(None, description="Factors influencing the technology-employment relationship (e.g., education, industry, union presence).")
    effect_sizes: Optional[str] = Field(None, description="Reported effect sizes (e.g., 'Pearson's r=0.3', 'Cohen's d=0.5', 'OR=1.2').")
    statistical_measures: Optional[str] = Field(None, description="Other reported statistical measures (e.g., means, SDs, CIs, p-values, regression coefficients).")

    # Qualitative Data (Fill if applicable and include_in_extraction is True)
    key_themes: Optional[List[str]] = Field(None, description="Major qualitative themes identified related to labor displacement.")
    text_fragments: Optional[List[str]] = Field(None, description="Relevant direct quotes or text fragments illustrating displacement impacts.")

    # Historical Context (Only fill if include_in_extraction is True)
    narrative_descriptions: Optional[str] = Field(None, description="Summary of qualitative/narrative accounts of displacement processes and impacts.")
    technological_changes_context: Optional[str] = Field(None, description="Contextual details about the specific technological advancements studied.")
    economic_conditions: Optional[str] = Field(None, description="Broader economic conditions during the study period (e.g., growth, recession, industrialization phase).")
    institutional_context: Optional[str] = Field(None, description="Relevant labor policies, regulations, or labor relations context.")

    # Outcomes and Conclusions (Only fill if include_in_extraction is True)
    main_findings: Optional[str] = Field(None, description="Summary of the study's main findings regarding labor displacement.")
    conclusions: Optional[str] = Field(None, description="The study's overall conclusions on the effects of technology on employment.")

    # Quality Assessment (Only fill if include_in_extraction is True)
    methodological_limitations: Optional[str] = Field(None, description="Limitations of the study methodology as reported by the authors or assessed by the extractor.")
    coherence_assessment: Optional[str] = Field(None, description="Assessment of how coherent the findings are (e.g., fit between methods and findings).")
    adequacy_assessment: Optional[str] = Field(None, description="Assessment of whether the data are rich and sufficient to support the findings.")
    relevance_assessment_quality: Optional[str] = Field(None, description="Assessment of the extent to which the findings are relevant to the review's research questions.")

# --- Extracted Data ---

study_data = HistoricalLaborDisplacementStudy(
    # Study Metadata
    authors=["Moses S. Musoke"], # [cite: 1]
    title="Mechanizing Cotton Production in the American South: The Tractor, 1915-1960", # [cite: 1]
    year_of_publication=1981, # [cite: 1]
    journal_or_publisher="Explorations in Economic History", # [cite: 1]

    # Inclusion
    include_in_extraction=True, # Based on analysis below

    # Study Relevance
    topic="Diffusion of the tractor in Southern cotton production and its economic impact, focusing on the profitability of adoption compared to mule power and the resulting effects on farm structure and labor arrangements, particularly the decline of sharecropping.", # [cite: 33, 102]
    relevance_assessment="Yes. The study empirically analyzes the adoption and impact of the farm tractor (a pre-1980 technology) on US Southern cotton agriculture between 1915 and 1960[cite: 1]. It examines the economic drivers of mechanization and explicitly discusses labor impacts, including changes in labor utilization and the significant displacement of sharecroppers[cite: 32, 33, 34, 238, 239]. This aligns with the review's focus on empirical labor market effects of historical technology.",
    technologies=["Tractor (specifically the general-purpose tractor) [cite: 84, 85]", "Multirow equipment [cite: 87, 88]", "Cotton picker [cite: 13, 35, 361]", "Flame cultivators [cite: 361]", "Herbicides [cite: 361]"],

    # Study Design Characteristics
    study_type="Quantitative", # Based primarily on cost-benefit analysis [cite: 107, 108] and analysis of aggregate quantitative data[cite: 224, 285, 288], though includes historical narrative.
    methodology="Historical analysis comparing the costs and profitability of tractor versus mule power in cotton production using data from agricultural experiment stations, USDA reports, and censuses[cite: 102, 107, 128, 217, 281]. Analysis includes calculation of cost savings per acre for representative farm sizes across different regions and time periods[cite: 108, 137, 193, 195]. Also analyzes aggregate census data on tractor adoption rates, farm sizes, and sharecropping trends[cite: 218, 224, 281, 288].",
    occupations=["Cotton farmers (smallholders, large farmers/planters) [cite: 138, 139, 268, 269, 325]", "Sharecroppers [cite: 32, 33, 238, 307]", "Farm laborers (including hired labor, family labor, tractor operators, animal service labor) [cite: 325, 393, 396]"],
    occupation_types="Main agricultural occupations.", # Implied
    occupation_classifications=["Omitted in source."],
    gross_vs_net="Focus on factors driving adoption (profitability) and resulting structural changes (decline in sharecropping, farm consolidation), implying net effects on labor structure.", # Inferred from focus on sharecropper decline [cite: 32, 33, 239] and farm structure changes[cite: 389].
    sample_size="Analysis uses aggregate data (state/regional level tractor numbers, farm counts, acreage from US Census of Agriculture and USDA statistics) [cite: 218, 225, 289, 461] and representative farm models (15 and 30 cotton acres) for cost calculations based on various agricultural studies and reports[cite: 128, 137, 138, 139, 140].",
    sample_characteristics="Focuses on cotton farms in the American South, with specific analysis for subregions: Yazoo-Mississippi Delta (Mississippi), South Carolina Piedmont (South Carolina), and Texas High Plains (Texas)[cite: 1, 45, 128, 129, 130]. Distinguishes farms by size (e.g., <30 acres vs. >=30 acres of cotton or cropland) [cite: 137, 268, 281] and tenure status (owner, tenant, sharecropper)[cite: 306, 307].",
    time_period_covered="1915-1960 [cite: 1] (Core analysis and cost data often focus on 1930-1959 [cite: 194, 196, 224])",
    time_period_start=1915, # [cite: 1]
    time_period_end=1960, # [cite: 1]
    geographical_focus="American South (specifically the ten leading cotton states defined as AL, AR, GA, LA, MS, NC, SC, OK, TN, TX)[cite: 1, 45]. Detailed subregional analysis of Yazoo-Mississippi Delta (MS), South Carolina Piedmont (SC), and Texas High Plains (TX)[cite: 128].",

    # Key Variables of Interest
    independent_variables_technologies="Adoption of tractor power versus traditional mule/workstock power, assessed primarily through comparative cost analysis (profitability threshold calculation). [cite: 102, 107, 108, 110]",
    displaced_description="Mechanization via tractors, often implemented by landlords/planters and sometimes encouraged by federal programs, led to the displacement of sharecroppers[cite: 238]. This involved consolidating tenant plots, dismissing sharecroppers, converting them to wage laborers, or revising contracts downwards[cite: 308].",
    displaced_number="Sharecropper farms in the South declined by over 33% during the 1930s and by over 91% between 1930 and 1960[cite: 239].",
    unemployment_underemployment_description="Displaced sharecroppers were either converted to wage labor on the farm or 'set adrift to fend for themselves elsewhere'[cite: 308]. Mentions accelerated migration to urban centers and outside of agriculture due to broader economic forces (higher wages, non-farm opportunities) concurrent with mechanization[cite: 212].",
    unemployment_underemployment_number="Omitted in source.", # Does not quantify unemployment/labor exit rates specifically for those displaced by tractors.
    duration_of_unemployment="Omitted in source.",
    wage_changes_description="Omitted in source.", # Discusses prevailing wage rates as a *cause* of mechanization [cite: 209] and the impact of using low-cost family labor versus hired labor on adoption decisions[cite: 325, 338], but not the wage outcomes for displaced workers upon re-employment.
    wage_changes_percent="Omitted in source.",

    # Quantitative Data
    moderators=[
        "Farm size (larger farms adopted earlier/more readily) [cite: 254, 265, 303]",
        "Geographical region (e.g., flatter terrain, larger farms in Texas favoured adoption) [cite: 133, 136, 303]",
        "Availability and cost of credit (lack of access/higher rates hindered small farmers) [cite: 326, 330, 331]",
        "Land tenure (planters could mechanize sharecropped land) [cite: 307, 308]",
        "Relative factor prices (rising wages/feed costs vs. machinery/fuel costs) [cite: 205-209, 353]",
        "Federal farm programs (price supports, acreage reduction, subsidized credit) [cite: 237, 238]",
        "Availability of complementary technologies (e.g., multirow equipment, pickers) [cite: 361, 362]",
        "Technical improvements in tractors (reliability, suitability for tasks, smaller models) [cite: 85, 188, 358, 360]",
        "Availability of repair services [cite: 52, 340]",
        "Cultural practices (e.g., shift from terracing to strip farming) [cite: 368]"
        ],
    effect_sizes="Omitted in source.", # Provides cost savings ($/acre) [cite: 194, 196] but no standardized statistical effect sizes linking tractor adoption to displacement.
    statistical_measures="Calculation of annual cost savings ($/acre) for tractor vs. mule power for different farm sizes and regions [cite: 194, 196, Table 2, Table 3]. Data on total fixed and variable costs [cite: 403, Table 7]. Number of tractors and percentage change over time by state [cite: 224, Table 4]. Ratios related to farm size distribution and tractor adoption (UFR, TFR, ATFR) [cite: 288, Table 6]. Data on tractor distribution by farm size for 1944 [cite: 285, Table 5]. Percentage decline in sharecropper farms[cite: 239]. Uses interest rates (e.g., 5%) [cite: 173] and depreciation rates[cite: 126, 394]. Input quantities (hours/acre, fuel/hour)[cite: 395, 406].",

    # Qualitative Data
    key_themes=[
        "Economic rationality and profitability threshold in technology adoption.",
        "Impact of farm scale and structure on diffusion pace.",
        "Role of changing factor prices (esp. labor) driving mechanization.",
        "Mechanization leading to displacement of traditional labor (sharecropping).",
        "Influence of institutions (federal programs, credit markets) on adoption.",
        "Co-evolution of technology (tractors and implements) and farming practices."
        ],
    text_fragments=[
        "Sharecropping, upon which much of postbellum cotton production was based, was literally wiped out; sharecroppers' farms declined by more than 90% between 1930 and 1959." ,# [cite: 32, 33]
        "Consequently some landlords bought tractors and dispensed with sharecroppers or revised share contracts to their benefit." ,# [cite: 238]
        "...the planter could, and in many instances did, combine sharecropper units and 'demoted' their previous operators to wage labor or set them adrift to fend for themselves elsewhere." ,# [cite: 308]
        "Small farmers who relied mostly on low-priced family labor were probably better off with the mule rather than the tractor process." ,# [cite: 338]
        "The paradox of increasing capital substitution and the displacement of labor when the latter was superabundant is explicable by the fact that some of the factors affecting the cost and revenue curves faced by some farmers are not captured in our estimates. For instance, federal farm programs involving price supports, acreage reductions, benefit payments and subsidized credit favored mechanization." # [cite: 236, 237]
        ],

    # Historical Context
    narrative_descriptions="The paper details the initial lag in Southern cotton mechanization compared to Northern grains due to technology limitations [cite: 2-9, 82]. It describes the arrival of the general-purpose tractor in the mid-1920s [cite: 84, 85] and the subsequent, though gradual, diffusion, influenced by the Depression and then accelerated by WWII and post-war conditions [cite: 99, 210-213, 232, 375, 377]. It narrates how profitability calculations shifted in favor of tractors, especially on larger farms and in regions like Texas [cite: 199-202, 303]. The narrative connects tractor adoption by landlords to the dramatic decline of the sharecropping system[cite: 32, 33, 238, 239]. It also covers the westward shift of cotton production facilitated by mechanization[cite: 73, 78, 79].",
    technological_changes_context="The key technology was the general-purpose tractor (mid-1920s), which was lighter, more mobile, and suitable for row-crop cultivation compared to earlier 'standard' tractors[cite: 83, 84, 85]. Subsequent improvements enhanced reliability and operator comfort[cite: 188]. The development of smaller, reliable tractors in the 1940s-50s expanded access to smaller farms[cite: 360]. The tractor's utility increased with the availability of complementary implements like multi-row equipment, mechanical choppers, flame cultivators, herbicides, and mechanical cotton pickers, forming a 'mechanization complex'[cite: 87, 361, 362].",
    economic_conditions="The study spans the period 1915-1960, covering post-WWI adjustments, the agricultural difficulties of the 1920s, the Great Depression (which slowed adoption)[cite: 232, 376], WWII (which created labor shortages and increased farm income, boosting demand for mechanization)[cite: 210, 347, 348], and the post-WWII era characterized by rising wages, non-farm opportunities, and continued mechanization[cite: 212, 352]. Federal farm programs (price supports, acreage controls) were implemented from the 1930s onwards[cite: 237].",
    institutional_context="The predominant pre-mechanization labor institution in cotton was sharecropping[cite: 32]. The study analyzes how tractor adoption, particularly by landowners, disrupted this system, leading to sharecropper displacement[cite: 33, 238, 308]. Federal farm programs influenced landlord decisions regarding mechanization and tenant relations[cite: 237, 238]. Differential access to credit based on farm size/status affected adoption capacity[cite: 326, 330]. The emergence of custom rental markets for tractors and harvesting equipment is noted[cite: 48, 53, 302].",

    # Outcomes and Conclusions
    main_findings="Tractor adoption in the Cotton South was primarily driven by economic profitability compared to mule power, with the threshold farm size for profitable adoption decreasing significantly over time, especially after WWII due to rising labor/feed costs relative to machinery/fuel costs [cite: 199-202, 205-209, 353]. Diffusion was significantly faster on larger farms and in regions like Texas with favorable farm structures[cite: 254, 303, 304]. Tractorization was a major factor contributing to the sharp decline in sharecropping, as landowners mechanized operations[cite: 32, 33, 238, 239]. Technological improvements in tractors and complementary equipment further accelerated adoption.",
    conclusions="The mechanization of Southern cotton farming via the tractor, while delayed compared to the North, followed rational economic patterns driven by relative factor costs and technological availability, rather than being solely determined by unique Southern social institutions[cite: 371, 373]. The tractor fundamentally reshaped Southern agriculture, compelling farm reorganization, increasing capital intensity, enabling scale economies, contributing to the decline of small farms and sharecropping, and facilitating the geographical shift of cotton production[cite: 387, 388, 389, 391].",

    # Quality Assessment
    methodological_limitations="Author notes reliance on average price data (state/national) may not reflect individual farm circumstances[cite: 167, 168]; difficulty in choosing the appropriate interest rate[cite: 170]; use of fixed input weights over time[cite: 183, 184]; assumption of yield neutrality[cite: 113]; cost savings calculations may not capture all decision factors like risk perception[cite: 322]; data availability constraints (e.g., county data pre-1945[cite: 247], cotton acreage by farm size only for 1944 [cite: 292]).",
    coherence_assessment="High. The quantitative findings on cost-profitability thresholds and adoption rates align logically with the historical narrative regarding factor price changes, technological developments, farm structure, and the decline of sharecropping. Arguments are well-supported by the presented data.",
    adequacy_assessment="High. The study draws on a substantial amount of quantitative data from censuses, USDA reports, and specific agricultural studies covering costs, inputs, tractor numbers, and farm structures over several decades [cite: 128, 149, 218, 225, 285, 289, 400-413]. The data appear sufficiently rich and detailed to support the main arguments regarding the economics of tractor adoption and its consequences.",
    relevance_assessment_quality="High. The study directly addresses the review's research questions by providing a detailed empirical analysis of the economic drivers and labor market consequences (specifically sharecropper displacement) of a major pre-1980 technological shift (tractorization) in a relevant historical context (US South cotton agriculture)."
)

# Output the structured data (as a Python dictionary for clarity)
print(study_data.dict())
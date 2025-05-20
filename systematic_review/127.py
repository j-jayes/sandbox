HistoricalLaborDisplacementStudy(
    # Study Metadata
    authors=["R. Clyde White"][cite: 1],
    title="Technological Unemployment"[cite: 1],
    year_of_publication=1931[cite: 1],
    journal_or_publisher="Social Forces"[cite: 1],

    # Inclusion
    include_in_extraction=True, # Based on relevance assessment below

    # Study Relevance (Only fill if include_in_extraction is True)
    topic="Analysis of the concept and extent of technological unemployment in the United States, challenging fears of a perpetually rising trend by examining historical examples, census data (1870-1920), contemporary studies, and limited firm-level data." [cite: 9, 13, 17, 44, 100-101, 158, 129-142],
    relevance_assessment="Yes. The study empirically examines historical (pre-1931) technological change (e.g., glass industry machinery, clothing cutters, streetcars, general industrial machinery, historical examples like textile machinery/cotton gin) and its impact on employment/unemployment using historical analysis, census data (1870-1920), firm-level data, and cited studies, thus fitting the review scope (historical, pre-1980 tech, empirical labor impact)." [cite: 1, 6, 9-11, 26-32, 76-98, 129-142, 151-180],
    technologies=[
        "Labor-saving machinery (general)"[cite: 6],
        "Glass bottle machinery"[cite: 10, 77],
        "Window glass machinery"[cite: 10],
        "Electric light bulb machinery"[cite: 10],
        "One-man streetcars"[cite: 11, 142],
        "Textile machinery (historical)"[cite: 27],
        "Steam power (historical)"[cite: 28],
        "Cotton gin (historical)"[cite: 30],
        "Clothing cutting technology (implied in cited study)"[cite: 87],
        "General industrial machinery (Indianapolis firms)",
        "Administrative reorganization/efficiency measures" [cite: 7, 9]
    ],

    # Study Design Characteristics (Only fill if include_in_extraction is True)
    study_type="Mixed-Methods (Primarily narrative/analytical review using historical examples, census data, firm-level data, and cited quantitative studies)" [cite: 9, 13, 75-98, 129-142, 151-180],
    methodology="Historical analysis, literature review (discusses Clague, Chase, Barnett, Myers, Douglas), secondary data analysis (US Census 1870-1920), presentation of primary/secondary firm-level data (5 Indianapolis firms), theoretical argumentation.",
    occupations=[
        "Glass bottle blowers"[cite: 78],
        "Clothing cutters"[cite: 87],
        "Streetcar motormen/conductors"[cite: 11, 142],
        "Textile workers (historical)"[cite: 27],
        "Cotton gin operators (historical, implied)"[cite: 30],
        "General factory workers"[cite: 61, 66],
        "Agricultural workers"[cite: 70, 169],
        "Railroad workers"[cite: 70],
        "Miners"[cite: 70, 169],
        "Slaughtering/packing workers",
        "Petroleum refining workers"[cite: 120, 123],
        "Occupations in US Census categories: Agriculture, Professional, Domestic/Personal Service, Trade/Transportation, Manufacturing/Mining/Mechanical" [cite: 169]
    ],
    occupation_types="Omitted in source", # Source doesn't classify studied occupations this way.
    occupation_classifications="Omitted in source", # Uses broad US Census categories[cite: 169], no specific codes mentioned.
    gross_vs_net="Focuses on Net displacement/reabsorption, arguing against permanent unemployment, while acknowledging Gross displacement in examples." [cite: 78, 87, 100-101, 104, 155, 173-175, 181],
    sample_size="Multiple datasets used: US Population > 10 years (Census data 1870-1920), 370 clothing cutters (cited study)[cite: 87], Glass Bottle Blowers Assoc. members (9,627 down to 6,321) (cited study/data)[cite: 78], 5 Indianapolis firms[cite: 132].",
    sample_characteristics="US Population (by sex, age >10, child labor 10-15) [cite: 152, 160, 178-180]; Skilled male clothing cutters[cite: 87, 101]; Skilled male glass bottle blowers[cite: 78]; Workers in 5 Indianapolis firms (unspecified, includes street railway)[cite: 132, 142]; Broad occupational groups from US Census[cite: 169]. Primarily US-focused[cite: 13].",
    time_period_covered="Late 18th Century - 1930, with detailed data mainly from 1870-1929."[cite: 1, 26, 78, 101, 132, 156, 187],
    time_period_start=1870, # Start of detailed census data used [cite: 156]
    time_period_end=1930, # Publication year and discussion context [cite: 1, 187]
    geographical_focus="United States"[cite: 13, 151], with specific examples/data from Indianapolis [cite: 129] and mentions of Detroit[cite: 56]. Cites Australian data for comparison[cite: 110].

    # Key Variables of Interest (Only fill if include_in_extraction is True)
    independent_variables_technologies="Introduction of labor-saving machinery[cite: 6], specific machines[cite: 10, 11, 27, 30], administrative reorganization for efficiency[cite: 7, 9]. Measured implicitly or through examples/case studies. Rising productivity per employee implies tech adoption in Indianapolis study[cite: 132].",
    displaced_description="Workers are 'thrown out of work'[cite: 15], jobs 'taken by a machine'[cite: 84], 'let out' of industry[cite: 87], 'laid off'[cite: 57, 66, 103]. The essential characteristic is a 'shift in occupations'[cite: 104]. Some may have to take less skilled/remunerative jobs[cite: 83].",
    displaced_number="Glass Bottle Blowers Assoc. members decreased by 3,306 (from 9,627 to 6,321) over 10 years (~34% decrease)[cite: 78]. 370 clothing cutters studied post-displacement (cited study)[cite: 87]. Cites Clague: ~1 million fewer manufacturing workers (1920-1929)[cite: 61]. Cites Chase: ~1.675 million fewer workers in agric./manuf./rail/mining (1919-1925) [cite: 70] (Author disputes interpretation of Clague/Chase figures as purely technological displacement [cite: 70-71, 74]).",
    unemployment_underemployment_description="Displaced workers experience a time lag before reabsorption[cite: 55, 181]. Some take 'poorer jobs' [cite: 94] or less skilled/remunerative work[cite: 83]. Unemployment is seen as temporary, involving a 'transfer of labor'.",
    unemployment_underemployment_number="Myers' study (cited): 11.4% of 370 displaced cutters were still unemployed >=1.5 years later[cite: 93]. ~40% had poorer jobs or none[cite: 94].",
    duration_of_unemployment="Myers' study (cited) of 240 cutters: 28.7% lost no time; 30.1% lost 1-3 mo; 12.9% lost 4-6 mo; 9.6% lost 6-9 mo; 5.8% lost 10-12 mo; 12.9% lost >1 yr. Weighted average time lost: 5.2 months (noted as potentially inflated)[cite: 96].",
    wage_changes_description="Some displaced workers might take 'less remunerative jobs'[cite: 83]. Myers' study (cited): ~40% of cutters got 'poorer jobs'; ~35% jobs 'approximately as good'; ~25% 'better jobs'[cite: 94].",
    wage_changes_percent="Omitted in source",

    # Quantitative Data (Fill if applicable and include_in_extraction is True)
    moderators="Omitted in source", # Dismissal wage mentioned affecting job search[cite: 95], but no systematic analysis of moderators.
    effect_sizes="Omitted in source",
    statistical_measures="Correlation coefficient (r=0.896 +/- 0.024) between production and employment indexes (5 Indianapolis firms)[cite: 141]. Percentages used for census data[cite: 152, 169, 178], Myers' study results. Index numbers used for productivity and employment (Indianapolis study, Australia, specific industries) [cite: 110-114, 120-123, 132]. Weighted average time lost reported[cite: 96].",

    # Qualitative Data (Fill if applicable and include_in_extraction is True)
    key_themes=[
        "Technological unemployment is historical, not new.",
        "Fears of permanent, rising technological unemployment are likely exaggerated." [cite: 14, 44, 100-101],
        "Technology causes occupational shifts and temporary unemployment, not permanent job loss overall."[cite: 101, 104, 181],
        "Productivity increases do not automatically equal unemployment." [cite: 106, 117-119, 183],
        "Service/distribution sectors absorb labor displaced from production sectors." [cite: 53-54, 74, 102, 155, 175],
        "Overall employment relative to population showed an upward trend (1870-1920)." [cite: 160-161, 184],
        "Child labor law changes affected employment statistics." [cite: 177-180, 186]
        ],
    text_fragments=[
        "Technological unemployment is that form of unemployment which results from the introduction of labor-saving machinery."[cite: 6],
        "Its essential characteristic is the shift in occupations, not a relative reduction in the total number of occupations."[cite: 104],
        "He [Douglas] concludes that the 'net result of these technological improvements is not permanent unemployment... but rather a transfer of labor from some lines to others' and that it is 'clear that permanent technological unemployment is impossible.'",
        "...the percentage of the population above ten years of age which is gainfully employed has a slight upward trend between 1870 and 1920" [cite: 184]
    ],

    # Historical Context (Only fill if include_in_extraction is True)
    narrative_descriptions="Describes historical examples like the Industrial Revolution's impact on handicraft workersand the effect of the cotton gin. Details the experience of glass bottle blowers displaced by machinesand clothing cutters' re-employment process (citing Myers). Discusses labor shifts from production to service/distribution sectors [cite: 53-54, 64, 66, 74, 102, 175].",
    technological_changes_context="Notes acceleration of invention via professional inventors. Gives specific output multipliers (e.g., glass bottles 41x faster)[cite: 10]. Describes one-man streetcars[cite: 11, 142]. Contextualizes early inventions and the Industrial Revolution [cite: 22-23, 26-29].",
    economic_conditions="Uses AT&T business cycle index to contextualize census employment data [cite: 153, 159, 162-163]. Notes potential impact of post-WWI adjustments/1921 depression on early 1920s data. Mentions 1930 census timing during a 'serious depression'[cite: 187]. General context of industrialization, rising productivity, and discussion of scale of living relative to population growth [cite: 43, 68, 106-108, 143].",
    institutional_context="Mentions Glass Bottle Blowers Association union's response to technology[cite: 78, 80]. Notes AFL's advocacy for shorter hours[cite: 59]. Highlights impact of child labor/compulsory school laws [cite: 178-180, 186]. Mentions 'dismissal wage'[cite: 95]. Suggests employment exchanges/personnel management as solutions[cite: 105].",

    # Outcomes and Conclusions (Only fill if include_in_extraction is True)
    main_findings="Technological change causes temporary unemployment and occupational shifts, not permanent job loss[cite: 104, 181]. Historical data (1870-1920) shows upward trend in employment rates relative to population [cite: 160-161, 184]. Displaced labor tends to shift to service/distribution sectors [cite: 53-54, 74, 102, 175]. Rising productivity doesn't automatically mean rising unemployment[cite: 117, 183]. Studies limited to declining sectors are misleading [cite: 51, 53, 175-176].",
    conclusions="Fears of permanent technological unemployment are likely overstated [cite: 44, 100-101]. The main effect is occupational readjustment[cite: 101, 104, 181]. Solutions should aid transition (e.g., employment exchanges)[cite: 105]. Interpreting data requires considering all sectors and economic context [cite: 51-53, 175-176, 182, 187].",

    # Quality Assessment (Only fill if include_in_extraction is True)
    methodological_limitations="Author acknowledges lack of comprehensive, current data for all sectors (esp. services) between censuses[cite: 53, 145]. Indianapolis firm data (n=5) may not be representative. Census date changes create comparability issues (seasonal effects). Cited studies have limits (e.g., Myers' time-lost potentially inflated; Australian productivity index issues). Paper is primarily interpretive using secondary data.",
    coherence_assessment="The argument (displacement leads to shifts, not permanent unemployment) is coherent and consistently supported by historical examples, census analysis, and cited studies. Different data sources are integrated to back the central thesis.",
    adequacy_assessment="Data (census 1870-1920, Myers' study details) adequately supports claims for the specific periods/groups covered. Acknowledged lack of comprehensive data for the 1920s, especially growing sectors, limits conclusions about the *then-current* situation [cite: 53, 156-158]. Indianapolis data is very limited[cite: 132].",
    relevance_assessment_quality="Highly relevant. Directly addresses historical (pre-1980) technological unemployment using empirical data (census, cited studies, firm data), discusses displacement, unemployment duration, occupational shifts, specific technologies, and occupations, aligning well with the review's research questions."
)
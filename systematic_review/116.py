# Extracted Data from Myers (1929)
study_data = HistoricalLaborDisplacementStudy(
    # Study Metadata
    authors=["Robert J. Myers"][cite: 1],
    title="Occupational Readjustment of Displaced Skilled Workmen"[cite: 1],
    year_of_publication=1929[cite: 1],
    journal_or_publisher="Journal of Political Economy"[cite: 1],

    # Inclusion
    include_in_extraction=True, # Based on relevance assessment below

    # Study Relevance
    topic="Occupational outcomes and readjustment experiences of skilled men's clothing cutters displaced from their trade in Chicago due to changes in production methods and market conditions in the 1920s"[cite: 5, 6],
    relevance_assessment="Yes. The study empirically examines the labor market consequences (subsequent occupations, unemployment duration, earnings changes) for workers displaced by pre-1980 technological/production changes (shift to 'factory system' in clothing manufacture, 1921-1926)[cite: 5, 25, 31, 40]. It focuses on concrete impacts, not just sentiment.",
    technologies=["Changes in production methods ('factory system') involving reorganization of work"[cite: 31], "Increased relative use of machine work and less hand labor"[cite: 25], "Abrogation of strict rules as to the use of machinery and methods already in service"[cite: 33]. Note: Emphasizes it did *not* involve significant *new* machinery introduction [cite: 31, 32]],

    # Study Design Characteristics
    study_type="Quantitative (primarily, based on analysis of survey/interview data presented statistically), with qualitative descriptions"[cite: 66, 73, 88, 95, 97, 99, 137, 140, 142, 148, 150, 152, 192, 201],
    methodology="Historical analysis using data collected via questionnaires sent to workers (n=82), personal interviews with workers, families, or friends (n~200), and information from employers, union officials, and fellow-workmen (n<100)[cite: 13, 55, 56, 57]. Compares outcomes for workers displaced through firm dissolution/relocation versus those accepting a dismissal wage[cite: 39, 105, 110].",
    occupations=["Cutters (primarily) and some Trimmers in the men's clothing industry" [cite: 6, 27, 58]],
    occupation_types="Skilled workmen[cite: 5, 28], Main occupation",
    occupation_classifications=["Omitted in source"],
    gross_vs_net="Gross (focuses on the outcomes of the individuals displaced from their original trade)",
    sample_size="370 ex-cutters studied in total[cite: 6, 40]. Sub-sample sizes vary for specific analyses (e.g., 241 for trades worked[cite: 73], 240 for time lost[cite: 88], 276 for earnings comparison[cite: 95], 198 for age analysis [cite: 192]).",
    sample_characteristics="Skilled male workers in Chicago's men's clothing industry, mostly union members[cite: 6, 9, 28]. Displaced between 1921-1926[cite: 40]. Included workers displaced by firm dissolution/relocation and 236 workers from Hart, Schaffner and Marx who received a $500 dismissal wage[cite: 36, 37, 105, 106]. Some analysis by ageand brief mention of ethnicity (Jewish workers noted as more successful in re-employment)[cite: 127].",
    time_period_covered="Displacement occurred 1921-1926[cite: 40]; outcomes assessed as of early summer 1928[cite: 44]. Overall period: 1921-1928.",
    time_period_start=1921[cite: 40],
    time_period_end=1928[cite: 44], # Year outcomes were assessed
    geographical_focus="Chicago"[cite: 6],

    # Key Variables of Interest
    independent_variables_technologies="Displacement from the cutting trade resulting from industry changes (shift to cheaper clothing production, adoption of 'factory system' methods)[cite: 25, 31, 42], firm closures/relocations[cite: 36, 37], or acceptance of a dismissal wage[cite: 105]. Age is analyzed as a predictor of readjustment success[cite: 174]. Receipt of dismissal wage is used as a comparison variable[cite: 110].",
    displaced_description="Skilled cutters (and some trimmers) forced out of the men's clothing trade due to industry depression hitting high-quality market[cite: 19, 20], a shift towards cheaper clothing production ('factory system') requiring less hand skill and different work organization[cite: 25, 31, 33], subsequent firm liquidations or relocations[cite: 37], or participation in a negotiated dismissal wage scheme[cite: 105, 106].",
    displaced_number="370 individuals studied[cite: 40]. This group was part of a larger pool of unemployed cutters in Chicago, potentially numbering 5,000 by 1926[cite: 21].",
    unemployment_underemployment_description="A significant period of unemployment was common between leaving cutting and securing a new regular job[cite: 89, 90]. Many workers changed trades multiple times, indicating instability[cite: 77, 78]. By 1928, a portion remained unemployed, ill, or retired[cite: 66]. Some held only temporary cutting jobs, hard to distinguish from unemployment[cite: 48].",
    unemployment_underemployment_number="As of 1928: 11.4% (42 men) were 'Not employed' (includes 8 dead, 5 retired, 3 ill/unemployable, 26 unemployed seeking work)[cite: 66]. Thus, 7.0% (26 men) were actively unemployed and seeking work[cite: 66]. 71.3% of men lost some time between leaving cutting and finding their first regular job[cite: 89].",
    duration_of_unemployment="Average time lost between leaving cutting and securing the first regular employment was 5.2 months[cite: 90]. About one-third (33.3%) lost six months or more [calculated from Table III: cite 88, 90].",
    wage_changes_description="Compared earnings in 1928 to previous earnings as cutters. A larger proportion earned less than earned more[cite: 91, 95]. Outcomes varied widely, with some finding better-paying jobs (e.g., successful salesmen/agents, other skilled trades like milk-wagon drivers) and others ending in 'miserably low wages' (e.g., caretakers, laborers, some factory work)[cite: 54, 61, 65, 69].",
    wage_changes_percent="Relative comparison: 46.4% earned less, 30.4% earned more, and 23.2% earned the same in 1928 compared to their earnings as cutters[cite: 95]. (Note: This is the distribution of workers, not the average percentage change in wages).",

    # Quantitative Data
    moderators=["Age (workers aged 35-39 showed greatest success in readjustment) [cite: 178, 189, 206]", "Receipt of dismissal wage (showed slight, possibly negligible, positive effect) [cite: 153, 199]", "Volunteer status vs. conscripted (volunteers fared better than conscripts among dismissal wage group)", "Ethnicity (Jewish workers mentioned anecdotally as more successful) [cite: 127]"],
    effect_sizes="Omitted in source (presents counts, percentages, averages)",
    statistical_measures="Counts and percentages in tables[cite: 66, 73, 88, 95, 97, 99, 137, 140, 142, 148, 150, 152, 192, 201]. Averages (mean time lost before re-employment[cite: 90], average number of trades worked [cite: 201]).",

    # Qualitative Data
    key_themes=["Significant hardship and cost borne by displaced skilled workers", "Difficulties in occupational readjustment, including long unemployment spells and job instability", "Frequent downward occupational and earnings mobility", "Persistence of desire to return to the original skilled trade", "Limited effectiveness of an early dismissal wage program in mitigating negative impacts", "Importance of age in influencing readjustment success"],
    text_fragments=[
        "changes in the industry have been made at a heavy cost to the men forced out."[cite: 100],
        "a substantial proportion, whether because of age, lack of initiative, inadaptability, or unfavorable circumstances, have drifted into jobs decidedly inferior to cutting."[cite: 161],
        "Probably a majority are less satisfied than at their old cutting jobs."[cite: 162],
        "The average time lost was five and two-tenths months."[cite: 90],
        "the number earning less in 1928 than they had earned as cutters was half again as large as the number earning more"[cite: 91],
        "over three-fifths of the men stating their wishes had either already returned to cutting men's clothing or wished to get back if they could get regular jobs" [cite: 91]
    ],

    # Historical Context
    narrative_descriptions="The study describes how the post-WWI depression [cite: 14] led Chicago's men's clothing industry to shift towards cheaper products[cite: 19, 24], implementing a 'factory system' that displaced skilled cutters[cite: 25, 31]. It details the subsequent experiences of 370 displaced cutters, tracking their diverse new occupations (ranging from professional/business to unskilled labor)[cite: 51, 52, 54, 60, 65, 66, 69], the frequency of job changes[cite: 77, 78], unemployment spells[cite: 88, 90], and earnings adjustments[cite: 95]. It also recounts the specific Hart, Schaffner & Marx dismissal wage experiment.",
    technological_changes_context="The key change was market-driven (demand for cheaper clothing post-1921 depression)[cite: 14, 17, 19], leading to organizational shifts ('factory system') [cite: 31] and altered production methods (more machine work relative to hand labor, relaxed quality rules like pattern matching)[cite: 25, 30]. This utilized *existing* machinery differently rather than introducing new technology[cite: 31, 32, 33].",
    economic_conditions="Post-World War I depression beginning in 1921 severely impacted the men's clothing industry, especially the high-grade Chicago market[cite: 14, 19, 20]. This led to increased competition, firm liquidations, consolidations, and relocations[cite: 23, 37]. General unemployment in Chicago was significant during the 1921-1926 period[cite: 131, 133].",
    institutional_context="Study occurs within a unionized sector (Amalgamated Clothing Workers) with established collective bargaining, including an unemployment insurance system and work-sharing rules[cite: 8, 9, 10, 35]. However, these agreements did not prevent displacement from firm closures or negotiated dismissals[cite: 36, 37, 105]. The dismissal wage was a specific, negotiated institutional response[cite: 105]. The study notes the potential but unrealized benefit of better public employment exchanges[cite: 167].",

    # Outcomes and Conclusions
    main_findings="Displacement resulted in substantial negative consequences: only 25% found work similar to cutting after 1.5+ years[cite: 46, 193]; average unemployment duration before finding regular work was 5.2 months[cite: 90]; nearly half (46.4%) earned less than before[cite: 95]; many experienced job instability (46.5% worked in >1 trade)[cite: 77]; and a majority (61%) wished to return to cutting[cite: 99, 196]. The $500 dismissal wage provided only a slight, possibly negligible, advantage in readjustment compared to those displaced without it[cite: 153, 154, 199]. Workers aged 35-39 demonstrated the most successful readjustment[cite: 178, 189, 206].",
    conclusions="Technological/organizational changes imposed 'a heavy cost' on displaced skilled workers[cite: 100]. Readjustment was difficult, often leading to inferior jobs and dissatisfaction[cite: 161, 162]. The dismissal wage, while a progressive step[cite: 166], did not fully compensate for lost time/earnings [cite: 165] and was not an 'unqualified success' for the workers[cite: 160]. Age significantly correlated with the ability to adjust[cite: 205, 206].",

    # Quality Assessment
    methodological_limitations="Author acknowledges data incompleteness [cite: 154] and comparability issues between the dismissal wage group and others (due to volunteer bias, age/ethnicity differences, timing) [cite: 125-130, 155]. Sample size varies for different analyses. Relies on worker recall. Limited analysis of potential confounders like ethnicity[cite: 127]. Exclusion of commission workers from unemployment duration average calculation[cite: 202, 204]. Small sample sizes in some age sub-groups for analysis[cite: 177].",
    coherence_assessment="Findings are largely coherent. Quantitative data (tables on occupations, earnings, unemployment duration) consistently support the qualitative narrative and conclusions regarding the negative impacts of displacement. The cautious interpretation of the dismissal wage comparison aligns with the acknowledged methodological limitations.",
    adequacy_assessment="Data appears adequate (sufficiently rich and numerous) to support the core findings about the negative consequences of displacement for this specific group (difficult readjustment, unemployment, earnings loss, desire to return). Data adequacy for definitively assessing the dismissal wage's effectiveness is lower due to comparability issues, as noted by the author[cite: 155, 200].",
    relevance_assessment_quality="The findings are highly relevant to the review's research questions, providing direct empirical evidence on labor displacement outcomes (occupations, unemployment, wages) resulting from pre-1980 production changes in a specific historical context. The study offers valuable quantitative and qualitative detail on the adjustment process for skilled workers."
)

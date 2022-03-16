#!/bin/bash

echo "Processing Dashboard 1"
python src/cbp_tableau_scraping.py \
     --url https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsFEBFY22/SBOEncounters2808\
     --data_element "SBO Table" \
     --skip_filters '["Fiscal Year"]' \
     --label 'cbp_encounters_dashboard_1'

echo "Processing Dashboard 2"
python src/cbp_tableau_scraping.py \
    --url https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsFEBFY22/SBObyMonthDemo2808\
    --data_element "Demo FYTD by Month (2)" \
    --skip_filters '["Demographic"]' \
    --label 'cbp_encounters_dashboard_2'
